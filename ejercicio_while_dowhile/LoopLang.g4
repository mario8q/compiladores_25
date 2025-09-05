grammar LoopLang;

// Reglas principales
programa   : sentencia* EOF ;

sentencia
    : whileStmt
    | doWhileStmt
    | asignacion
    ;

whileStmt
    : WHILE LPAREN condicion RPAREN LBRACE sentencia* RBRACE
    ;

doWhileStmt
    : DO LBRACE sentencia* RBRACE WHILE LPAREN condicion RPAREN SEMI
    ;

asignacion
    : ID ASSIGN expr SEMI
    ;

// Reglas auxiliares
condicion
    : expr ( (LT | GT | EQ | NEQ) expr )?
    ;

expr
    : INT
    | ID
    | expr (PLUS|MINUS|MUL|DIV) expr
    ;

// Palabras clave
WHILE   : 'while' ;
DO      : 'do' ;

// Símbolos
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
ASSIGN  : '=' ;
SEMI    : ';' ;

PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;

LT      : '<' ;
GT      : '>' ;
EQ      : '==' ;
NEQ     : '!=' ;

// Tokens generales
ID      : [a-zA-Z_][a-zA-Z_0-9]* ;
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;

