import os
from antlr4 import *
from fortallLexer import fortallLexer
from fortallParser import fortallParser
from fortallSemantic import SemanticAnalyzer
from fortallInterpreter import FortallInterpreter

# Configuração dos exemplos
examples = {
    "1": {
        "title": "Exemplo 1 - Apenas função principal",
        "description": "Programa simples com apenas a função principal que faz operações básicas",
        "file": "exemplo1.txt"
    },
    "2": {
        "title": "Exemplo 2 - Função principal + função auxiliar",
        "description": "Programa com função principal e uma função auxiliar para cálculos",
        "file": "exemplo2.txt"
    },
    "3": {
        "title": "Exemplo 3 - Fibonacci recursivo",
        "description": "Implementação recursiva da sequência de Fibonacci",
        "file": "exemplo3.txt"
    },
    "4": {
        "title": "Exemplo 4 - Calculadora interativa",
        "description": "Calculadora que lê números do usuário e realiza operações matemáticas",
        "file": "exemplo4.txt"
    },
    "5": {
        "title": "Exemplo 5 - Jogo de adivinhação interativo",
        "description": "Jogo onde o usuário tenta adivinhar um número secreto com dicas",
        "file": "exemplo5.txt"
    }
}

def load_example_code(filename):
    """Carrega o código de um arquivo de exemplo"""
    examples_dir = os.path.join(os.path.dirname(__file__), "examples")
    file_path = os.path.join(examples_dir, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None

def show_menu():
    print("\n" + "="*50)
    print("     SIMULADOR DA LINGUAGEM FORTALL")
    print("="*50)
    print("Escolha um exemplo para executar:")
    print()
    
    for key, example in examples.items():
        print(f"{key}. {example['title']}")
        print(f"   {example['description']}")
        print(f"Arquivo: {example['file']}")
        print()
    
    print("0. Sair")
    print("="*50)

def execute_example(code, title):
    print(f"\nExecutando: {title}")
    print("="*60)
    
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
            print("\nSaída do programa:")
            print("-" * 40)
            
            interpreter = FortallInterpreter()
            interpreter.visit(tree)
            
            print("-" * 40)
            print("Programa executado com sucesso")
            
            # Mostra o estado final das variáveis globais
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

def show_code(code, title, filename):
    print(f"\nCódigo fonte - {title}")
    print(f"Arquivo: examples/{filename}")
    print("="*60)
    print(code.strip())
    print("="*60)

def list_example_files():
    """Lista todos os arquivos de exemplo disponíveis"""
    examples_dir = os.path.join(os.path.dirname(__file__), "examples")
    
    if not os.path.exists(examples_dir):
        print(f"Diretório de exemplos não encontrado: {examples_dir}")
        return
    
    print(f"\nArquivos encontrados em {examples_dir}:")
    try:
        files = os.listdir(examples_dir)
        fortall_files = [f for f in files if f.endswith('.txt')]
        
        if fortall_files:
            for file in sorted(fortall_files):
                print(f"{file}")
        else:
            print("Nenhum arquivo .txt encontrado")
            
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

def main():
    # Verifica se o diretório de exemplos existe
    examples_dir = os.path.join(os.path.dirname(__file__), "examples")
    if not os.path.exists(examples_dir):
        print(f"Criando diretório de exemplos: {examples_dir}")
        try:
            os.makedirs(examples_dir)
            print("Diretório criado com sucesso")
            print("Por favor, adicione os arquivos de exemplo no diretório 'examples'")
        except Exception as e:
            print(f"Erro ao criar diretório: {e}")
            return
    
    while True:
        show_menu()
        
        try:
            choice = input("Digite sua escolha: ").strip()
            
            if choice == "0":
                print("\nObrigado por usar o Simulador Fortall!")
                break
                
            elif choice.lower() in ['help', 'ajuda', 'h']:
                list_example_files()
                input("\nPressione Enter para continuar...")
                continue
                
            elif choice in examples:
                example = examples[choice]
                
                # Carrega o código do arquivo
                code = load_example_code(example["file"])
                
                if code is None:
                    print("Não foi possível carregar o exemplo.")
                    input("Pressione Enter para continuar...")
                    continue
                
                show_code(code, example["title"], example["file"])
                
                execute = input("\nDeseja executar este exemplo? (s/n): ").strip().lower()
                
                if execute in ['s', 'sim', 'y', 'yes']:
                    success = execute_example(code, example["title"])
                    
                    if success:
                        input("\nPressione Enter para continuar...")
                else:
                    print("Exemplo não executado.")
                    
            else:
                print("Opção inválida! Tente novamente.")
                print("Digite 'help' para ver os arquivos disponíveis.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()