grammar HLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+ EOF ; // write for program rule here using vardecl and funcdecl

vardecl: type vard SEMI;
vard: ID CM vard | ID;

funcdecl: type func body;
func: ID '(' param ')';
param: parameter (SEMI parameter)* | ;
parameter: type var;
var: ID CM var | ID;

body: '{' stmtlist '}';
stmtlist: stmt stmtlist |;
stmt: vardecl | ((returnstmt | assignstmt | callstmt) SEMI);

assignstmt: ID EQUAL expr;
callstmt: ID '(' paramcall ')';
paramcall: expr CM paramcall |expr;
returnstmt: RETURN expr;

expr: term ADD expr | term;
term: fact SUB fact | fact;
fact: fact MUL factor | fact DIV factor | factor;
factor: operand | '(' expr ')';

operand: INTLIT | FLOATLIT | ID | callstmt;

type: 'int' | 'float';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
INTLIT: DIGIT;
FLOATLIT: DIGIT '.' DIGIT;
DIGIT: [0-9]+;
CM: ',';
SEMI: ';';
EQUAL: '=';
RETURN: 'return';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;

