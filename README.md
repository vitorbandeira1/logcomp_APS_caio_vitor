# LogComp-APS - Submarinos

## Sobre a linguagem desenvolvida

Este projeto apresenta uma linguagem de programação desenvolvida para o controle de submarinos. Inspirada na necessidade de simplificar a operação de veículos subaquáticos, a linguagem foi projetada para oferecer comandos intuitivos e eficientes, permitindo a execução de manobras e ajustes diretamente relacionados à navegação submersa. Com isso, busca-se facilitar o desenvolvimento de soluções voltadas para atividades exploratórias e operacionais no ambiente aquático.


## EBNF da linguagem

```ebnf
PROGRAM = STATEMENT ;
BLOCK = "{" STATEMENT "}" ;
STATEMENT = ( λ | ASSIGNMENT | PRINT | VARIABLE | SUBMARINE_CONTROLLER | SUBMARINE_COMMANDS | IF | LOOP | COMMENT), "\n" ;
SUBMARINE_CONTROLLER = "submergir" | "emergir" | "ajustar_inclinacao" ;
SUBMARINE_COMMANDS = ("ativar_propulsor", "(", INT, ")") | ("ajustar_profundidade", "(", INT, ")") | ("ajustar_posicao", "(", INT, ",", INT, ")") ;
VARIABLE = "var", IDENTIFIER, TYPE ;
ASSIGNMENT = IDENTIFIER, "=", EXPRESSION ;
PRINT = "Println", "(", PRINT_ARG, { ",", PRINT_ARG }, ")" ;
PRINT_ARG = EXPRESSION | STR ;
IF = "if", BOOLEXP, BLOCK, ["else", BLOCK] ;
LOOP = "for", IDENTIFIER, "=", EXPRESSION, ";", BOOLEXP, ";", IDENTIFIER, "=", EXPRESSION, BLOCK ;
BOOLEXP = EXPRESSION, { ("<" | ">" | "==" | "&&" | "||"), EXPRESSION } ;
EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"), FACTOR) | INT | "(", EXPRESSION, ")" | IDENTIFIER ;
TYPE = INT | STR ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
INT = DIGIT, { DIGIT } ;
STR = '"', { LETTER | DIGIT | SPACE | SYMBOL }, '"' ;
COMMENT = "//", { ANY_CHARACTER }, "\n" ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
SPACE = " " ;
SYMBOL = ( ! | ... | ?) ;
```

## Exemplo

```
var ang int
var x int
var y int

var a string
var b string
var c string

a = "A inclinação final foi: "
b = "A coordenada x final foi: "
c = "A coordenada y final foi: "

x = 6
y = 3

ativar_propulsor(30)
submergir

for ang = 90; ang < 100; ang = ang + 1 {
	Println(ang)
}

ajustar_inclinacao
ang = 90

if x == 6 || y == 3 {
	x = 10
	y = 20
}

ajustar_posicao(x, y)
emergir

// Saída final
Println(a)
Println(ang)
Println(b)
Println(x)
Println(c)
Println(y)

```

## Descrição do Código

Este código apresenta uma simulação do controle de um submarino utilizando a linguagem desenvolvida para operações subaquáticas. Ele demonstra a execução de comandos básicos, como movimentação, ajustes de posição e inclinação, além de verificar condições e gerenciar variáveis que representam parâmetros importantes da navegação. O objetivo é ilustrar o funcionamento de estruturas da linguagem, como loops, condicionais e comandos específicos do submarino.

## Funcionalidades Existentes

- **Declaração de Variáveis:**
  - Inicialização de variáveis inteiras (`int`) e strings (`string`) para controle dos parâmetros do submarino, como profundidade, velocidade, e nível de energia.
  
- **Comandos de Controle do Submarino:**
  - `ativar_propulsor(duracao)`: Ativa o propulsor principal por um tempo determinado.
  - `submergir`: Submerge o submarino, aumentando sua profundidade.
  - `ajustar_inclinacao`: Ajusta a inclinação do submarino para estabilização.
  - `ajustar_posicao(x, y)`: Reposiciona o submarino para as coordenadas `(x, y)`.
  - `emergir`: Faz o submarino emergir à superfície.

- **Estruturas de Controle:**
  - **Loop `for`:** Simula a variação da profundidade do submarino em um intervalo definido, ao mesmo tempo que reduz o nível de energia.
  - **Condicional `if`:** Verifica o nível de energia e define o estado da operação como crítico ou suficiente.

- **Impressão de Dados:**
  - O comando `Println` é utilizado para exibir informações no console, incluindo valores das variáveis e mensagens de status.

## Exemplo de Saída
```
Propulsor ativado durante 30 segundos para efetuar o deslocamento
O submarino está submergindo para maior profundidade
90
91
92
93
94
95
96
97
98
99
O submarino está ajustando a inclinacao
O submarino está reposicionando-se para a coordenada (10, 20)
O submarino está emergindo para a superficie
A inclinação final foi:
90
A coordenada x final foi:
10
A coordenada y final foi:
20
```
