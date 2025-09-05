grammar CombinationLangFunc;

// Regla principal
programa : (funcion | sentencia)+ EOF ;

// === FUNCIONES ===
funcion
    : FUNC ID LPAREN parametros? RPAREN LBRACE sentencia* RETURN expr SEMI RBRACE
    ;

// Parámetros separados por coma
parametros
    : ID (COMMA ID)*
    ;

// === SENTENCIAS ===
sentencia
    : asignacion SEMI
    | forStmt
    | switchStmt
    | ifStmt
    ;

// Asignaciones a variables
asignacion
    : ID ASSIGN expr
    ;

// Expresiones aritméticas simples
expr
    : expr (MUL | DIV | PLUS | MINUS) expr
    | ID
    | INT
    ;

// Reglas para for statement
forStmt 
    : FOR LPAREN asignacion SEMI condicion SEMI paso RPAREN 
      LBRACE sentencia* RBRACE
    ;

condicion
    : expr (GT | LT | EQ | NEQ) expr
    ;

paso
    : asignacion
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

// === TOKENS ===
FUNC    : 'func';
RETURN  : 'return';
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
COMMA   : ',';
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

// === LÉXICO ===
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ;
