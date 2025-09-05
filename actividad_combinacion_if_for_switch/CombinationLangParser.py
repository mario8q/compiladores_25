# Generated from CombinationLang.g4 by ANTLR 4.13.2
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
        4,1,23,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,56,8,3,10,
        3,12,3,59,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,80,8,6,11,6,12,6,81,1,6,1,6,1,7,1,
        7,1,7,1,7,5,7,90,8,7,10,7,12,7,93,9,7,1,8,1,8,1,8,5,8,98,8,8,10,
        8,12,8,101,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,109,8,9,10,9,12,9,112,
        9,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,21,22,1,
        0,13,16,1,0,17,20,116,0,21,1,0,0,0,2,33,1,0,0,0,4,43,1,0,0,0,6,45,
        1,0,0,0,8,62,1,0,0,0,10,66,1,0,0,0,12,72,1,0,0,0,14,85,1,0,0,0,16,
        94,1,0,0,0,18,102,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,
        0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,0,0,1,26,1,
        1,0,0,0,27,28,3,4,2,0,28,29,5,11,0,0,29,34,1,0,0,0,30,34,3,6,3,0,
        31,34,3,12,6,0,32,34,3,18,9,0,33,27,1,0,0,0,33,30,1,0,0,0,33,31,
        1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,5,21,0,0,36,37,5,12,0,0,
        37,44,7,0,0,0,38,39,5,21,0,0,39,40,5,12,0,0,40,41,7,0,0,0,41,42,
        7,1,0,0,42,44,7,0,0,0,43,35,1,0,0,0,43,38,1,0,0,0,44,5,1,0,0,0,45,
        46,5,1,0,0,46,47,5,6,0,0,47,48,3,4,2,0,48,49,5,11,0,0,49,50,3,8,
        4,0,50,51,5,11,0,0,51,52,3,10,5,0,52,53,5,7,0,0,53,57,5,8,0,0,54,
        56,3,2,1,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,
        0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,9,0,0,61,7,1,0,0,0,62,63,5,
        21,0,0,63,64,7,2,0,0,64,65,7,0,0,0,65,9,1,0,0,0,66,67,5,21,0,0,67,
        68,5,12,0,0,68,69,5,21,0,0,69,70,7,1,0,0,70,71,7,0,0,0,71,11,1,0,
        0,0,72,73,5,3,0,0,73,74,5,6,0,0,74,75,5,21,0,0,75,76,5,7,0,0,76,
        79,5,8,0,0,77,80,3,14,7,0,78,80,3,16,8,0,79,77,1,0,0,0,79,78,1,0,
        0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,
        5,9,0,0,84,13,1,0,0,0,85,86,5,4,0,0,86,87,5,22,0,0,87,91,5,10,0,
        0,88,90,3,2,1,0,89,88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,
        1,0,0,0,92,15,1,0,0,0,93,91,1,0,0,0,94,95,5,5,0,0,95,99,5,10,0,0,
        96,98,3,2,1,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,
        1,0,0,0,100,17,1,0,0,0,101,99,1,0,0,0,102,103,5,2,0,0,103,104,5,
        6,0,0,104,105,3,8,4,0,105,106,5,7,0,0,106,110,5,8,0,0,107,109,3,
        2,1,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,
        0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,5,9,0,0,114,19,1,0,
        0,0,9,23,33,43,57,79,81,91,99,110
    ]

class CombinationLangParser ( Parser ):

    grammarFileName = "CombinationLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'for'", "'if'", "'switch'", "'case'", 
                     "'default'", "'('", "')'", "'{'", "'}'", "':'", "';'", 
                     "'='", "'*'", "'/'", "'+'", "'-'", "'>'", "'<'", "'=='", 
                     "'!='" ]

    symbolicNames = [ "<INVALID>", "FOR", "IF", "SWITCH", "CASE", "DEFAULT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", 
                      "ASSIGN", "MUL", "DIV", "PLUS", "MINUS", "GT", "LT", 
                      "EQ", "NEQ", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_forStmt = 3
    RULE_condicion = 4
    RULE_paso = 5
    RULE_switchStmt = 6
    RULE_case = 7
    RULE_default = 8
    RULE_ifStmt = 9

    ruleNames =  [ "programa", "sentencia", "asignacion", "forStmt", "condicion", 
                   "paso", "switchStmt", "case", "default", "ifStmt" ]

    EOF = Token.EOF
    FOR=1
    IF=2
    SWITCH=3
    CASE=4
    DEFAULT=5
    LPAREN=6
    RPAREN=7
    LBRACE=8
    RBRACE=9
    COLON=10
    SEMI=11
    ASSIGN=12
    MUL=13
    DIV=14
    PLUS=15
    MINUS=16
    GT=17
    LT=18
    EQ=19
    NEQ=20
    ID=21
    INT=22
    WS=23

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
            return self.getToken(CombinationLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = CombinationLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.sentencia()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2097166) != 0)):
                    break

            self.state = 25
            self.match(CombinationLangParser.EOF)
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

        def asignacion(self):
            return self.getTypedRuleContext(CombinationLangParser.AsignacionContext,0)


        def SEMI(self):
            return self.getToken(CombinationLangParser.SEMI, 0)

        def forStmt(self):
            return self.getTypedRuleContext(CombinationLangParser.ForStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(CombinationLangParser.SwitchStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(CombinationLangParser.IfStmtContext,0)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = CombinationLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.asignacion()
                self.state = 28
                self.match(CombinationLangParser.SEMI)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.forStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.switchStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.ifStmt()
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CombinationLangParser.ID)
            else:
                return self.getToken(CombinationLangParser.ID, i)

        def ASSIGN(self):
            return self.getToken(CombinationLangParser.ASSIGN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(CombinationLangParser.INT)
            else:
                return self.getToken(CombinationLangParser.INT, i)

        def MUL(self):
            return self.getToken(CombinationLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(CombinationLangParser.DIV, 0)

        def PLUS(self):
            return self.getToken(CombinationLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CombinationLangParser.MINUS, 0)

        def getRuleIndex(self):
            return CombinationLangParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = CombinationLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(CombinationLangParser.ID)
                self.state = 36
                self.match(CombinationLangParser.ASSIGN)
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(CombinationLangParser.ID)
                self.state = 39
                self.match(CombinationLangParser.ASSIGN)
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 42
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


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
            return self.getToken(CombinationLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(CombinationLangParser.LPAREN, 0)

        def asignacion(self):
            return self.getTypedRuleContext(CombinationLangParser.AsignacionContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CombinationLangParser.SEMI)
            else:
                return self.getToken(CombinationLangParser.SEMI, i)

        def condicion(self):
            return self.getTypedRuleContext(CombinationLangParser.CondicionContext,0)


        def paso(self):
            return self.getTypedRuleContext(CombinationLangParser.PasoContext,0)


        def RPAREN(self):
            return self.getToken(CombinationLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CombinationLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CombinationLangParser.RBRACE, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = CombinationLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(CombinationLangParser.FOR)
            self.state = 46
            self.match(CombinationLangParser.LPAREN)
            self.state = 47
            self.asignacion()
            self.state = 48
            self.match(CombinationLangParser.SEMI)
            self.state = 49
            self.condicion()
            self.state = 50
            self.match(CombinationLangParser.SEMI)
            self.state = 51
            self.paso()
            self.state = 52
            self.match(CombinationLangParser.RPAREN)
            self.state = 53
            self.match(CombinationLangParser.LBRACE)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097166) != 0):
                self.state = 54
                self.sentencia()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(CombinationLangParser.RBRACE)
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
                return self.getTokens(CombinationLangParser.ID)
            else:
                return self.getToken(CombinationLangParser.ID, i)

        def INT(self):
            return self.getToken(CombinationLangParser.INT, 0)

        def GT(self):
            return self.getToken(CombinationLangParser.GT, 0)

        def LT(self):
            return self.getToken(CombinationLangParser.LT, 0)

        def EQ(self):
            return self.getToken(CombinationLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CombinationLangParser.NEQ, 0)

        def getRuleIndex(self):
            return CombinationLangParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = CombinationLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(CombinationLangParser.ID)
            self.state = 63
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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
                return self.getTokens(CombinationLangParser.ID)
            else:
                return self.getToken(CombinationLangParser.ID, i)

        def ASSIGN(self):
            return self.getToken(CombinationLangParser.ASSIGN, 0)

        def INT(self):
            return self.getToken(CombinationLangParser.INT, 0)

        def MUL(self):
            return self.getToken(CombinationLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(CombinationLangParser.DIV, 0)

        def PLUS(self):
            return self.getToken(CombinationLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CombinationLangParser.MINUS, 0)

        def getRuleIndex(self):
            return CombinationLangParser.RULE_paso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPaso" ):
                listener.enterPaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPaso" ):
                listener.exitPaso(self)




    def paso(self):

        localctx = CombinationLangParser.PasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paso)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(CombinationLangParser.ID)
            self.state = 67
            self.match(CombinationLangParser.ASSIGN)
            self.state = 68
            self.match(CombinationLangParser.ID)
            self.state = 69
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
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


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(CombinationLangParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(CombinationLangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(CombinationLangParser.ID, 0)

        def RPAREN(self):
            return self.getToken(CombinationLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CombinationLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CombinationLangParser.RBRACE, 0)

        def case(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.CaseContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.CaseContext,i)


        def default(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.DefaultContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.DefaultContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_switchStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStmt" ):
                listener.enterSwitchStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStmt" ):
                listener.exitSwitchStmt(self)




    def switchStmt(self):

        localctx = CombinationLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CombinationLangParser.SWITCH)
            self.state = 73
            self.match(CombinationLangParser.LPAREN)
            self.state = 74
            self.match(CombinationLangParser.ID)
            self.state = 75
            self.match(CombinationLangParser.RPAREN)
            self.state = 76
            self.match(CombinationLangParser.LBRACE)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 77
                    self.case()
                    pass
                elif token in [5]:
                    self.state = 78
                    self.default()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4 or _la==5):
                    break

            self.state = 83
            self.match(CombinationLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(CombinationLangParser.CASE, 0)

        def INT(self):
            return self.getToken(CombinationLangParser.INT, 0)

        def COLON(self):
            return self.getToken(CombinationLangParser.COLON, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase" ):
                listener.enterCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase" ):
                listener.exitCase(self)




    def case(self):

        localctx = CombinationLangParser.CaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_case)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CombinationLangParser.CASE)
            self.state = 86
            self.match(CombinationLangParser.INT)
            self.state = 87
            self.match(CombinationLangParser.COLON)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097166) != 0):
                self.state = 88
                self.sentencia()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(CombinationLangParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(CombinationLangParser.COLON, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_default

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault" ):
                listener.enterDefault(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault" ):
                listener.exitDefault(self)




    def default(self):

        localctx = CombinationLangParser.DefaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_default)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(CombinationLangParser.DEFAULT)
            self.state = 95
            self.match(CombinationLangParser.COLON)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097166) != 0):
                self.state = 96
                self.sentencia()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CombinationLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(CombinationLangParser.LPAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(CombinationLangParser.CondicionContext,0)


        def RPAREN(self):
            return self.getToken(CombinationLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CombinationLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CombinationLangParser.RBRACE, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CombinationLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CombinationLangParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CombinationLangParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = CombinationLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(CombinationLangParser.IF)
            self.state = 103
            self.match(CombinationLangParser.LPAREN)
            self.state = 104
            self.condicion()
            self.state = 105
            self.match(CombinationLangParser.RPAREN)
            self.state = 106
            self.match(CombinationLangParser.LBRACE)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2097166) != 0):
                self.state = 107
                self.sentencia()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(CombinationLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





