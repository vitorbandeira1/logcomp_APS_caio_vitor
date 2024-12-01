# LogComp-APS - Submarinos

## Sobre a linguagem desenvolvida

Este projeto apresenta uma linguagem de programação desenvolvida para o controle de submarinos. Inspirada na necessidade de simplificar a operação de veículos subaquáticos, a linguagem foi projetada para oferecer comandos intuitivos e eficientes, permitindo a execução de manobras e ajustes diretamente relacionados à navegação submersa. Com isso, busca-se facilitar o desenvolvimento de soluções voltadas para atividades exploratórias e operacionais no ambiente aquático.


## EBNF da linguagem

```ebnf
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
```

## Exemplo

```
// Declaração de variáveis
var profundidade int
var velocidade int
var energia int

var mensagem string
var status_energia string

mensagem = "Estado atual da operação: "
status_energia = "Nível de energia restante: "

// Inicialização
profundidade = 50
velocidade = 20
energia = 100

// Ativação do propulsor para iniciar o movimento
ativar_propulsor(15)
submergir

// Ajuste de inclinação antes da navegação
ajustar_inclinacao

// Loop para simular variação da profundidade
for profundidade = 100; profundidade > 50; profundidade = profundidade - 10 {
	Println(profundidade)
	energia = energia - 5
}

// Condicional para verificar energia restante
if energia < 50 {
	status_energia = "Alerta: nível crítico"
} else {
	status_energia = "Energia suficiente"
}

// Ajuste final de posição
ajustar_posicao(25, 45)
emergir

// Ajuste final de posição
ajustar_posicao(25, 45)
emergir

// Saída final
Println(mensagem)
Println(status_energia)
Println("Profundidade final: " . profundidade)
Println("Velocidade final: " . velocidade)
Println("Nível de energia final: " . energia)

```

## Descrição do Código

Este código apresenta uma simulação do controle de um submarino utilizando a linguagem desenvolvida para operações subaquáticas. Ele demonstra a execução de comandos básicos, como movimentação, ajustes de posição e inclinação, além de verificar condições e gerenciar variáveis que representam parâmetros importantes da navegação. O objetivo é ilustrar o funcionamento de estruturas da linguagem, como loops, condicionais e comandos específicos do submarino.

## Funcionalidades Demonstradas

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
Propulsor principal ativado por 15 segundos para impulsionar o deslocamento
O submarino está submergindo para maior profundidade
O submarino está ajustando a inclinação para estabilização
100
90
80
70
60
50
O submarino está reposicionando-se para a coordenada (25, 45)
O submarino está emergindo para a superfície
Estado atual da operação:
Energia suficiente
Profundidade final: 50
Velocidade final: 20
Nível de energia final: 75
```
