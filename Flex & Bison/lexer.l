%{
#include "parser.tab.h"
%}

%option noyywrap

%%
"submergir"                { return SUBMERGIR; }
"emergir"                  { return EMERGIR; }
"ajustar-inclinação"       { return AJUSTAR_INCLINACAO; }
"ativar-propulsor"         { return ATIVAR_PROPULSOR; }
"ajustar-profundidade"     { return AJUSTAR_PROFUNDIDADE; }
"ajustar-posição"          { return AJUSTAR_POSICAO; }
"var"                      { return VAR; }
"Println"                  { return PRINTLN; }
"if"                       { return IF; }
"else"                     { return ELSE; }
"loop"                     { return LOOP; }
"int"                      { return INT; } // Deve ser reconhecido antes de IDEN
"<"                        { return LESS_THAN; }
">"                        { return GREATER_THAN; }
"=="                       { return EQUAL; }
"+"                        { return PLUS; }
"-"                        { return MINUS; }
"*"                        { return MULTIPLY; }
"/"                        { return DIVIDE; }
"("                        { return LPAREN; }
")"                        { return RPAREN; }
","                        { return COMMA; }
"{"                        { return LBRACE; }
"}"                        { return RBRACE; }
"//".*                     ;  // Ignorar comentários
[ \t]                      ;  // Ignorar espaços em branco
"\n"                       { return NEWLINE; }
[0-9]+                   { yylval.intValue = atoi(yytext); return INT; }
[a-zA-Z_][a-zA-Z0-9_]*     { yylval.strValue = strdup(yytext); return IDEN; }
[0-9]+:[0-9]+:[0-9]+		{ yylval.strValue = strdup(yytext); return TIME;}
%%
