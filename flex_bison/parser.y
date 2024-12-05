%{
#include <stdio.h>

extern int yylex();
void yyerror(const char *s);

#undef yywrap
#define yywrap() 0
%}

%debug

%token SUBMERGIR EMERGIR AJUSTAR_INCLINACAO ATIVAR_PROPULSOR AJUSTAR_PROFUNDIDADE AJUSTAR_POSICAO
%token VAR PRINTLN DB_EQUAL OR IF ELSE AND LOOP STRING_LITERAL SEMICOLON LESS_THAN GREATER_THAN EQUAL PLUS MINUS MULTIPLY DIVIDE STRING
%token LPAREN RPAREN COMMA LBRACE RBRACE NEWLINE INT IDEN TIME

%union {
        int intValue;
        char* strValue;
}

%start PROGRAM

%%

PROGRAM : STATEMENT
        | PROGRAM STATEMENT;
               
BLOCK : LBRACE NEWLINE STATEMENTS RBRACE;

STATEMENTS : STATEMENT
           | STATEMENTS STATEMENT;

STATEMENT : NEWLINE
          | ASSIGNMENT NEWLINE
          | PRINT NEWLINE
          | VARIABLE NEWLINE
          | SUBMARINE_CONTROLLER NEWLINE
          | SUBMARINE_COMMANDS NEWLINE
          | IF_STATEMENT NEWLINE
          | LOOP_STATEMENT NEWLINE;
                    
SUBMARINE_CONTROLLER : SUBMERGIR | EMERGIR | AJUSTAR_INCLINACAO;

SUBMARINE_COMMANDS : ATIVAR_PROPULSOR LPAREN INT RPAREN
                   | AJUSTAR_PROFUNDIDADE LPAREN INT RPAREN
                   | AJUSTAR_POSICAO COORDINATES;

VARIABLE : VAR IDEN
         | VAR IDEN TYPE;

ASSIGNMENT : IDEN EQUAL EXPRESSION;

PRINT : PRINTLN LPAREN EXPRESSION RPAREN;

IF_STATEMENT : IF BOOLEXP BLOCK
             | IF BOOLEXP BLOCK ELSE BLOCK;

LOOP_STATEMENT : LOOP IDEN EQUAL EXPRESSION SEMICOLON BOOLEXP SEMICOLON IDEN EQUAL EXPRESSION BLOCK;

BOOLEXP : BOOLTERM
        | BOOLTERM OR  BOOLEXP;

BOOLTERM : RELEXP
         | RELEXP AND BOOLTERM;
        
RELEXP : EXPRESSION
       | EXPRESSION RELOP EXPRESSION;

RELOP : GREATER_THAN | LESS_THAN | DB_EQUAL;

EXPRESSION : TERM
           | TERM PLUS EXPRESSION
           | TERM MINUS EXPRESSION;

TERM : FACTOR
     | FACTOR MULTIPLY TERM
     | FACTOR DIVIDE TERM;

FACTOR : PLUS FACTOR
       | MINUS FACTOR
       | INT
       | STRING_LITERAL
       | LPAREN EXPRESSION RPAREN
       | IDEN;

TYPE : INT | STRING | COORDINATES | TIME;

COORDINATES : LPAREN EXPRESSION COMMA EXPRESSION RPAREN;

%%

void yyerror(const char *s){
        extern int yylineno;
        extern char *yytext;

        printf("\n Erro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main(){
        yyparse();
        return 0;
}