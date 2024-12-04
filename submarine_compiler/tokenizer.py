# Declarando a classe Token
class Token:
    def __init__(self, type: str, value: any):
        self.type = type
        self.value = value

# Declarando a classe Tokenizer
class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.next = None

    def select_next(self):
        # Processar a fonte e identificar o próximo token
        while self.position < len(self.source):
            char = self.source[self.position]

            # Ignorar espaços em branco
            if char.isspace():
                self.position += 1
                continue

            # Processar números
            if char.isdigit():
                number = ""
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    number += self.source[self.position]
                    self.position += 1
                self.next = Token("INT", int(number))
                return

            # Processar tokens únicos
            single_char_tokens = {
                "+": "PLUS",
                "-": "MINUS",
                "*": "MULTIPLY",
                "/": "DIVIDE",
                "(": "PARENTESE_ABERTO",
                ")": "PARENTESE_FECHADO",
                "{": "CHAVES_ABERTO",
                "}": "CHAVES_FECHADO",
                ";": "PONTO_E_VIRGULA",
                ",": "VIRGULA",
                ">": "MAIOR_QUE",
                "<": "MENOR_QUE",
                "!": "NOT",
                ".": "PONTO",
            }
            if char in single_char_tokens:
                self.position += 1
                self.next = Token(single_char_tokens[char], None)
                return

            # Processar strings
            if char == '"':
                self.position += 1
                start = self.position
                while self.position < len(self.source) and self.source[self.position] != '"':
                    self.position += 1
                if self.position >= len(self.source):
                    raise SyntaxError("String não terminada")
                string_value = self.source[start:self.position]
                self.position += 1
                self.next = Token("STRING", string_value)
                return

            # Processar igualdade (==) e atribuição (=)
            if char == "=":
                self.position += 1
                if self.position < len(self.source) and self.source[self.position] == "=":
                    self.position += 1
                    self.next = Token("IGUAL_IGUAL", None)
                else:
                    self.next = Token("IGUAL", None)
                return

            # Processar identificadores e palavras reservadas
            if char.isalpha() or char == "_":
                start = self.position
                while self.position < len(self.source) and (
                    self.source[self.position].isalnum() or self.source[self.position] == "_"
                ):
                    self.position += 1
                palavra = self.source[start:self.position]

                # Verificar palavras reservadas
                reserved_words = {
                    "Println": "PRINT",
                    "submergir": "SUBMERGIR",
                    "emergir": "EMERGIR",
                    "ajustar_inclinacao": "AJUSTAR_INCLINACAO",
                    "ajustar_posicao": "AJUSTAR_POSICAO",
                    "ativar_propulsor": "ATIVAR_PROPULSOR",
                    "for": "FOR",
                    "if": "IF",
                    "else": "ELSE",
                    "var": "VAR",
                    "int": "TYPE_INT",
                    "string": "TYPE_STRING",
                }
                if palavra in reserved_words:
                    self.next = Token(reserved_words[palavra], None)
                else:
                    self.next = Token("IDENTIFIER", palavra)
                return

            raise SyntaxError(f"Caractere inválido: {char}")

        # Finalizar com EOF
        self.next = Token("EOF", None)
