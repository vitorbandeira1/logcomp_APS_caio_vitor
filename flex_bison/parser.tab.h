/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_PARSER_TAB_H_INCLUDED
# define YY_YY_PARSER_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    SUBMERGIR = 258,               /* SUBMERGIR  */
    EMERGIR = 259,                 /* EMERGIR  */
    AJUSTAR_INCLINACAO = 260,      /* AJUSTAR_INCLINACAO  */
    ATIVAR_PROPULSOR = 261,        /* ATIVAR_PROPULSOR  */
    AJUSTAR_PROFUNDIDADE = 262,    /* AJUSTAR_PROFUNDIDADE  */
    AJUSTAR_POSICAO = 263,         /* AJUSTAR_POSICAO  */
    VAR = 264,                     /* VAR  */
    PRINTLN = 265,                 /* PRINTLN  */
    DB_EQUAL = 266,                /* DB_EQUAL  */
    OR = 267,                      /* OR  */
    IF = 268,                      /* IF  */
    ELSE = 269,                    /* ELSE  */
    AND = 270,                     /* AND  */
    LOOP = 271,                    /* LOOP  */
    STRING_LITERAL = 272,          /* STRING_LITERAL  */
    SEMICOLON = 273,               /* SEMICOLON  */
    LESS_THAN = 274,               /* LESS_THAN  */
    GREATER_THAN = 275,            /* GREATER_THAN  */
    EQUAL = 276,                   /* EQUAL  */
    PLUS = 277,                    /* PLUS  */
    MINUS = 278,                   /* MINUS  */
    MULTIPLY = 279,                /* MULTIPLY  */
    DIVIDE = 280,                  /* DIVIDE  */
    STRING = 281,                  /* STRING  */
    LPAREN = 282,                  /* LPAREN  */
    RPAREN = 283,                  /* RPAREN  */
    COMMA = 284,                   /* COMMA  */
    LBRACE = 285,                  /* LBRACE  */
    RBRACE = 286,                  /* RBRACE  */
    NEWLINE = 287,                 /* NEWLINE  */
    INT = 288,                     /* INT  */
    IDEN = 289,                    /* IDEN  */
    TIME = 290                     /* TIME  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 17 "parser.y"

        int intValue;
        char* strValue;

#line 104 "parser.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_PARSER_TAB_H_INCLUDED  */