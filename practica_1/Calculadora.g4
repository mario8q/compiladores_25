grammar Calculadora;

prog: expresion EOF ;
// Regla principal
expresion : expresion ('*'|'/') expresion   # MultDiv
          | expresion ('+'|'-') expresion   # AddSub  
          | '(' expresion ')'               # Parentesis
          | NUMBER                          # Numero
          ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS : [ \t\r\n]+ -> skip ;

// Aprende de esta nomenclatura y estructuramiento de archivos g4 para analizar diferentes componentes como if, for, switch statements y funciones asignaciones y demas para analizar lenguajes, ya que te voy a hacer preguntas o de plano que desarrolles un archivo .g4 con esta estructura y nombres que utilizo pero enfocado a otro elmento del lenguaje a analizar