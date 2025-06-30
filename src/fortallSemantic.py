from fortallVisitor import fortallVisitor
from fortallParser import fortallParser

class SemanticAnalyzer(fortallVisitor):
    def __init__(self):
        self.symbol_table = {}  
        self.functions = {}     
        self.errors = []       
        self.current_scope = "global"
        self.current_function = None
        self.in_function = False
        self.has_main = False

    def print_symbol_table(self):
        print("Tabela de Símbolos:")
        for name, info in self.symbol_table.items():
            print(f"  {name}: {info}")
        print("\nFunções:")
        for name, info in self.functions.items():
            print(f"  {name}: {info}")
        
    def get_errors(self):
        return self.errors
        
    def add_error(self, message, ctx=None):
        if ctx:
            line = ctx.start.line
            column = ctx.start.column
            self.errors.append(f"Linha {line}, Coluna {column}: {message}")
        else:
            self.errors.append(message)
    
    def visitPrograma(self, ctx: fortallParser.ProgramaContext):
        program_name = ctx.ID().getText()

        self.symbol_table[program_name] = {
            'type': 'program',
            'scope': 'global',
            'initialized': True,
            'declared_line': ctx.start.line
        }
        
        for decl in ctx.declaracao():
            self.visit(decl)
        
        if ctx.funcaoPrincipal():
            self.has_main = True
            self.visit(ctx.funcaoPrincipal())
        else:
            self.add_error("Programa deve ter uma função principal")
        
        for func in ctx.funcao():
            self.visit(func)
            
        return len(self.errors) == 0
    
    def visitFuncaoPrincipal(self, ctx: fortallParser.FuncaoPrincipalContext):
        self.current_function = "principal"
        self.in_function = True
        
        self.functions["principal"] = {
            'return_type': 'nada',
            'parameters': [],
            'declared_line': ctx.start.line
        }
        
        old_symbol_table = self.symbol_table.copy()
        
        self.visit(ctx.bloco())
        
        self.symbol_table = old_symbol_table
        self.in_function = False
        self.current_function = None
    
    def visitDeclaracaoFuncao(self, ctx: fortallParser.DeclaracaoFuncaoContext):
        func_name = ctx.ID().getText()
        return_type = ctx.getChild(1).getText()  # nada ou tipo
        
        if func_name in self.functions:
            self.add_error(f"Função '{func_name}' já declarada", ctx)
            return
        
        parameters = []
        if ctx.parametros():
            param_ctx = ctx.parametros()
            for i in range(0, len(param_ctx.children), 3):  # tipo ID, tipo ID...
                if i + 1 < len(param_ctx.children):
                    param_type = param_ctx.children[i].getText()
                    param_name = param_ctx.children[i + 1].getText()
                    parameters.append({'type': param_type, 'name': param_name})
        
        self.functions[func_name] = {
            'return_type': return_type,
            'parameters': parameters,
            'declared_line': ctx.start.line
        }
        
        old_function = self.current_function
        old_in_function = self.in_function
        old_symbol_table = self.symbol_table.copy()
        
        self.current_function = func_name
        self.in_function = True
        
        for param in parameters:
            self.symbol_table[param['name']] = {
                'type': param['type'],
                'scope': 'local',
                'initialized': True
            }
        
        self.visit(ctx.bloco())
        
        self.current_function = old_function
        self.in_function = old_in_function
        self.symbol_table = old_symbol_table
    
    def visitDeclaracaoVariavel(self, ctx: fortallParser.DeclaracaoVariavelContext):
        var_name = ctx.ID().getText()
        var_type = ctx.tipo().getText()
        
        if var_name in self.symbol_table:
            if self.symbol_table[var_name]['scope'] == self.current_scope:
                self.add_error(f"Variável '{var_name}' já declarada neste escopo", ctx)
                return
        
        initialized = ctx.expressao() is not None
        if initialized:
            expr_type = self.visit(ctx.expressao())
            if not self.is_type_compatible(var_type, expr_type):
                self.add_error(f"Tipo incompatível na inicialização da variável '{var_name}'. Esperado: {var_type}, Encontrado: {expr_type}", ctx)
        
        self.symbol_table[var_name] = {
            'type': var_type,
            'scope': self.current_scope,
            'initialized': initialized,
            'declared_line': ctx.start.line
        }
    
    def visitAtribuicao(self, ctx: fortallParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            self.add_error(f"Variável '{var_name}' não declarada", ctx)
            return
        
        expr_type = self.visit(ctx.expressao())
        var_type = self.symbol_table[var_name]['type']

        if not self.is_type_compatible(var_type, expr_type):
            self.add_error(f"Tipo incompatível na atribuição. Variável '{var_name}' é do tipo {var_type}, mas expressão é do tipo {expr_type}", ctx)
        
        self.symbol_table[var_name]['initialized'] = True
    
    def visitComandoSe(self, ctx: fortallParser.ComandoSeContext):
        condition_type = self.visit(ctx.expressao())
        
        if condition_type not in ['int', 'bool']:
            self.add_error("Condição do 'se' deve ser do tipo inteiro ou booleano", ctx)
        
        self.visit(ctx.comando(0))
        if len(ctx.comando()) > 1:  # tem senao
            self.visit(ctx.comando(1))

    
    def visitComandoEnquanto(self, ctx: fortallParser.ComandoEnquantoContext):
        condition_type = self.visit(ctx.expressao())
        
        if condition_type not in ['int', 'bool']:
            self.add_error("Condição do 'enquanto' deve ser do tipo inteiro ou booleano", ctx)
        
        self.visit(ctx.comando())

    
    def visitComandoEscreva(self, ctx: fortallParser.ComandoEscrevaContext):
        self.visit(ctx.listaExpressoes())
    
    def visitComandoLeia(self, ctx: fortallParser.ComandoLeiaContext):
        var_name = ctx.ID().getText()
        
        if var_name not in self.symbol_table:
            self.add_error(f"Variável '{var_name}' não declarada", ctx)
        else:
            self.symbol_table[var_name]['initialized'] = True
    
    def visitComandoRetorna(self, ctx: fortallParser.ComandoRetornaContext):
        if not self.in_function:
            self.add_error("Comando 'retorna' fora de função", ctx)
            return
        
        func_info = self.functions.get(self.current_function)
        if not func_info:
            return
        
        expected_type = func_info['return_type']
        
        if ctx.expressao():
            expr_type = self.visit(ctx.expressao())
            if expected_type == 'nada':
                self.add_error(f"Função '{self.current_function}' não deve retornar valor", ctx)
            elif not self.is_type_compatible(expected_type, expr_type):
                self.add_error(f"Tipo de retorno incompatível. Esperado: {expected_type}, Encontrado: {expr_type}", ctx)
        else:
            if expected_type != 'nada':
                self.add_error(f"Função '{self.current_function}' deve retornar valor do tipo {expected_type}", ctx)
    
    def visitChamadaFuncao(self, ctx: fortallParser.ChamadaFuncaoContext):
        func_name = ctx.ID().getText()
        
        if func_name not in self.functions:
            self.add_error(f"Função '{func_name}' não declarada", ctx)
            return 'unknown'
        
        func_info = self.functions[func_name]
        expected_params = func_info['parameters']
        
        actual_args = []
        if ctx.argumentos():
            for expr in ctx.argumentos().expressao():
                arg_type = self.visit(expr)
                actual_args.append(arg_type)
        
        if len(actual_args) != len(expected_params):
            self.add_error(f"Função '{func_name}' espera {len(expected_params)} argumentos, mas recebeu {len(actual_args)}", ctx)
            return func_info['return_type']
        
        for i, (actual, expected) in enumerate(zip(actual_args, expected_params)):
            if not self.is_type_compatible(expected['type'], actual):
                self.add_error(f"Argumento {i+1} da função '{func_name}': esperado {expected['type']}, encontrado {actual}", ctx)
        
        return func_info['return_type']
    
    def visitExpressaoPrimaria(self, ctx: fortallParser.ExpressaoPrimariaContext):
        # Boolean literal - DEVE VIR PRIMEIRO para capturar true e false
        if ctx.BOOLEAN():
            return "bool"
        
        elif ctx.STRING():
            return "string"
        
        elif ctx.NUMERO():
            return "int"
        
        # Variável (ID) - DEVE VIR DEPOIS dos literais
        elif ctx.ID():
            var_name = ctx.ID().getText()
            
            # Verifica primeiro se é um literal booleano disfarçado de ID
            if var_name in ['true', 'false']:
                return "bool"
            
            if var_name not in self.symbol_table:
                self.add_error(f"Variável '{var_name}' não foi declarada", ctx)
                return "error"
            
            if not self.symbol_table[var_name]['initialized']:
                self.add_error(f"Variável '{var_name}' usada antes de ser inicializada", ctx)
            
            return self.symbol_table[var_name]['type']
        
        elif ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        
        elif ctx.expressao():
            return self.visit(ctx.expressao())
        
        return "error"
    
    def visitExpressaoAditiva(self, ctx: fortallParser.ExpressaoAditivaContext):
        if len(ctx.expressaoMultiplicativa()) == 1:
            return self.visit(ctx.expressaoMultiplicativa(0))
        
        left_type = self.visit(ctx.expressaoMultiplicativa(0))
        
        for i in range(1, len(ctx.expressaoMultiplicativa())):
            right_type = self.visit(ctx.expressaoMultiplicativa(i))
            
            if left_type != "int" or right_type != "int":
                self.add_error("Operação aritmética requer operandos do tipo inteiro", ctx)
                return "error"
            
            left_type = "int"  # Resultado é inteiro
        
        return left_type
    
    def visitExpressaoMultiplicativa(self, ctx: fortallParser.ExpressaoMultiplicativaContext):
        if len(ctx.expressaoUnaria()) == 1:
            return self.visit(ctx.expressaoUnaria(0))
        
        left_type = self.visit(ctx.expressaoUnaria(0))
        
        for i in range(1, len(ctx.expressaoUnaria())):
            right_type = self.visit(ctx.expressaoUnaria(i))
            
            if left_type != "int" or right_type != "int":
                self.add_error("Operação aritmética requer operandos do tipo inteiro", ctx)
                return "error"
            
            left_type = "int"  # Resultado é inteiro
        
        return left_type
    
    def visitExpressaoUnaria(self, ctx: fortallParser.ExpressaoUnariaContext):
        expr_type = self.visit(ctx.expressaoPrimaria())
        
        if ctx.getChildCount() == 1:
            return expr_type
        
        operator = ctx.getChild(0).getText()
        
        if operator == '!':
            if expr_type != "bool":
                self.add_error("Operador '!' requer operando do tipo bool", ctx)
                return "error"
            return "bool"
        
        elif operator in ['+', '-']:
            if expr_type != "int":
                self.add_error(f"Operador '{operator}' requer operando do tipo inteiro", ctx)
                return "error"
            return "int"
        
        return expr_type
    
    def visitComandoEscreva(self, ctx: fortallParser.ComandoEscrevaContext):
        return self.visit(ctx.listaExpressoes())
    
    def visitListaExpressoes(self, ctx: fortallParser.ListaExpressoesContext):
        for expr in ctx.expressao():
            self.visit(expr)  # Não importa o tipo de retorno para escreva
        return "void"
    
    def visitExpressao(self, ctx: fortallParser.ExpressaoContext):
        return self.visit(ctx.expressaoOu())
    
    def visitExpressaoOu(self, ctx: fortallParser.ExpressaoOuContext):
        if len(ctx.expressaoE()) == 1:
            return self.visit(ctx.expressaoE(0))
        
        for expr_e in ctx.expressaoE():
            expr_type = self.visit(expr_e)
            if expr_type != "int":
                self.add_error("Operação lógica '||' requer operandos do tipo inteiro", ctx)
                return "error"
        
        return "int"
    
    def visitExpressaoE(self, ctx: fortallParser.ExpressaoEContext):
        if len(ctx.expressaoIgualdade()) == 1:
            return self.visit(ctx.expressaoIgualdade(0))
        
        for expr_igualdade in ctx.expressaoIgualdade():
            expr_type = self.visit(expr_igualdade)
            if expr_type != "int":
                self.add_error("Operação lógica '&&' requer operandos do tipo inteiro", ctx)
                return "error"
        
        return "int"
    
    def visitExpressaoIgualdade(self, ctx: fortallParser.ExpressaoIgualdadeContext):
        if len(ctx.expressaoRelacional()) == 1:
            return self.visit(ctx.expressaoRelacional(0))
        
        left_type = self.visit(ctx.expressaoRelacional(0))
        
        for i in range(1, len(ctx.expressaoRelacional())):
            right_type = self.visit(ctx.expressaoRelacional(i))
            
            if left_type != right_type and left_type != "error" and right_type != "error":
                self.add_error("Operação de igualdade requer operandos do mesmo tipo", ctx)
                return "error"
        
        return "int"
    
    def visitExpressaoRelacional(self, ctx: fortallParser.ExpressaoRelacionalContext):
        if len(ctx.expressaoAditiva()) == 1:
            return self.visit(ctx.expressaoAditiva(0))
        
        for expr_aditiva in ctx.expressaoAditiva():
            expr_type = self.visit(expr_aditiva)
            if expr_type != "int":
                self.add_error("Operação relacional requer operandos do tipo inteiro", ctx)
                return "error"
        
        return "int"
    
    def is_type_compatible(self, expected, actual):
        if actual == 'unknown':
            return True
        return expected == actual
    
    def defaultResult(self):
        return 'unknown'