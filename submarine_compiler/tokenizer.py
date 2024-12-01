#Declarando a classe Token
class Token:
    
    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value

#Declarando a classe Tokenizer
class Tokenizer:

    def __init__(self, source: str, next: Token):
        self.source = source
        self.position = 0
        self.next = next

    def select_next(self):

        #Tokens
        while self.position < len(self.source):
            
            char = self.source[self.position]            

            if char.isnumeric():
                number = ""
                while self.position < len(self.source) and self.source[self.position].isnumeric():
                    number += self.source[self.position]
                    self.position += 1
                self.next = Token("INT", int(number))
                return
                        
            single_char_tokens = {
                "+": "PLUS",
                "-": "MINUS",
                "*": "MULTIPLY",
                "/": "DIVIDE",
                "(": "PARENTESE ABERTO",
                ")": "PARENTESE FECHADO",
                "{": "CHAVES ABERTO",
                "}": "CHAVES FECHADO",
                ">": "MAIOR QUE",
                "<": "MENOR QUE",
                "!": "NOT",
                ",": "VIRGULA",
                ";": "PONTO E VIRGULA",
                ".": "PONTO",
            }

            if char in single_char_tokens:
                self.position += 1
                self.next = Token(single_char_tokens[char], None)
                return
                        
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
            
            if char == "=":
                self.position += 1
                if self.position < len(self.source) and self.source[self.position] == "=":
                    self.position += 1
                    self.next = Token("IGUAL IGUAL", None)
                else:
                    self.next = Token("IGUAL", None)
                return
            
            elif char == "\n":
                tipo = "PULA LINHA"
                valor = 0
                self.position += 1
                self.next = Token(tipo, valor)
                return
            
            elif char in [",", "[", "]"]:
                raise Exception()
            
            # if char in ["|", "&"]:
            #     operator = char
            #     self.position += 1
            #     if self.position < len(self.source) and self.source[self.position] == char:
            #         operator += char
            #         self.position += 1
            #         self.next = Token("OR" if operator == "||" else "AND", None)
            #         return
            #     raise SyntaxError(f"Operador inválido: {operator}")
            
            elif type(char) == str:
                palavra = ""
            
                while ((char.isidentifier()) or (char.isdigit())):
                    char = self.source[self.position]
                    if not ((char.isidentifier()) or (char.isdigit())):
                        self.position -= 1
                        break
                    
                    palavra += char
                    self.position += 1

                if palavra == "Println":
                    tipo = "PRINTAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "emergir":
                    tipo = "EMERGIR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "submergir":
                    tipo = "SUBMERGIR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ajustar_inclinacao":
                    tipo = "AJUSTARINC"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ajustar_posicao":
                    tipo = "AJUSTARPOS"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                if palavra == "ativar_propulsor":
                    tipo = "ATIVAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "for":
                    tipo = "FOR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "if":
                    tipo = "IF"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "else":
                    tipo = "ELSE"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "Scanln":
                    tipo = "SCANEAR"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "var":
                    tipo = "VARIAVEL"
                    valor = 0
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
            
                elif palavra == "int":
                    tipo = "TYPE"
                    valor = "INT"
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif palavra == "string":
                    tipo = "TYPE"
                    valor = "STR"
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return
                
                elif char in ["|", "&"]:
                    while char in ["|", "&"]:
                        
                        if palavra == "||":
                            tipo = "OR"
                            valor = 0
                            self.position += 1
                            self.next = Token(tipo, valor)
                            return
                        
                        elif palavra == "&&":
                            tipo = "AND"
                            valor = 0
                            self.position += 1
                            self.next = Token(tipo, valor)
                            return
                        
                        palavra += char
                        self.position += 1

                elif palavra == "":
                    self.position += 1

                else:
                    tipo = "IDEN"
                    valor = palavra
                    self.position += 1
                    self.next = Token(tipo, valor)
                    return

            else:
                self.position += 1

        if self.position >= len(self.source):
            tipo = "EOF"
            self.next = Token(tipo, 0)
            return