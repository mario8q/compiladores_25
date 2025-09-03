# Generated from ForLang.g4 by ANTLR 4.13.2
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
        4,1,18,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,5,2,37,8,2,10,2,12,2,40,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,66,8,5,1,5,0,0,6,0,2,4,6,8,
        10,0,4,1,0,16,17,1,0,11,14,1,0,9,10,1,0,7,8,67,0,13,1,0,0,0,2,21,
        1,0,0,0,4,23,1,0,0,0,6,43,1,0,0,0,8,47,1,0,0,0,10,65,1,0,0,0,12,
        14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,
        0,16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,22,3,4,2,0,20,22,3,
        10,5,0,21,19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,5,1,0,0,24,
        25,5,2,0,0,25,26,3,6,3,0,26,27,5,15,0,0,27,28,3,8,4,0,28,29,5,15,
        0,0,29,30,3,10,5,0,30,31,5,3,0,0,31,38,5,4,0,0,32,34,3,10,5,0,33,
        35,5,15,0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,32,1,0,
        0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,
        1,0,0,0,41,42,5,5,0,0,42,5,1,0,0,0,43,44,5,16,0,0,44,45,5,6,0,0,
        45,46,7,0,0,0,46,7,1,0,0,0,47,48,5,16,0,0,48,49,7,1,0,0,49,50,7,
        0,0,0,50,9,1,0,0,0,51,52,5,16,0,0,52,53,5,6,0,0,53,54,5,16,0,0,54,
        55,7,2,0,0,55,66,7,0,0,0,56,57,5,16,0,0,57,58,5,6,0,0,58,59,5,16,
        0,0,59,60,7,3,0,0,60,66,7,0,0,0,61,62,5,2,0,0,62,63,3,10,5,0,63,
        64,5,3,0,0,64,66,1,0,0,0,65,51,1,0,0,0,65,56,1,0,0,0,65,61,1,0,0,
        0,66,11,1,0,0,0,5,15,21,34,38,65
    ]

class ForLangParser ( Parser ):

    grammarFileName = "ForLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'for'", "'('", "')'", "'{'", "'}'", "'='", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "FOR", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "NEQ", "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forStmt = 2
    RULE_indice = 3
    RULE_condicion = 4
    RULE_paso = 5

    ruleNames =  [ "programa", "sentencia", "forStmt", "indice", "condicion", 
                   "paso" ]

    EOF = Token.EOF
    FOR=1
    LPAREN=2
    RPAREN=3
    LBRACE=4
    RBRACE=5
    ASSIGN=6
    PLUS=7
    MINUS=8
    MUL=9
    DIV=10
    GT=11
    LT=12
    EQ=13
    NEQ=14
    SEMI=15
    ID=16
    INT=17
    WS=18

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
            return self.getToken(ForLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ForLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return ForLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ForLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.sentencia()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 65542) != 0)):
                    break

            self.state = 17
            self.match(ForLangParser.EOF)
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

        def forStmt(self):
            return self.getTypedRuleContext(ForLangParser.ForStmtContext,0)


        def paso(self):
            return self.getTypedRuleContext(ForLangParser.PasoContext,0)


        def getRuleIndex(self):
            return ForLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = ForLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.forStmt()
                pass
            elif token in [2, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.paso()
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


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ForLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(ForLangParser.LPAREN, 0)

        def indice(self):
            return self.getTypedRuleContext(ForLangParser.IndiceContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.SEMI)
            else:
                return self.getToken(ForLangParser.SEMI, i)

        def condicion(self):
            return self.getTypedRuleContext(ForLangParser.CondicionContext,0)


        def paso(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.PasoContext)
            else:
                return self.getTypedRuleContext(ForLangParser.PasoContext,i)


        def RPAREN(self):
            return self.getToken(ForLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(ForLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ForLangParser.RBRACE, 0)

        def getRuleIndex(self):
            return ForLangParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = ForLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ForLangParser.FOR)
            self.state = 24
            self.match(ForLangParser.LPAREN)
            self.state = 25
            self.indice()
            self.state = 26
            self.match(ForLangParser.SEMI)
            self.state = 27
            self.condicion()
            self.state = 28
            self.match(ForLangParser.SEMI)
            self.state = 29
            self.paso()
            self.state = 30
            self.match(ForLangParser.RPAREN)
            self.state = 31
            self.match(ForLangParser.LBRACE)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==16:
                self.state = 32
                self.paso()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 33
                    self.match(ForLangParser.SEMI)


                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(ForLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.ID)
            else:
                return self.getToken(ForLangParser.ID, i)

        def ASSIGN(self):
            return self.getToken(ForLangParser.ASSIGN, 0)

        def INT(self):
            return self.getToken(ForLangParser.INT, 0)

        def getRuleIndex(self):
            return ForLangParser.RULE_indice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndice" ):
                listener.enterIndice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndice" ):
                listener.exitIndice(self)




    def indice(self):

        localctx = ForLangParser.IndiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_indice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ForLangParser.ID)
            self.state = 44
            self.match(ForLangParser.ASSIGN)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.op = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.ID)
            else:
                return self.getToken(ForLangParser.ID, i)

        def INT(self):
            return self.getToken(ForLangParser.INT, 0)

        def GT(self):
            return self.getToken(ForLangParser.GT, 0)

        def LT(self):
            return self.getToken(ForLangParser.LT, 0)

        def EQ(self):
            return self.getToken(ForLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ForLangParser.NEQ, 0)

        def getRuleIndex(self):
            return ForLangParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = ForLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ForLangParser.ID)
            self.state = 48
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.ID)
            else:
                return self.getToken(ForLangParser.ID, i)

        def ASSIGN(self):
            return self.getToken(ForLangParser.ASSIGN, 0)

        def INT(self):
            return self.getToken(ForLangParser.INT, 0)

        def MUL(self):
            return self.getToken(ForLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(ForLangParser.DIV, 0)

        def PLUS(self):
            return self.getToken(ForLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ForLangParser.MINUS, 0)

        def LPAREN(self):
            return self.getToken(ForLangParser.LPAREN, 0)

        def paso(self):
            return self.getTypedRuleContext(ForLangParser.PasoContext,0)


        def RPAREN(self):
            return self.getToken(ForLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return ForLangParser.RULE_paso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaso" ):
                listener.enterPaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaso" ):
                listener.exitPaso(self)




    def paso(self):

        localctx = ForLangParser.PasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paso)
        self._la = 0 # Token type
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(ForLangParser.ID)
                self.state = 52
                self.match(ForLangParser.ASSIGN)
                self.state = 53
                self.match(ForLangParser.ID)
                self.state = 54
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(ForLangParser.ID)
                self.state = 57
                self.match(ForLangParser.ASSIGN)
                self.state = 58
                self.match(ForLangParser.ID)
                self.state = 59
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 60
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(ForLangParser.LPAREN)
                self.state = 62
                self.paso()
                self.state = 63
                self.match(ForLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





