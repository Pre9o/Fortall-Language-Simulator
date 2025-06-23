from fortallVisitor import fortallVisitor
from fortallParser import fortallParser

class FortallInterpreter(fortallVisitor):
    def __init__(self):
        self.global_variables = {}  
        self.local_variables = {}   
        self.functions = {}         
        self.call_stack = []        
        self.return_value = None    
        self.should_return = False  
        self.output = []           
        
    def get_output(self):
        return self.output
    
    def get_variable_value(self, name):
        if name in self.local_variables:
            return self.local_variables[name]
        elif name in self.global_variables:
            return self.global_variables[name]
        else:
            raise RuntimeError(f"Variável '{name}' não encontrada")
    
    def set_variable_value(self, name, value):
        if name in self.local_variables:
            self.local_variables[name] = value
        elif name in self.global_variables:
            self.global_variables[name] = value
        else:
            if self.call_stack:
                self.local_variables[name] = value
            else:
                self.global_variables[name] = value
    
    def visitPrograma(self, ctx: fortallParser.ProgramaContext):
        for func in ctx.funcao():
            self.visit(func)
        
        for decl in ctx.declaracao():
            self.visit(decl)
        
        if ctx.funcaoPrincipal():
            self.visit(ctx.funcaoPrincipal())
        
        return True
    
    def visitFuncaoPrincipal(self, ctx: fortallParser.FuncaoPrincipalContext):
        self.functions["principal"] = {
            'context': ctx,
            'parameters': [],
            'return_type': 'nada'
        }
        
        self.call_stack.append("principal")
        old_locals = self.local_variables.copy()
        self.local_variables = {}
        
        self.visit(ctx.bloco())
        
        self.local_variables = old_locals
        self.call_stack.pop()
    
    def visitDeclaracaoFuncao(self, ctx: fortallParser.DeclaracaoFuncaoContext):
        func_name = ctx.ID().getText()
        return_type = ctx.getChild(1).getText()
        
        parameters = []
        if ctx.parametros():
            param_ctx = ctx.parametros()
            for i in range(0, len(param_ctx.children), 3):
                if i + 1 < len(param_ctx.children):
                    param_type = param_ctx.children[i].getText()
                    param_name = param_ctx.children[i + 1].getText()
                    parameters.append({'type': param_type, 'name': param_name})
        
        self.functions[func_name] = {
            'context': ctx,
            'parameters': parameters,
            'return_type': return_type
        }
    
    def visitDeclaracaoVariavel(self, ctx: fortallParser.DeclaracaoVariavelContext):
        var_name = ctx.ID().getText()
        var_type = ctx.tipo().getText()
        
        if var_type == 'int':
            initial_value = 0
        elif var_type == 'bool':
            initial_value = False
        else:
            initial_value = None
        
        # Se há inicialização, calcula o valor
        if ctx.expressao():
            initial_value = self.visit(ctx.expressao())
        
        if self.call_stack:
            self.local_variables[var_name] = initial_value
        else:
            self.global_variables[var_name] = initial_value
    
    def visitAtribuicao(self, ctx: fortallParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expressao())
        self.set_variable_value(var_name, value)
    
    def visitComandoSe(self, ctx: fortallParser.ComandoSeContext):
        condition = self.visit(ctx.expressao())
        
        # Em Fortall, condições são inteiros (0 = falso, != 0 = verdadeiro)
        if condition != 0:
            self.visit(ctx.comando(0))
        elif len(ctx.comando()) > 1:  # tem else
            self.visit(ctx.comando(1))
    
    def visitComandoEnquanto(self, ctx: fortallParser.ComandoEnquantoContext):
        while True:
            condition = self.visit(ctx.expressao())
            if condition == 0:  # 0 = falso
                break
            
            self.visit(ctx.comando())
            
            # Verifica se houve return
            if self.should_return:
                break
    
    def visitComandoEscreva(self, ctx: fortallParser.ComandoEscrevaContext):
        values = self.visit(ctx.listaExpressoes())
        output_line = " ".join(str(v) for v in values)
        self.output.append(output_line)
        print(output_line)  # também imprime no console
    
    def visitComandoLeia(self, ctx: fortallParser.ComandoLeiaContext):
        var_name = ctx.ID().getText()
        try:
            user_input = input(f"Digite o valor para {var_name}: ")
            try:
                value = int(user_input)
            except ValueError:
                value = user_input
            
            self.set_variable_value(var_name, value)
        except EOFError:
            self.set_variable_value(var_name, 0)
    
    def visitComandoRetorna(self, ctx: fortallParser.ComandoRetornaContext):
        if ctx.expressao():
            self.return_value = self.visit(ctx.expressao())
        else:
            self.return_value = None
        
        self.should_return = True
    
    def visitChamadaFuncao(self, ctx: fortallParser.ChamadaFuncaoContext):
        func_name = ctx.ID().getText()
        
        if func_name not in self.functions:
            raise RuntimeError(f"Função '{func_name}' não encontrada")
        
        func_info = self.functions[func_name]
        
        args = []
        if ctx.argumentos():
            for expr in ctx.argumentos().expressao():
                args.append(self.visit(expr))
        
        old_locals = self.local_variables.copy()
        old_return = self.should_return
        old_return_value = self.return_value
        
        self.local_variables = {}
        self.should_return = False
        self.return_value = None
        
        for i, param in enumerate(func_info['parameters']):
            if i < len(args):
                self.local_variables[param['name']] = args[i]
        
        self.call_stack.append(func_name)
        self.visit(func_info['context'].bloco())
        self.call_stack.pop()
        
        result = self.return_value
        
        self.local_variables = old_locals
        self.should_return = old_return
        self.return_value = old_return_value
        
        return result if result is not None else 0
    
    def visitBloco(self, ctx: fortallParser.BlocoContext):
        for comando in ctx.comando():
            self.visit(comando)
            if self.should_return:
                break
    
    def visitListaExpressoes(self, ctx: fortallParser.ListaExpressoesContext):
        values = []
        for expr in ctx.expressao():
            values.append(self.visit(expr))
        return values
    
    def visitExpressao(self, ctx: fortallParser.ExpressaoContext):
        return self.visit(ctx.expressaoOu())
    
    def visitExpressaoOu(self, ctx: fortallParser.ExpressaoOuContext):
        result = self.visit(ctx.expressaoE(0))
        
        for i in range(1, len(ctx.expressaoE())):
            right = self.visit(ctx.expressaoE(i))
            result = 1 if (result != 0 or right != 0) else 0
        
        return result
    
    def visitExpressaoE(self, ctx: fortallParser.ExpressaoEContext):
        result = self.visit(ctx.expressaoIgualdade(0))
        
        for i in range(1, len(ctx.expressaoIgualdade())):
            right = self.visit(ctx.expressaoIgualdade(i))
            result = 1 if (result != 0 and right != 0) else 0
        
        return result
    
    def visitExpressaoIgualdade(self, ctx: fortallParser.ExpressaoIgualdadeContext):
        result = self.visit(ctx.expressaoRelacional(0))
        
        for i in range(1, len(ctx.expressaoRelacional())):
            operator = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.expressaoRelacional(i))
            
            if operator == '==':
                result = 1 if result == right else 0
            elif operator == '!=':
                result = 1 if result != right else 0
        
        return result
    
    def visitExpressaoRelacional(self, ctx: fortallParser.ExpressaoRelacionalContext):
        result = self.visit(ctx.expressaoAditiva(0))
        
        for i in range(1, len(ctx.expressaoAditiva())):
            operator = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.expressaoAditiva(i))
            
            if operator == '<':
                result = 1 if result < right else 0
            elif operator == '>':
                result = 1 if result > right else 0
            elif operator == '<=':
                result = 1 if result <= right else 0
            elif operator == '>=':
                result = 1 if result >= right else 0
        
        return result
    
    def visitExpressaoAditiva(self, ctx: fortallParser.ExpressaoAditivaContext):
        result = self.visit(ctx.expressaoMultiplicativa(0))
        
        for i in range(1, len(ctx.expressaoMultiplicativa())):
            operator = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.expressaoMultiplicativa(i))
            
            if operator == '+':
                result = result + right
            elif operator == '-':
                result = result - right
        
        return result
    
    def visitExpressaoMultiplicativa(self, ctx: fortallParser.ExpressaoMultiplicativaContext):
        result = self.visit(ctx.expressaoUnaria(0))
        
        for i in range(1, len(ctx.expressaoUnaria())):
            operator = ctx.getChild(2*i-1).getText()
            right = self.visit(ctx.expressaoUnaria(i))
            
            if operator == '*':
                result = result * right
            elif operator == '/':
                if right == 0:
                    raise RuntimeError("Divisão por zero")
                result = result // right  # Divisão inteira
            elif operator == '%':
                if right == 0:
                    raise RuntimeError("Divisão por zero")
                result = result % right
        
        return result
    
    def visitExpressaoUnaria(self, ctx: fortallParser.ExpressaoUnariaContext):
        if ctx.getChildCount() > 1:
            operator = ctx.getChild(0).getText()
            value = self.visit(ctx.expressaoPrimaria())
            
            if operator == '!':
                return 1 if value == 0 else 0  # NOT lógico
            elif operator == '-':
                return -value
            elif operator == '+':
                return value
        
        return self.visit(ctx.expressaoPrimaria())
    
    def visitExpressaoPrimaria(self, ctx: fortallParser.ExpressaoPrimariaContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        
        # Boolean literal
        elif ctx.BOOLEAN():
            return 1 if ctx.BOOLEAN().getText() == 'true' else 0
        
        elif ctx.STRING():
            text = ctx.STRING().getText()
            # Remove aspas e processa escapes
            return text[1:-1].replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
        
        # Variável
        elif ctx.ID():
            var_name = ctx.ID().getText()
            # Verifica se é literal booleano
            if var_name == 'true':
                return 1
            elif var_name == 'false':
                return 0
            else:
                return self.get_variable_value(var_name)
        
        elif ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        
        elif ctx.expressao():
            return self.visit(ctx.expressao())
        
        return 0
