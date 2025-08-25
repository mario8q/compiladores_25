# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#prog.
    def enterProg(self, ctx:CalculadoraParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#prog.
    def exitProg(self, ctx:CalculadoraParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#expresion.
    def enterExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expresion.
    def exitExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#sumares.
    def enterSumares(self, ctx:CalculadoraParser.SumaresContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#sumares.
    def exitSumares(self, ctx:CalculadoraParser.SumaresContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#mult.
    def enterMult(self, ctx:CalculadoraParser.MultContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#mult.
    def exitMult(self, ctx:CalculadoraParser.MultContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#potencia.
    def enterPotencia(self, ctx:CalculadoraParser.PotenciaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#potencia.
    def exitPotencia(self, ctx:CalculadoraParser.PotenciaContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#atomo.
    def enterAtomo(self, ctx:CalculadoraParser.AtomoContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#atomo.
    def exitAtomo(self, ctx:CalculadoraParser.AtomoContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#funcion.
    def enterFuncion(self, ctx:CalculadoraParser.FuncionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#funcion.
    def exitFuncion(self, ctx:CalculadoraParser.FuncionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#listaExpresiones.
    def enterListaExpresiones(self, ctx:CalculadoraParser.ListaExpresionesContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#listaExpresiones.
    def exitListaExpresiones(self, ctx:CalculadoraParser.ListaExpresionesContext):
        pass



del CalculadoraParser