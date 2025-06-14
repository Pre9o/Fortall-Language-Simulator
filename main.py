from antlr4 import *
from fortallLexer import fortallLexer
from fortallParser import fortallParser

code = "programa teste; retorna nada funcao principal() { int x = 10; }"


input_stream = InputStream(code)
lexer = fortallLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = fortallParser(stream)
tree = parser.programa()
print("Parsing completed successfully.")
print(tree.toStringTree(recog=parser))