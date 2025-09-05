# Generated from LoopLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,2,
        12,2,43,9,2,1,2,1,2,1,3,1,3,1,3,5,3,50,8,3,10,3,12,3,53,9,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,
        1,6,1,7,1,7,1,7,3,7,76,8,7,1,8,1,8,1,8,3,8,81,8,8,1,8,1,8,1,8,5,
        8,86,8,8,10,8,12,8,89,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,2,
        1,0,15,18,1,0,11,14,91,0,21,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,
        46,1,0,0,0,8,61,1,0,0,0,10,66,1,0,0,0,12,69,1,0,0,0,14,72,1,0,0,
        0,16,80,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,
        1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,
        25,1,1,0,0,0,26,32,3,4,2,0,27,32,3,6,3,0,28,32,3,8,4,0,29,32,3,10,
        5,0,30,32,3,12,6,0,31,26,1,0,0,0,31,27,1,0,0,0,31,28,1,0,0,0,31,
        29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,1,0,0,34,35,5,5,0,
        0,35,36,3,14,7,0,36,37,5,6,0,0,37,41,5,7,0,0,38,40,3,2,1,0,39,38,
        1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,
        43,41,1,0,0,0,44,45,5,8,0,0,45,5,1,0,0,0,46,47,5,2,0,0,47,51,5,7,
        0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,
        1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,8,0,0,55,56,5,1,0,0,
        56,57,5,5,0,0,57,58,3,14,7,0,58,59,5,6,0,0,59,60,5,10,0,0,60,7,1,
        0,0,0,61,62,5,19,0,0,62,63,5,9,0,0,63,64,3,16,8,0,64,65,5,10,0,0,
        65,9,1,0,0,0,66,67,5,3,0,0,67,68,5,10,0,0,68,11,1,0,0,0,69,70,5,
        4,0,0,70,71,5,10,0,0,71,13,1,0,0,0,72,75,3,16,8,0,73,74,7,0,0,0,
        74,76,3,16,8,0,75,73,1,0,0,0,75,76,1,0,0,0,76,15,1,0,0,0,77,78,6,
        8,-1,0,78,81,5,20,0,0,79,81,5,19,0,0,80,77,1,0,0,0,80,79,1,0,0,0,
        81,87,1,0,0,0,82,83,10,1,0,0,83,84,7,1,0,0,84,86,3,16,8,2,85,82,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,17,1,0,0,0,
        89,87,1,0,0,0,7,21,31,41,51,75,80,87
    ]

class LoopLangParser ( Parser ):

    grammarFileName = "LoopLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'do'", "'break'", "'continue'", 
                     "'('", "')'", "'{'", "'}'", "'='", "';'", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "WHILE", "DO", "BREAK", "CONTINUE", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "ASSIGN", "SEMI", "PLUS", 
                      "MINUS", "MUL", "DIV", "LT", "GT", "EQ", "NEQ", "ID", 
                      "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_whileStmt = 2
    RULE_doWhileStmt = 3
    RULE_asignacion = 4
    RULE_breakStmt = 5
    RULE_continueStmt = 6
    RULE_condicion = 7
    RULE_expr = 8

    ruleNames =  [ "programa", "sentencia", "whileStmt", "doWhileStmt", 
                   "asignacion", "breakStmt", "continueStmt", "condicion", 
                   "expr" ]

    EOF = Token.EOF
    WHILE=1
    DO=2
    BREAK=3
    CONTINUE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    ASSIGN=9
    SEMI=10
    PLUS=11
    MINUS=12
    MUL=13
    DIV=14
    LT=15
    GT=16
    EQ=17
    NEQ=18
    ID=19
    INT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LoopLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LoopLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LoopLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LoopLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524318) != 0):
                self.state = 18
                self.sentencia()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(LoopLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def whileStmt(self):
            return self.getTypedRuleContext(LoopLangParser.WhileStmtContext,0)


        def doWhileStmt(self):
            return self.getTypedRuleContext(LoopLangParser.DoWhileStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(LoopLangParser.AsignacionContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(LoopLangParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(LoopLangParser.ContinueStmtContext,0)


        def getRuleIndex(self):
            return LoopLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = LoopLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.whileStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.doWhileStmt()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.asignacion()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.breakStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.continueStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LoopLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LoopLangParser.LPAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(LoopLangParser.CondicionContext,0)


        def RPAREN(self):
            return self.getToken(LoopLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(LoopLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LoopLangParser.RBRACE, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LoopLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LoopLangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = LoopLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(LoopLangParser.WHILE)
            self.state = 34
            self.match(LoopLangParser.LPAREN)
            self.state = 35
            self.condicion()
            self.state = 36
            self.match(LoopLangParser.RPAREN)
            self.state = 37
            self.match(LoopLangParser.LBRACE)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524318) != 0):
                self.state = 38
                self.sentencia()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(LoopLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(LoopLangParser.DO, 0)

        def LBRACE(self):
            return self.getToken(LoopLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LoopLangParser.RBRACE, 0)

        def WHILE(self):
            return self.getToken(LoopLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LoopLangParser.LPAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(LoopLangParser.CondicionContext,0)


        def RPAREN(self):
            return self.getToken(LoopLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(LoopLangParser.SEMI, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LoopLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LoopLangParser.RULE_doWhileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStmt" ):
                listener.enterDoWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStmt" ):
                listener.exitDoWhileStmt(self)




    def doWhileStmt(self):

        localctx = LoopLangParser.DoWhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_doWhileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(LoopLangParser.DO)
            self.state = 47
            self.match(LoopLangParser.LBRACE)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 524318) != 0):
                self.state = 48
                self.sentencia()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(LoopLangParser.RBRACE)
            self.state = 55
            self.match(LoopLangParser.WHILE)
            self.state = 56
            self.match(LoopLangParser.LPAREN)
            self.state = 57
            self.condicion()
            self.state = 58
            self.match(LoopLangParser.RPAREN)
            self.state = 59
            self.match(LoopLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LoopLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(LoopLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(LoopLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(LoopLangParser.SEMI, 0)

        def getRuleIndex(self):
            return LoopLangParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = LoopLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LoopLangParser.ID)
            self.state = 62
            self.match(LoopLangParser.ASSIGN)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(LoopLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(LoopLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(LoopLangParser.SEMI, 0)

        def getRuleIndex(self):
            return LoopLangParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)




    def breakStmt(self):

        localctx = LoopLangParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(LoopLangParser.BREAK)
            self.state = 67
            self.match(LoopLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(LoopLangParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(LoopLangParser.SEMI, 0)

        def getRuleIndex(self):
            return LoopLangParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)




    def continueStmt(self):

        localctx = LoopLangParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(LoopLangParser.CONTINUE)
            self.state = 70
            self.match(LoopLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LoopLangParser.ExprContext,i)


        def LT(self):
            return self.getToken(LoopLangParser.LT, 0)

        def GT(self):
            return self.getToken(LoopLangParser.GT, 0)

        def EQ(self):
            return self.getToken(LoopLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(LoopLangParser.NEQ, 0)

        def getRuleIndex(self):
            return LoopLangParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = LoopLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.expr(0)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0):
                self.state = 73
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 74
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LoopLangParser.INT, 0)

        def ID(self):
            return self.getToken(LoopLangParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LoopLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LoopLangParser.ExprContext,i)


        def PLUS(self):
            return self.getToken(LoopLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LoopLangParser.MINUS, 0)

        def MUL(self):
            return self.getToken(LoopLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(LoopLangParser.DIV, 0)

        def getRuleIndex(self):
            return LoopLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LoopLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 78
                self.match(LoopLangParser.INT)
                pass
            elif token in [19]:
                self.state = 79
                self.match(LoopLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LoopLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 82
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 83
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 84
                    self.expr(2) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




