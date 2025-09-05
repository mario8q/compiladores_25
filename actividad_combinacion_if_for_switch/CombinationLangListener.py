# Generated from CombinationLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CombinationLangParser import CombinationLangParser
else:
    from CombinationLangParser import CombinationLangParser

# This class defines a complete listener for a parse tree produced by CombinationLangParser.
class CombinationLangListener(ParseTreeListener):

    # Enter a parse tree produced by CombinationLangParser#programa.
    def enterPrograma(self, ctx:CombinationLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#programa.
    def exitPrograma(self, ctx:CombinationLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#sentencia.
    def enterSentencia(self, ctx:CombinationLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#sentencia.
    def exitSentencia(self, ctx:CombinationLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#asignacion.
    def enterAsignacion(self, ctx:CombinationLangParser.AsignacionContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#asignacion.
    def exitAsignacion(self, ctx:CombinationLangParser.AsignacionContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#forStmt.
    def enterForStmt(self, ctx:CombinationLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#forStmt.
    def exitForStmt(self, ctx:CombinationLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#condicion.
    def enterCondicion(self, ctx:CombinationLangParser.CondicionContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#condicion.
    def exitCondicion(self, ctx:CombinationLangParser.CondicionContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#paso.
    def enterPaso(self, ctx:CombinationLangParser.PasoContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#paso.
    def exitPaso(self, ctx:CombinationLangParser.PasoContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#switchStmt.
    def enterSwitchStmt(self, ctx:CombinationLangParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#switchStmt.
    def exitSwitchStmt(self, ctx:CombinationLangParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#case.
    def enterCase(self, ctx:CombinationLangParser.CaseContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#case.
    def exitCase(self, ctx:CombinationLangParser.CaseContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#default.
    def enterDefault(self, ctx:CombinationLangParser.DefaultContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#default.
    def exitDefault(self, ctx:CombinationLangParser.DefaultContext):
        pass


    # Enter a parse tree produced by CombinationLangParser#ifStmt.
    def enterIfStmt(self, ctx:CombinationLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CombinationLangParser#ifStmt.
    def exitIfStmt(self, ctx:CombinationLangParser.IfStmtContext):
        pass



del CombinationLangParser