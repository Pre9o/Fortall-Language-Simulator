from antlr4 import *
from fortallLexer import fortallLexer
from fortallParser import fortallParser
from fortallSemantic import SemanticAnalyzer
from fortallInterpreter import FortallInterpreter

# Código de teste
code = """
programa teste;

int x;
bool z = true;
int teste;

retorna nada funcao seila(int x) {
    int a = 5;
    z = false;
    escreva("Função seila executada");
    escreva(x);
}

retorna nada funcao principal() {
    x = 10;
    int y = x + 5;

    seila(x);
    
    se (x > 0) {
        escreva("x é positivo");
    }
    
    enquanto (y > 0) {
        y = y - 1;
    }

    escreva(y);
}
"""

def main():
    try:
        # Análise léxica e sintática
        input_stream = InputStream(code)
        lexer = fortallLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = fortallParser(stream)
        tree = parser.programa()
        
        print("Análise léxica e sintática concluída")
        
        # Análise semântica
        semantic_analyzer = SemanticAnalyzer()
        is_semantically_valid = semantic_analyzer.visit(tree)
        
        errors = semantic_analyzer.get_errors()
        
        if errors:
            print("\nErros semânticos encontrados:")
            for error in errors:
                print(f"  • {error}")
            return False
        else:
            print("Análise semântica concluída com sucesso")
        
        # Se passou na análise semântica, executa o programa
        if is_semantically_valid:
            print("\Executando programa:\n")
            print("-" * 40)
            
            interpreter = FortallInterpreter()
            interpreter.visit(tree)
            
            print("-" * 40)
            print("Programa executado com sucesso")
            
            if interpreter.global_variables:
                print("\nVariáveis globais finais:")
                for var, value in interpreter.global_variables.items():
                    print(f"  {var} = {value}")
        
        return True
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()