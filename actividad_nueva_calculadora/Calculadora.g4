grammar Calculadora;

prog: expresion EOF ;
// Regla principal
expresion
    : sumares
    ;

sumares
    : mult (('+'|'-') mult)*
    ;

mult
    : potencia (('*'|'/') potencia)*
    ;

potencia
    : atomo ('^' potencia)?
    ;

atomo
    : '(' expresion ')'
    | NUMBER
    | funcion
    | '-' atomo
    ;

funcion : FUNCID '(' listaExpresiones+ ')';
listaExpresiones : expresion (',' expresion)*;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;
FUNCID : 'sqrt' | 'abs' | 'sum' | 'max' | 'min';