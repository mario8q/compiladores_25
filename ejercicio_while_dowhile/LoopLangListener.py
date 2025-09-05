# Generated from LoopLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LoopLangParser import LoopLangParser
else:
    from LoopLangParser import LoopLangParser

# This class defines a complete listener for a parse tree produced by LoopLangParser.
class LoopLangListener(ParseTreeListener):

    # Enter a parse tree produced by LoopLangParser#programa.
    def enterPrograma(self, ctx:LoopLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LoopLangParser#programa.
    def exitPrograma(self, ctx:LoopLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LoopLangParser#sentencia.
    def enterSentencia(self, ctx:LoopLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LoopLangParser#sentencia.
    def exitSentencia(self, ctx:LoopLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LoopLangParser#whileStmt.
    def enterWhileStmt(self, ctx:LoopLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by LoopLangParser#whileStmt.
    def exitWhileStmt(self, ctx:LoopLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by LoopLangParser#doWhileStmt.
    def enterDoWhileStmt(self, ctx:LoopLangParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by LoopLangParser#doWhileStmt.
    def exitDoWhileStmt(self, ctx:LoopLangParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by LoopLangParser#asignacion.
    def enterAsignacion(self, ctx:LoopLangParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LoopLangParser#asignacion.
    def exitAsignacion(self, ctx:LoopLangParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LoopLangParser#breakStmt.
    def enterBreakStmt(self, ctx:LoopLangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by LoopLangParser#breakStmt.
    def exitBreakStmt(self, ctx:LoopLangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by LoopLangParser#continueStmt.
    def enterContinueStmt(self, ctx:LoopLangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by LoopLangParser#continueStmt.
    def exitContinueStmt(self, ctx:LoopLangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by LoopLangParser#condicion.
    def enterCondicion(self, ctx:LoopLangParser.CondicionContext):
        pass

    # Exit a parse tree produced by LoopLangParser#condicion.
    def exitCondicion(self, ctx:LoopLangParser.CondicionContext):
        pass


    # Enter a parse tree produced by LoopLangParser#expr.
    def enterExpr(self, ctx:LoopLangParser.ExprContext):
        pass

    # Exit a parse tree produced by LoopLangParser#expr.
    def exitExpr(self, ctx:LoopLangParser.ExprContext):
        pass



del LoopLangParser