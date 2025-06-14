# Generated from fortall.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fortallParser import fortallParser
else:
    from fortallParser import fortallParser

# This class defines a complete generic visitor for a parse tree produced by fortallParser.

class fortallVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fortallParser#programa.
    def visitPrograma(self, ctx:fortallParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#funcaoPrincipal.
    def visitFuncaoPrincipal(self, ctx:fortallParser.FuncaoPrincipalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#declaracao.
    def visitDeclaracao(self, ctx:fortallParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#declaracaoVariavel.
    def visitDeclaracaoVariavel(self, ctx:fortallParser.DeclaracaoVariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#declaracaoFuncao.
    def visitDeclaracaoFuncao(self, ctx:fortallParser.DeclaracaoFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#funcao.
    def visitFuncao(self, ctx:fortallParser.FuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#parametros.
    def visitParametros(self, ctx:fortallParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#tipo.
    def visitTipo(self, ctx:fortallParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#bloco.
    def visitBloco(self, ctx:fortallParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comando.
    def visitComando(self, ctx:fortallParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#atribuicao.
    def visitAtribuicao(self, ctx:fortallParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comandoSe.
    def visitComandoSe(self, ctx:fortallParser.ComandoSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comandoEnquanto.
    def visitComandoEnquanto(self, ctx:fortallParser.ComandoEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comandoEscreva.
    def visitComandoEscreva(self, ctx:fortallParser.ComandoEscrevaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comandoLeia.
    def visitComandoLeia(self, ctx:fortallParser.ComandoLeiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#comandoRetorna.
    def visitComandoRetorna(self, ctx:fortallParser.ComandoRetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#listaExpressoes.
    def visitListaExpressoes(self, ctx:fortallParser.ListaExpressoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressao.
    def visitExpressao(self, ctx:fortallParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoOu.
    def visitExpressaoOu(self, ctx:fortallParser.ExpressaoOuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoE.
    def visitExpressaoE(self, ctx:fortallParser.ExpressaoEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoIgualdade.
    def visitExpressaoIgualdade(self, ctx:fortallParser.ExpressaoIgualdadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoRelacional.
    def visitExpressaoRelacional(self, ctx:fortallParser.ExpressaoRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoAditiva.
    def visitExpressaoAditiva(self, ctx:fortallParser.ExpressaoAditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoMultiplicativa.
    def visitExpressaoMultiplicativa(self, ctx:fortallParser.ExpressaoMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoUnaria.
    def visitExpressaoUnaria(self, ctx:fortallParser.ExpressaoUnariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#expressaoPrimaria.
    def visitExpressaoPrimaria(self, ctx:fortallParser.ExpressaoPrimariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:fortallParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fortallParser#argumentos.
    def visitArgumentos(self, ctx:fortallParser.ArgumentosContext):
        return self.visitChildren(ctx)



del fortallParser