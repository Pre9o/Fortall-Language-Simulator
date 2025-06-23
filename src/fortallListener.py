# Generated from fortall.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .fortallParser import fortallParser
else:
    from fortallParser import fortallParser

# This class defines a complete listener for a parse tree produced by fortallParser.
class fortallListener(ParseTreeListener):

    # Enter a parse tree produced by fortallParser#programa.
    def enterPrograma(self, ctx:fortallParser.ProgramaContext):
        pass

    # Exit a parse tree produced by fortallParser#programa.
    def exitPrograma(self, ctx:fortallParser.ProgramaContext):
        pass


    # Enter a parse tree produced by fortallParser#funcaoPrincipal.
    def enterFuncaoPrincipal(self, ctx:fortallParser.FuncaoPrincipalContext):
        pass

    # Exit a parse tree produced by fortallParser#funcaoPrincipal.
    def exitFuncaoPrincipal(self, ctx:fortallParser.FuncaoPrincipalContext):
        pass


    # Enter a parse tree produced by fortallParser#declaracao.
    def enterDeclaracao(self, ctx:fortallParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by fortallParser#declaracao.
    def exitDeclaracao(self, ctx:fortallParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by fortallParser#declaracaoVariavel.
    def enterDeclaracaoVariavel(self, ctx:fortallParser.DeclaracaoVariavelContext):
        pass

    # Exit a parse tree produced by fortallParser#declaracaoVariavel.
    def exitDeclaracaoVariavel(self, ctx:fortallParser.DeclaracaoVariavelContext):
        pass


    # Enter a parse tree produced by fortallParser#declaracaoFuncao.
    def enterDeclaracaoFuncao(self, ctx:fortallParser.DeclaracaoFuncaoContext):
        pass

    # Exit a parse tree produced by fortallParser#declaracaoFuncao.
    def exitDeclaracaoFuncao(self, ctx:fortallParser.DeclaracaoFuncaoContext):
        pass


    # Enter a parse tree produced by fortallParser#funcao.
    def enterFuncao(self, ctx:fortallParser.FuncaoContext):
        pass

    # Exit a parse tree produced by fortallParser#funcao.
    def exitFuncao(self, ctx:fortallParser.FuncaoContext):
        pass


    # Enter a parse tree produced by fortallParser#parametros.
    def enterParametros(self, ctx:fortallParser.ParametrosContext):
        pass

    # Exit a parse tree produced by fortallParser#parametros.
    def exitParametros(self, ctx:fortallParser.ParametrosContext):
        pass


    # Enter a parse tree produced by fortallParser#tipo.
    def enterTipo(self, ctx:fortallParser.TipoContext):
        pass

    # Exit a parse tree produced by fortallParser#tipo.
    def exitTipo(self, ctx:fortallParser.TipoContext):
        pass


    # Enter a parse tree produced by fortallParser#bloco.
    def enterBloco(self, ctx:fortallParser.BlocoContext):
        pass

    # Exit a parse tree produced by fortallParser#bloco.
    def exitBloco(self, ctx:fortallParser.BlocoContext):
        pass


    # Enter a parse tree produced by fortallParser#comando.
    def enterComando(self, ctx:fortallParser.ComandoContext):
        pass

    # Exit a parse tree produced by fortallParser#comando.
    def exitComando(self, ctx:fortallParser.ComandoContext):
        pass


    # Enter a parse tree produced by fortallParser#atribuicao.
    def enterAtribuicao(self, ctx:fortallParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by fortallParser#atribuicao.
    def exitAtribuicao(self, ctx:fortallParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by fortallParser#comandoSe.
    def enterComandoSe(self, ctx:fortallParser.ComandoSeContext):
        pass

    # Exit a parse tree produced by fortallParser#comandoSe.
    def exitComandoSe(self, ctx:fortallParser.ComandoSeContext):
        pass


    # Enter a parse tree produced by fortallParser#comandoEnquanto.
    def enterComandoEnquanto(self, ctx:fortallParser.ComandoEnquantoContext):
        pass

    # Exit a parse tree produced by fortallParser#comandoEnquanto.
    def exitComandoEnquanto(self, ctx:fortallParser.ComandoEnquantoContext):
        pass


    # Enter a parse tree produced by fortallParser#comandoEscreva.
    def enterComandoEscreva(self, ctx:fortallParser.ComandoEscrevaContext):
        pass

    # Exit a parse tree produced by fortallParser#comandoEscreva.
    def exitComandoEscreva(self, ctx:fortallParser.ComandoEscrevaContext):
        pass


    # Enter a parse tree produced by fortallParser#comandoLeia.
    def enterComandoLeia(self, ctx:fortallParser.ComandoLeiaContext):
        pass

    # Exit a parse tree produced by fortallParser#comandoLeia.
    def exitComandoLeia(self, ctx:fortallParser.ComandoLeiaContext):
        pass


    # Enter a parse tree produced by fortallParser#comandoRetorna.
    def enterComandoRetorna(self, ctx:fortallParser.ComandoRetornaContext):
        pass

    # Exit a parse tree produced by fortallParser#comandoRetorna.
    def exitComandoRetorna(self, ctx:fortallParser.ComandoRetornaContext):
        pass


    # Enter a parse tree produced by fortallParser#listaExpressoes.
    def enterListaExpressoes(self, ctx:fortallParser.ListaExpressoesContext):
        pass

    # Exit a parse tree produced by fortallParser#listaExpressoes.
    def exitListaExpressoes(self, ctx:fortallParser.ListaExpressoesContext):
        pass


    # Enter a parse tree produced by fortallParser#expressao.
    def enterExpressao(self, ctx:fortallParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by fortallParser#expressao.
    def exitExpressao(self, ctx:fortallParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoOu.
    def enterExpressaoOu(self, ctx:fortallParser.ExpressaoOuContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoOu.
    def exitExpressaoOu(self, ctx:fortallParser.ExpressaoOuContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoE.
    def enterExpressaoE(self, ctx:fortallParser.ExpressaoEContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoE.
    def exitExpressaoE(self, ctx:fortallParser.ExpressaoEContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoIgualdade.
    def enterExpressaoIgualdade(self, ctx:fortallParser.ExpressaoIgualdadeContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoIgualdade.
    def exitExpressaoIgualdade(self, ctx:fortallParser.ExpressaoIgualdadeContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoRelacional.
    def enterExpressaoRelacional(self, ctx:fortallParser.ExpressaoRelacionalContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoRelacional.
    def exitExpressaoRelacional(self, ctx:fortallParser.ExpressaoRelacionalContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoAditiva.
    def enterExpressaoAditiva(self, ctx:fortallParser.ExpressaoAditivaContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoAditiva.
    def exitExpressaoAditiva(self, ctx:fortallParser.ExpressaoAditivaContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoMultiplicativa.
    def enterExpressaoMultiplicativa(self, ctx:fortallParser.ExpressaoMultiplicativaContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoMultiplicativa.
    def exitExpressaoMultiplicativa(self, ctx:fortallParser.ExpressaoMultiplicativaContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoUnaria.
    def enterExpressaoUnaria(self, ctx:fortallParser.ExpressaoUnariaContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoUnaria.
    def exitExpressaoUnaria(self, ctx:fortallParser.ExpressaoUnariaContext):
        pass


    # Enter a parse tree produced by fortallParser#expressaoPrimaria.
    def enterExpressaoPrimaria(self, ctx:fortallParser.ExpressaoPrimariaContext):
        pass

    # Exit a parse tree produced by fortallParser#expressaoPrimaria.
    def exitExpressaoPrimaria(self, ctx:fortallParser.ExpressaoPrimariaContext):
        pass


    # Enter a parse tree produced by fortallParser#chamadaFuncao.
    def enterChamadaFuncao(self, ctx:fortallParser.ChamadaFuncaoContext):
        pass

    # Exit a parse tree produced by fortallParser#chamadaFuncao.
    def exitChamadaFuncao(self, ctx:fortallParser.ChamadaFuncaoContext):
        pass


    # Enter a parse tree produced by fortallParser#argumentos.
    def enterArgumentos(self, ctx:fortallParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by fortallParser#argumentos.
    def exitArgumentos(self, ctx:fortallParser.ArgumentosContext):
        pass



del fortallParser