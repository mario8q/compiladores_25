# Generated from ForLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ForLangParser import ForLangParser
else:
    from ForLangParser import ForLangParser

# This class defines a complete listener for a parse tree produced by ForLangParser.
class ForLangListener(ParseTreeListener):

    # Enter a parse tree produced by ForLangParser#programa.
    def enterPrograma(self, ctx:ForLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ForLangParser#programa.
    def exitPrograma(self, ctx:ForLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ForLangParser#sentencia.
    def enterSentencia(self, ctx:ForLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ForLangParser#sentencia.
    def exitSentencia(self, ctx:ForLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ForLangParser#forStmt.
    def enterForStmt(self, ctx:ForLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by ForLangParser#forStmt.
    def exitForStmt(self, ctx:ForLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by ForLangParser#indice.
    def enterIndice(self, ctx:ForLangParser.IndiceContext):
        pass

    # Exit a parse tree produced by ForLangParser#indice.
    def exitIndice(self, ctx:ForLangParser.IndiceContext):
        pass


    # Enter a parse tree produced by ForLangParser#condicion.
    def enterCondicion(self, ctx:ForLangParser.CondicionContext):
        pass

    # Exit a parse tree produced by ForLangParser#condicion.
    def exitCondicion(self, ctx:ForLangParser.CondicionContext):
        pass


    # Enter a parse tree produced by ForLangParser#paso.
    def enterPaso(self, ctx:ForLangParser.PasoContext):
        pass

    # Exit a parse tree produced by ForLangParser#paso.
    def exitPaso(self, ctx:ForLangParser.PasoContext):
        pass



del ForLangParser