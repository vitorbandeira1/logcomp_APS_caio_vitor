%{
#include "parser.tab.h"
#define YYDEBUG 1

%}

%option yylineno
%option noyywrap

%%
"submergir"                { return SUBMERGIR; }
"emergir"                  { return EMERGIR; }
"ajustar-inclinação"       { return AJUSTAR_INCLINACAO; }
"ativar-propulsor"         { return ATIVAR_PROPULSOR; }
"ajustar-profundidade"     { return AJUSTAR_PROFUNDIDADE; }
"ajustar-posição"          { return AJUSTAR_POSICAO; }
"var"                      { return VAR; }
"Print"                    { return PRINTLN; }
"if"                       { return IF; }
"else"                     { return ELSE; }
"for"                      { return LOOP; }
"int"                      { return INT; } // Deve ser reconhecido antes de IDEN
"string"                   { return STRING; }
\"[^\"]*\"                 { yylval.strValue = strdup(yytext + 1); yytext[yyleng - 1] = '\0'; return STRING_LITERAL; }
"<"                        { return LESS_THAN; }
">"                        { return GREATER_THAN; }
"=="                       { return DB_EQUAL; }
"="                        { return EQUAL; }
";"                        { return SEMICOLON; }
"+"                        { return PLUS; }
"-"                        { return MINUS; }
"*"                        { return MULTIPLY; }
"/"                        { return DIVIDE; }
"("                        { return LPAREN; }
")"                        { return RPAREN; }
","                        { return COMMA; }
"{"                        { return LBRACE; }
"}"                        { return RBRACE; }
"&&"                       { return AND; }
"//".*                     ;  // Ignorar comentários
[ \t]                      ;  // Ignorar espaços em branco
"\n"                       { return NEWLINE; }
[0-9]+                     { yylval.intValue = atoi(yytext); return INT; }
[a-zA-Z_][a-zA-Z0-9_]*     { return IDEN; }
[0-9]+:[0-9]+:[0-9]+	   { yylval.strValue = strdup(yytext); return TIME; }

%%