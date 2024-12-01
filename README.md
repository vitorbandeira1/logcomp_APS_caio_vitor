# LogComp-APS - Submarinos

Este projeto apresenta uma linguagem de programação desenvolvida para o controle de submarinos. Inspirada na necessidade de simplificar a operação de veículos subaquáticos, a linguagem foi projetada para oferecer comandos intuitivos e eficientes, permitindo a execução de manobras e ajustes diretamente relacionados à navegação submersa. Com isso, busca-se facilitar o desenvolvimento de soluções voltadas para atividades exploratórias e operacionais no ambiente aquático.


## EBNF

PROGRAM = STATEMENT

BLOCK = "{" STATEMENT "}"

STATEMENT = ( λ | ASSIGNMENT | PRINT | VARIABLE | SUBMARINE_CONTROLLER | SUBMARINE_COMMANDS | IF | LOOP | COMMENT), "\n"

SUBMARINE_CONTROLLER = "submergir" | "emergir" | "ajustar_inclinacao"

SUBMARINE_COMMANDS = "ativar_propulsor", "(", INT, ")" 
                   | "ajustar_profundidade", "(", INT, ")" 
                   | "ajustar_posicao", "(", INT, ",", INT, ")"

VARIABLE = "var", IDENTIFIER, TYPE

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION

PRINT = ("Print" | "Println"), "(", PRINT_ARG, { ",", PRINT_ARG }, ")"
PRINT_ARG = EXPRESSION | STR

IF = "if", "(", BOOLEXP, ")", BLOCK, ("else", BLOCK)?

LOOP = "for", IDENTIFIER, "=", EXPRESSION, ";", BOOLEXP, ";", IDENTIFIER, "=", EXPRESSION, BLOCK

BOOLEXP = EXPRESSION, { ("<" | ">" | "==" | "&&" | "||"), EXPRESSION }

EXPRESSION = TERM, { ("+" | "-"), TERM }

TERM = FACTOR, { ("*" | "/"), FACTOR }

FACTOR = (("+" | "-"), FACTOR) | INT | "(", EXPRESSION, ")" | IDENTIFIER

TYPE = INT | STR

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" }

INT = DIGIT, { DIGIT }

STR = '"', { LETTER | DIGIT | SPACE | SYMBOL }, '"'

COMMENT = "//", { ANY_CHARACTER }, "\n"

RESERVED_WORDS = ("var" | "if" | "for" | "loop" | "Print" | "Println" | "submergir" | "emergir" | "ajustar_inclinacao" | "ativar_propulsor" | "ajustar_profundidade" | "ajustar_posicao")

LETTER = ( a | ... | z | A | ... | Z )

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 )
