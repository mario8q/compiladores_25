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
        4,1,19,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,3,
        1,3,1,3,5,3,44,8,3,10,3,12,3,47,9,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,3,6,69,8,
        6,1,6,1,6,1,6,5,6,74,8,6,10,6,12,6,77,9,6,1,6,0,1,12,7,0,2,4,6,8,
        10,12,0,2,1,0,13,16,1,0,9,12,79,0,17,1,0,0,0,2,25,1,0,0,0,4,27,1,
        0,0,0,6,40,1,0,0,0,8,55,1,0,0,0,10,60,1,0,0,0,12,68,1,0,0,0,14,16,
        3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,26,3,4,
        2,0,23,26,3,6,3,0,24,26,3,8,4,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,
        1,0,0,0,26,3,1,0,0,0,27,28,5,1,0,0,28,29,5,3,0,0,29,30,3,10,5,0,
        30,31,5,4,0,0,31,35,5,5,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,
        0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,
        39,5,6,0,0,39,5,1,0,0,0,40,41,5,2,0,0,41,45,5,5,0,0,42,44,3,2,1,
        0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,5,6,0,0,49,50,5,1,0,0,50,51,5,3,0,0,
        51,52,3,10,5,0,52,53,5,4,0,0,53,54,5,8,0,0,54,7,1,0,0,0,55,56,5,
        17,0,0,56,57,5,7,0,0,57,58,3,12,6,0,58,59,5,8,0,0,59,9,1,0,0,0,60,
        63,3,12,6,0,61,62,7,0,0,0,62,64,3,12,6,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,11,1,0,0,0,65,66,6,6,-1,0,66,69,5,18,0,0,67,69,5,17,0,0,68,
        65,1,0,0,0,68,67,1,0,0,0,69,75,1,0,0,0,70,71,10,1,0,0,71,72,7,1,
        0,0,72,74,3,12,6,2,73,70,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,
        76,1,0,0,0,76,13,1,0,0,0,77,75,1,0,0,0,7,17,25,35,45,63,68,75
    ]

class LoopLangParser ( Parser ):

    grammarFileName = "LoopLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'while'", "'do'", "'('", "')'", "'{'", 
                     "'}'", "'='", "';'", "'+'", "'-'", "'*'", "'/'", "'<'", 
                     "'>'", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "WHILE", "DO", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ASSIGN", "SEMI", "PLUS", "MINUS", "MUL", 
                      "DIV", "LT", "GT", "EQ", "NEQ", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_whileStmt = 2
    RULE_doWhileStmt = 3
    RULE_asignacion = 4
    RULE_condicion = 5
    RULE_expr = 6

    ruleNames =  [ "programa", "sentencia", "whileStmt", "doWhileStmt", 
                   "asignacion", "condicion", "expr" ]

    EOF = Token.EOF
    WHILE=1
    DO=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    ASSIGN=7
    SEMI=8
    PLUS=9
    MINUS=10
    MUL=11
    DIV=12
    LT=13
    GT=14
    EQ=15
    NEQ=16
    ID=17
    INT=18
    WS=19

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131078) != 0):
                self.state = 14
                self.sentencia()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.whileStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.doWhileStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.asignacion()
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
            self.state = 27
            self.match(LoopLangParser.WHILE)
            self.state = 28
            self.match(LoopLangParser.LPAREN)
            self.state = 29
            self.condicion()
            self.state = 30
            self.match(LoopLangParser.RPAREN)
            self.state = 31
            self.match(LoopLangParser.LBRACE)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131078) != 0):
                self.state = 32
                self.sentencia()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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
            self.state = 40
            self.match(LoopLangParser.DO)
            self.state = 41
            self.match(LoopLangParser.LBRACE)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 131078) != 0):
                self.state = 42
                self.sentencia()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(LoopLangParser.RBRACE)
            self.state = 49
            self.match(LoopLangParser.WHILE)
            self.state = 50
            self.match(LoopLangParser.LPAREN)
            self.state = 51
            self.condicion()
            self.state = 52
            self.match(LoopLangParser.RPAREN)
            self.state = 53
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
            self.state = 55
            self.match(LoopLangParser.ID)
            self.state = 56
            self.match(LoopLangParser.ASSIGN)
            self.state = 57
            self.expr(0)
            self.state = 58
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
        self.enterRule(localctx, 10, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.expr(0)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0):
                self.state = 61
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.state = 66
                self.match(LoopLangParser.INT)
                pass
            elif token in [17]:
                self.state = 67
                self.match(LoopLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LoopLangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 70
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 71
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 72
                    self.expr(2) 
                self.state = 77
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
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




