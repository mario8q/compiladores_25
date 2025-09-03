# Generated from SwitchLang.g4 by ANTLR 4.13.2
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
        4,1,13,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,29,8,2,5,2,31,8,2,10,2,12,2,34,9,2,1,2,4,2,37,8,2,11,2,12,
        2,38,1,3,1,3,1,3,1,3,1,3,1,3,1,3,4,3,48,8,3,11,3,12,3,49,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,59,0,11,1,0,0,0,2,19,1,0,0,
        0,4,36,1,0,0,0,6,47,1,0,0,0,8,9,3,2,1,0,9,10,5,10,0,0,10,12,1,0,
        0,0,11,8,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,15,
        1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,20,3,4,2,0,18,20,3,6,3,0,19,
        17,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,21,22,5,1,0,0,22,23,5,4,0,
        0,23,24,5,11,0,0,24,25,5,5,0,0,25,32,5,6,0,0,26,28,3,2,1,0,27,29,
        5,10,0,0,28,27,1,0,0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,26,1,0,0,0,
        31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,
        0,0,0,35,37,5,7,0,0,36,21,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,
        39,1,0,0,0,39,5,1,0,0,0,40,41,5,2,0,0,41,42,5,12,0,0,42,43,5,9,0,
        0,43,44,5,11,0,0,44,45,5,8,0,0,45,46,5,12,0,0,46,48,5,10,0,0,47,
        40,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,
        0,51,52,5,3,0,0,52,53,5,9,0,0,53,54,5,11,0,0,54,55,5,8,0,0,55,56,
        5,12,0,0,56,7,1,0,0,0,6,13,19,28,32,38,49
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "'default'", "'('", 
                     "')'", "'{'", "'}'", "'='", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "SWITCH", "CASE", "DEFAULT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "ASSIGN", "TPOINT", 
                      "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_switchStmt = 2
    RULE_asignacion = 3

    ruleNames =  [ "programa", "sentencia", "switchStmt", "asignacion" ]

    EOF = Token.EOF
    SWITCH=1
    CASE=2
    DEFAULT=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    ASSIGN=8
    TPOINT=9
    SEMI=10
    ID=11
    INT=12
    WS=13

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
            return self.getToken(SwitchLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = SwitchLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.sentencia()
                self.state = 9
                self.match(SwitchLangParser.SEMI)
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 15
            self.match(SwitchLangParser.EOF)
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

        def switchStmt(self):
            return self.getTypedRuleContext(SwitchLangParser.SwitchStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(SwitchLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = SwitchLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.switchStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
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


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SWITCH)
            else:
                return self.getToken(SwitchLangParser.SWITCH, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.LPAREN)
            else:
                return self.getToken(SwitchLangParser.LPAREN, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.ID)
            else:
                return self.getToken(SwitchLangParser.ID, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.RPAREN)
            else:
                return self.getToken(SwitchLangParser.RPAREN, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.LBRACE)
            else:
                return self.getToken(SwitchLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.RBRACE)
            else:
                return self.getToken(SwitchLangParser.RBRACE, i)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = SwitchLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 21
                    self.match(SwitchLangParser.SWITCH)
                    self.state = 22
                    self.match(SwitchLangParser.LPAREN)
                    self.state = 23
                    self.match(SwitchLangParser.ID)
                    self.state = 24
                    self.match(SwitchLangParser.RPAREN)
                    self.state = 25
                    self.match(SwitchLangParser.LBRACE)
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1 or _la==2:
                        self.state = 26
                        self.sentencia()
                        self.state = 28
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==10:
                            self.state = 27
                            self.match(SwitchLangParser.SEMI)


                        self.state = 34
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 35
                    self.match(SwitchLangParser.RBRACE)

                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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

        def DEFAULT(self):
            return self.getToken(SwitchLangParser.DEFAULT, 0)

        def TPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.TPOINT)
            else:
                return self.getToken(SwitchLangParser.TPOINT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.ID)
            else:
                return self.getToken(SwitchLangParser.ID, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.ASSIGN)
            else:
                return self.getToken(SwitchLangParser.ASSIGN, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.INT)
            else:
                return self.getToken(SwitchLangParser.INT, i)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.CASE)
            else:
                return self.getToken(SwitchLangParser.CASE, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = SwitchLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(SwitchLangParser.CASE)
                self.state = 41
                self.match(SwitchLangParser.INT)
                self.state = 42
                self.match(SwitchLangParser.TPOINT)
                self.state = 43
                self.match(SwitchLangParser.ID)
                self.state = 44
                self.match(SwitchLangParser.ASSIGN)
                self.state = 45
                self.match(SwitchLangParser.INT)
                self.state = 46
                self.match(SwitchLangParser.SEMI)
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 51
            self.match(SwitchLangParser.DEFAULT)
            self.state = 52
            self.match(SwitchLangParser.TPOINT)
            self.state = 53
            self.match(SwitchLangParser.ID)
            self.state = 54
            self.match(SwitchLangParser.ASSIGN)
            self.state = 55
            self.match(SwitchLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





