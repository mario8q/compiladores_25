grammar ForLang;

// Regla principal: permite for y un "paso" 
programa: (sentencia)+ EOF ;

// Sentencias permitidas (for y paso)
sentencia
    : forStmt  
    | paso  
    ;

// Regla para for statement
forStmt
    : FOR LPAREN indice SEMI condicion SEMI paso RPAREN LBRACE (paso SEMI?)* RBRACE 
    ;

// Aumento de indice para el for
indice
    : ID ASSIGN (ID | INT) 
    ;

// Condiciones dentro del for
condicion
    : ID op=(GT | LT | EQ | NEQ) (ID | INT)  
    ;

// Pasos del ciclo for
paso
    : ID ASSIGN ID op=(MUL | DIV) (ID | INT)
    | ID ASSIGN ID op=(PLUS | MINUS) (ID | INT)
    | LPAREN paso RPAREN 
    ;

// === TOKENS ===
FOR    : 'for';
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
ASSIGN : '=' ;
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
GT     : '>' ;
LT     : '<' ;
EQ     : '==' ;
NEQ    : '!=' ;
SEMI   : ';' ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Ignorar espacios en blanco