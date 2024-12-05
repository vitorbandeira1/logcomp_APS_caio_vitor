# Importação de bibliotecas
from abc import ABC, abstractmethod

# Classe SymbolTable
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def set_symbol(self, name, tipo, value):
        self.symbols[name] = (value, tipo)

    def get_symbol(self, name):
        return self.symbols.get(name)

# Classe abstrata Node
class Node(ABC):
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

    @abstractmethod
    def evaluate(self, symbol_table):
        pass

# Operações binárias
class BinOp(Node):
    def evaluate(self, symbol_table):
        left = self.children[0].evaluate(symbol_table)
        right = self.children[1].evaluate(symbol_table)

        left_val, left_type = left
        right_val, right_type = right

        if left_type != right_type and self.value != ".":
            raise TypeError("Operação entre tipos incompatíveis")

        operations = {
            "+": lambda: (left_val + right_val, "INT"),
            ".": lambda: (str(left_val) + str(right_val), "STR"),
            "-": lambda: (left_val - right_val, "INT"),
            "*": lambda: (left_val * right_val, "INT"),
            "/": lambda: (left_val // right_val, "INT"),
            "||": lambda: (int(left_val or right_val), "INT"),
            "&&": lambda: (int(left_val and right_val), "INT"),
            ">": lambda: (int(left_val > right_val), "INT"),
            "<": lambda: (int(left_val < right_val), "INT"),
            "==": lambda: (int(left_val == right_val), "INT")
        }

        return operations.get(self.value, lambda: None)()

# Operações unárias
class UnOp(Node):
    def evaluate(self, symbol_table):
        operand = self.children[0].evaluate(symbol_table)[0]

        operations = {
            "+": lambda: (operand, "INT"),
            "-": lambda: (-operand, "INT"),
            "!": lambda: (int(not operand), "INT")
        }

        return operations.get(self.value, lambda: None)()

# Valores inteiros
class IntVal(Node):
    def evaluate(self, symbol_table):
        return (self.value, "INT")

# Valores de string
class StringVal(Node):
    def evaluate(self, symbol_table):
        return (self.value, "STR")

# Declaração de variáveis
class VarDec(Node):
    def evaluate(self, symbol_table):
        var_name = self.children[0].value
        var_value = None if len(self.children) == 1 else self.children[1].evaluate(symbol_table)[0]

        if var_name in symbol_table.symbols:
            raise ValueError(f"Variável '{var_name}' já declarada")

        symbol_table.set_symbol(var_name, self.value, var_value)

# Identificadores
class Identifier(Node):
    def evaluate(self, symbol_table):
        return symbol_table.get_symbol(self.children[0])

# Atribuição
class Assignment(Node):
    def evaluate(self, symbol_table):
        var_name = self.children[0]
        new_value, new_type = self.children[1].evaluate(symbol_table)

        current_value, current_type = symbol_table.get_symbol(var_name)
        if current_type != new_type:
            raise TypeError(f"Tipos incompatíveis na atribuição: {current_type} e {new_type}")

        symbol_table.set_symbol(var_name, current_type, new_value)

# Bloco de código
class Block(Node):
    def evaluate(self, symbol_table):
        for child in self.children:
            child.evaluate(symbol_table)

# Programa principal
class Program(Node):
    def evaluate(self, symbol_table):
        for child in self.children:
            child.evaluate(symbol_table)

# Comando de escrita
class Escrever(Node):
    def evaluate(self, symbol_table):
        print(self.children[0].evaluate(symbol_table)[0])

# Condicional
class Se(Node):
    def evaluate(self, symbol_table):
        condition = self.children[0].evaluate(symbol_table)[0]
        if condition:
            self.children[1].evaluate(symbol_table)
        elif len(self.children) > 2:
            self.children[2].evaluate(symbol_table)

# Laço de repetição
class Enquanto(Node):
    def evaluate(self, SymbolTable):
        self.children[0].evaluate(SymbolTable)
        while self.children[1].evaluate(SymbolTable)[0]:
            self.children[3].evaluate(SymbolTable)
            self.children[2].evaluate(SymbolTable)

# Comando de escaneamento
class Escanear(Node):
    def evaluate(self, symbol_table):
        return self.value

# Comandos de controle do submarino
class Emergir(Node):
    def evaluate(self, symbol_table):
        print("O submarino está emergindo para a superficie")

class Submergir(Node):
    def evaluate(self, symbol_table):
        print("O submarino está submergindo para maior profundidade")

class AjustarInc(Node):
    def evaluate(self, symbol_table):
        print("O submarino está ajustando a inclinacao")

class AjustarPos(Node):
    def evaluate(self, symbol_table):
        coords = (self.children[0].evaluate(symbol_table)[0], self.children[1].evaluate(symbol_table)[0])
        print(f"O submarino está reposicionando-se para a coordenada {coords}")

class Ativar(Node):
    def evaluate(self, symbol_table):
        duration = self.children[0].evaluate(symbol_table)[0]
        print(f"Propulsor ativado durante {duration} segundos para efetuar o deslocamento")

# No-Operation
class NoOp(Node):
    def evaluate(self, symbol_table):
        pass