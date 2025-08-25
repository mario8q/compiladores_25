# Generated from Calculadora.g4 by ANTLR 4.13.2
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
        4,1,11,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,25,8,2,10,2,12,2,28,
        9,2,1,3,1,3,1,3,5,3,33,8,3,10,3,12,3,36,9,3,1,4,1,4,1,4,3,4,41,8,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,51,8,5,1,6,1,6,1,6,4,6,56,
        8,6,11,6,12,6,57,1,6,1,6,1,7,1,7,1,7,5,7,65,8,7,10,7,12,7,68,9,7,
        1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,1,2,1,0,3,4,69,0,16,1,0,0,0,
        2,19,1,0,0,0,4,21,1,0,0,0,6,29,1,0,0,0,8,37,1,0,0,0,10,50,1,0,0,
        0,12,52,1,0,0,0,14,61,1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,18,1,1,
        0,0,0,19,20,3,4,2,0,20,3,1,0,0,0,21,26,3,6,3,0,22,23,7,0,0,0,23,
        25,3,6,3,0,24,22,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,
        0,27,5,1,0,0,0,28,26,1,0,0,0,29,34,3,8,4,0,30,31,7,1,0,0,31,33,3,
        8,4,0,32,30,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,
        7,1,0,0,0,36,34,1,0,0,0,37,40,3,10,5,0,38,39,5,5,0,0,39,41,3,8,4,
        0,40,38,1,0,0,0,40,41,1,0,0,0,41,9,1,0,0,0,42,43,5,6,0,0,43,44,3,
        2,1,0,44,45,5,7,0,0,45,51,1,0,0,0,46,51,5,9,0,0,47,51,3,12,6,0,48,
        49,5,2,0,0,49,51,3,10,5,0,50,42,1,0,0,0,50,46,1,0,0,0,50,47,1,0,
        0,0,50,48,1,0,0,0,51,11,1,0,0,0,52,53,5,11,0,0,53,55,5,6,0,0,54,
        56,3,14,7,0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,
        0,0,58,59,1,0,0,0,59,60,5,7,0,0,60,13,1,0,0,0,61,66,3,2,1,0,62,63,
        5,8,0,0,63,65,3,2,1,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,15,1,0,0,0,68,66,1,0,0,0,6,26,34,40,50,57,66
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", 
                     "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "WS", "FUNCID" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_sumares = 2
    RULE_mult = 3
    RULE_potencia = 4
    RULE_atomo = 5
    RULE_funcion = 6
    RULE_listaExpresiones = 7

    ruleNames =  [ "prog", "expresion", "sumares", "mult", "potencia", "atomo", 
                   "funcion", "listaExpresiones" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUMBER=9
    WS=10
    FUNCID=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.expresion()
            self.state = 17
            self.match(CalculadoraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sumares(self):
            return self.getTypedRuleContext(CalculadoraParser.SumaresContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.sumares()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumaresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.MultContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.MultContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_sumares

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumares" ):
                listener.enterSumares(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumares" ):
                listener.exitSumares(self)




    def sumares(self):

        localctx = CalculadoraParser.SumaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sumares)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.mult()
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 23
                    self.mult() 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def potencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.PotenciaContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.PotenciaContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_mult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMult" ):
                listener.enterMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMult" ):
                listener.exitMult(self)




    def mult(self):

        localctx = CalculadoraParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mult)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.potencia()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 31
                self.potencia()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomo(self):
            return self.getTypedRuleContext(CalculadoraParser.AtomoContext,0)


        def potencia(self):
            return self.getTypedRuleContext(CalculadoraParser.PotenciaContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_potencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)




    def potencia(self):

        localctx = CalculadoraParser.PotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_potencia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.atomo()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 38
                self.match(CalculadoraParser.T__4)
                self.state = 39
                self.potencia()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def funcion(self):
            return self.getTypedRuleContext(CalculadoraParser.FuncionContext,0)


        def atomo(self):
            return self.getTypedRuleContext(CalculadoraParser.AtomoContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_atomo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomo" ):
                listener.enterAtomo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomo" ):
                listener.exitAtomo(self)




    def atomo(self):

        localctx = CalculadoraParser.AtomoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atomo)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(CalculadoraParser.T__5)
                self.state = 43
                self.expresion()
                self.state = 44
                self.match(CalculadoraParser.T__6)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(CalculadoraParser.NUMBER)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.funcion()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(CalculadoraParser.T__1)
                self.state = 49
                self.atomo()
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


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCID(self):
            return self.getToken(CalculadoraParser.FUNCID, 0)

        def listaExpresiones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ListaExpresionesContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ListaExpresionesContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = CalculadoraParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(CalculadoraParser.FUNCID)
            self.state = 53
            self.match(CalculadoraParser.T__5)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.listaExpresiones()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2628) != 0)):
                    break

            self.state = 59
            self.match(CalculadoraParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExpresionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_listaExpresiones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpresiones" ):
                listener.enterListaExpresiones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpresiones" ):
                listener.exitListaExpresiones(self)




    def listaExpresiones(self):

        localctx = CalculadoraParser.ListaExpresionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listaExpresiones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.expresion()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 62
                self.match(CalculadoraParser.T__7)
                self.state = 63
                self.expresion()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





