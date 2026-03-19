grammar brainfuck;

program
    : statement* EOF
    ;

statement
    : command
    | loop
    ;

command
    : PLUS
    | MINUS
    | LSHIFT
    | RSHIFT
    | DOT
    | COMMA
    ;

loop
    : LBRACKET statement* RBRACKET
    ;

PLUS    : '+' ;
MINUS   : '-' ;
LSHIFT  : '<' ;
RSHIFT  : '>' ;
DOT     : '.' ;
COMMA   : ',' ;
LBRACKET: '[' ;
RBRACKET: ']' ;

COMMENT : ~[+\-<>.,[\]] -> skip ;
