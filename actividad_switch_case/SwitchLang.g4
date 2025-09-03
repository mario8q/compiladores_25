grammar SwitchLang;

//Regla principal
programa: (sentencia SEMI)+ EOF ;

// Sentencias
sentencia
    : switchStmt
    | asignacion
    ;

// Regla para switch statement
switchStmt
    : (SWITCH LPAREN ID RPAREN LBRACE (sentencia SEMI?)* RBRACE)+
    ;

// Asignaciones entre braces del switch
asignacion
    : (CASE INT TPOINT ID ASSIGN INT SEMI)+ DEFAULT TPOINT ID ASSIGN INT
    ;

// TOKENS
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
ASSIGN  : '=';
TPOINT  : ':';
SEMI    : ';';

// Reglas lexicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Ignorar espacios en blanco