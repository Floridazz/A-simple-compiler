// 2153148
//Phan Quốc An
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

ignore: NEWL+;
T: 'true'; 
F: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
BY: 'by';
UNTIL: 'until';
BR: 'break';
CONT: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// TODO Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
GOE: '>=';
LOE: '<=';
ASSIGN: '<-';
NEQ: '!=';
LT: '<';
GT: '>';
CONCAT: '...';
CMP: '==';
EQ: '=';
REL_OP: CMP | NEQ | LOE | GOE | LT | GT | EQ;

// TODO Separators
LB: '(';
RB: ')';
SLB: '[';
SRB: ']';
CM: ',';

// TODO ID
ID: [a-zA-Z_][a-zA-Z_0-9]*;
// TODO lit 

NUM_LIT: Int Dec? Expo?;

BOOL_LIT: T | F;

//FRAGMENT
fragment Digit: [0-9];
fragment Int: Digit+;
fragment Dec: '.'Digit*;
fragment Expo: [Ee][+-]?Digit+;

STRING_LIT: '"' (~[\r\n\\"] | '\\' [bfrnt'\\] | [']["])* '"'{self.text = self.text[1:-1];};


NEWL: [\n]; // 
CMT: '##' ~[\n\r]* ->skip; 
WS : [ \t\r\f\b]+ -> skip ;
fragment YES: (~[\r\n\\"] | '\\' [bfrnt'\\] | '\'"' );
fragment NO: [\r] | '\\' ~[bfrnt'\\];


// TODO ERROR
UNCLOSE_STRING: '"' YES* (EOF | '\r\n' | '\n')
{
	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' YES* NO
{
	raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: . {raise ErrorToken(self.text)};
//!  -------------------------- end Lexical structure ------------------- //



//Program
program: NEWL* list_decl EOF;
decl: func | varis ignore;
list_decl:  decl list_decl |  decl;

//TODO decl variable
varis: implicit_var | keyword_var | implicit_dynamic; 
implicit_var: VAR ID ASSIGN exp;
keyword_var:  (BOOL|NUMBER|STRING) ID (SLB list_NUMBER_LIT SRB )?(ASSIGN exp)? ignore?;
implicit_dynamic: DYNAMIC ID (ASSIGN exp)?;

//TODO decl func
func: FUNC ID LB param_list RB  (ignore? return_stmt | ignore? block_stmt | ignore);
param_list: paraprime | ;
paraprime: param CM paraprime | param;
param: (NUMBER|BOOL|STRING) ID (SLB list_NUMBER_LIT SRB)?;

//TODO exp
list_expr: exp list_expr_tail | exp;
list_expr_tail: CM exp list_expr_tail | ;
exp: exp1 CONCAT exp1 | exp1;
exp1: exp2 (CMP | NEQ | LOE | GOE | LT | GT | EQ) exp2 | exp2;
exp2: exp2 AND exp3 | exp2 OR exp3 | exp3;
exp3: exp3 ADD exp4 | exp3 SUB exp4 | exp4;
exp4: exp4 MUL exp5 | exp4 DIV exp5 | exp4 MOD exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: (ID | func_call) SLB list_expr SRB | exp8;
exp8: func_call | ID | lit | LB exp RB;

func_call: ID LB nullable_list_expr RB;

nullable_list_expr: exp nullable_list_expr_tail | ;
nullable_list_expr_tail: CM exp nullable_list_expr_tail | ;

//TODO Value
lit: NUM_LIT | STRING_LIT | arr_lit | T | F;
arr_lit: SLB list_expr SRB;
list_lit: lit CM list_lit | lit;

list_NUMBER_LIT: NUM_LIT list_NUMBER_tail | NUM_LIT;
list_NUMBER_tail: CM NUM_LIT list_NUMBER_tail | ;


//TODO  stmts
stmt_list: stmt stmt_list | ; 
stmt: (decl_stmt | assign_stmt | return_stmt  | call_stmt | block_stmt| if_stmt | for_stmt | break_stmt | cont_stmt);
decl_stmt: varis ignore;
assign_stmt : lhs ASSIGN exp ignore;
return_stmt: RETURN exp? ignore;
call_stmt: ID LB nullable_list_expr RB ignore;
block_stmt: BEGIN ignore stmt_list END ignore;
if_stmt: IF LB exp RB ignore? stmt elif_list (ELSE ignore? stmt )?;
elif_list:ELIF LB exp RB ignore? stmt elif_list | ;
for_stmt: FOR ID UNTIL exp 
BY exp ignore? stmt ignore?;
break_stmt: BR ignore;
cont_stmt: CONT ignore;
lhs: ID (SLB list_expr SRB)?;

