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
    : SWITCH LPAREN ID RPAREN LBRACE (sentencia SEMI?)*
    ;

// Asignaciones entre braces del switch
asignacion
    : (case INT TPOINT ID ASSIGN INT SEMI)+ default TPOINT ID ASSIGN INT
    ;

// TOKENS
SWITCH  : 'switch';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
ASSIGN  : '=';
ASSIGN  : '=';
SEMI    : ';';

// Reglas lexicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Ignorar espacios en blanco