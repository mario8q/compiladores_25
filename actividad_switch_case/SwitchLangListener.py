# Generated from SwitchLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwitchLangParser import SwitchLangParser
else:
    from SwitchLangParser import SwitchLangParser

# This class defines a complete listener for a parse tree produced by SwitchLangParser.
class SwitchLangListener(ParseTreeListener):

    # Enter a parse tree produced by SwitchLangParser#programa.
    def enterPrograma(self, ctx:SwitchLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#programa.
    def exitPrograma(self, ctx:SwitchLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#sentencia.
    def enterSentencia(self, ctx:SwitchLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#sentencia.
    def exitSentencia(self, ctx:SwitchLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#switchStmt.
    def enterSwitchStmt(self, ctx:SwitchLangParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#switchStmt.
    def exitSwitchStmt(self, ctx:SwitchLangParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#asignacion.
    def enterAsignacion(self, ctx:SwitchLangParser.AsignacionContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#asignacion.
    def exitAsignacion(self, ctx:SwitchLangParser.AsignacionContext):
        pass



del SwitchLangParser