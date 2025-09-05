grammar CombinationLang;

// Regla principal commando g4 -> antlr4 -Dlanguage=Python3 CombinationLang.g4
programa : sentencia+ EOF ; 

// Sentencias permitidas (asignacion, for statment, switch statement, if statement)
sentencia
    : asignacion SEMI
    | forStmt
    | switchStmt
    | ifStmt
    ;

// Asignaciones a variables
asignacion
    : ID ASSIGN (ID | INT)
    | ID ASSIGN (ID | INT) op=(MUL | DIV | PLUS | MINUS) (ID | INT)
    ;

// Reglas para for statement
forStmt 
    : FOR LPAREN asignacion SEMI condicion SEMI paso RPAREN LBRACE sentencia* RBRACE
    ;

condicion
    : ID op=(GT | LT | EQ | NEQ) (ID | INT)
    ;

paso
    : ID ASSIGN ID op=(MUL | DIV | PLUS | MINUS) (ID | INT)
    ;

// Reglas para el switch statement
switchStmt
    : SWITCH LPAREN ID RPAREN LBRACE (case | default)+ RBRACE
    ;

case
    : CASE INT COLON sentencia*
    ;

default
    : DEFAULT COLON sentencia*
    ;

// Reglas para el if statement
ifStmt
    : IF LPAREN condicion RPAREN LBRACE sentencia* RBRACE
    ;

// TOKENS
FOR     : 'for';
IF      : 'if';
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
COLON   : ':';
SEMI    : ';';
ASSIGN  : '=';
MUL     : '*';
DIV     : '/';
PLUS    : '+';
MINUS   : '-';
GT      : '>';
LT      : '<';
EQ      : '==';
NEQ     : '!=';

// Reglas lexicas
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ; 