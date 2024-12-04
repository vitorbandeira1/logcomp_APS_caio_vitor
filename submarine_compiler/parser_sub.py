# Importando bibliotecas
from tokenizer import Tokenizer, Token
from nodes import *


#Declarando a classe Token

class Parser:
    tokenizer = None

    # Método - Program
    def parse_program():
        program_node = Program(None, [])
        while Parser.tokenizer.next.type != "EOF":
            statement_node = Parser.parse_statement()
            if statement_node:
                program_node.children.append(statement_node)
        return program_node

    def parse_block():
        if Parser.tokenizer.next.type != "CHAVES_ABERTO":
            raise SyntaxError("Esperado '{' no início do bloco")
        
        Parser.tokenizer.select_next()
        block_node = Block(None, [])

        while Parser.tokenizer.next.type != "CHAVES_FECHADO":
            statement_node = Parser.parse_statement()
            if statement_node:
                block_node.children.append(statement_node)
        
        Parser.tokenizer.select_next()  # Consome '}'
        return block_node

    def parse_assignment():
        variable_name = Parser.tokenizer.next.value
        Parser.tokenizer.select_next()

        if Parser.tokenizer.next.type == "IGUAL":
            Parser.tokenizer.select_next()
            assignment_node = Assignment("=", [variable_name, Parser.parse_bool_expression()])

            if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                Parser.tokenizer.select_next()
                return assignment_node
            raise SyntaxError("Esperado ';' após a atribuição")
        raise SyntaxError("Erro na atribuição")

    # Método - Statement
    def parse_statement():
        if Parser.tokenizer.next.type == "PULA_LINHA":
            Parser.tokenizer.select_next()
            return NoOp(None, None)

        if Parser.tokenizer.next.type in ["EMERGIR", "SUBMERGIR", "AJUSTARINC"]:
            command = Parser.tokenizer.next.type
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                Parser.tokenizer.select_next()
                return Node(command, [])
            raise SyntaxError(f"Esperado ';' após o comando {command}")

        if Parser.tokenizer.next.type == "AJUSTARPOS":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE_ABERTO":
                Parser.tokenizer.select_next()
                x = Parser.parse_expression()

                if Parser.tokenizer.next.type == "VIRGULA":
                    Parser.tokenizer.select_next()
                    y = Parser.parse_expression()

                    if Parser.tokenizer.next.type == "PARENTESE_FECHADO":
                        Parser.tokenizer.select_next()

                        if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                            Parser.tokenizer.select_next()
                            return AjustarPos(None, [x, y])
            raise SyntaxError("Erro ao processar 'ajustar_posicao'")

        if Parser.tokenizer.next.type == "ATIVAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE_ABERTO":
                Parser.tokenizer.select_next()
                intensidade = Parser.parse_expression()

                if Parser.tokenizer.next.type == "PARENTESE_FECHADO":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                        Parser.tokenizer.select_next()
                        return Ativar(None, [intensidade])
            raise SyntaxError("Erro ao processar 'ativar_propulsor'")

        if Parser.tokenizer.next.type == "PRINT":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE_ABERTO":
                Parser.tokenizer.select_next()
                expr = Parser.parse_expression()

                if Parser.tokenizer.next.type == "PARENTESE_FECHADO":
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                        Parser.tokenizer.select_next()
                        return Escrever(None, [expr])
            raise SyntaxError("Erro ao processar 'Println'")

        if Parser.tokenizer.next.type == "IF":
            Parser.tokenizer.select_next()
            condition = Parser.parse_bool_expression()
            if_block = Parser.parse_block()

            node = Se(None, [condition, if_block])

            if Parser.tokenizer.next.type == "ELSE":
                Parser.tokenizer.select_next()
                else_block = Parser.parse_block()
                node.children.append(else_block)

            if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                Parser.tokenizer.select_next()
                return node
            raise SyntaxError("Esperado ';' após o comando 'if'")

        if Parser.tokenizer.next.type == "FOR":
            Parser.tokenizer.select_next()
            init = Parser.parse_assignment()

            if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                Parser.tokenizer.select_next()
                condition = Parser.parse_bool_expression()

                if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                    Parser.tokenizer.select_next()
                    update = Parser.parse_assignment()
                    loop_block = Parser.parse_block()

                    if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                        Parser.tokenizer.select_next()
                        return Enquanto(None, [init, condition, update, loop_block])
            raise SyntaxError("Erro ao processar 'for'")

        if Parser.tokenizer.next.type == "VAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "IDEN":
                identifier = Identifier(Parser.tokenizer.next.value, [])
                Parser.tokenizer.select_next()

                if Parser.tokenizer.next.type == "TYPE_INT" or Parser.tokenizer.next.type == "TYPE_STRING":
                    var_type = Parser.tokenizer.next.type
                    Parser.tokenizer.select_next()

                    if Parser.tokenizer.next.type == "PONTO_E_VIRGULA":
                        Parser.tokenizer.select_next()
                        return VarDec(var_type, [identifier])
            raise SyntaxError("Erro na declaração de variável")

        raise SyntaxError(f"Token inesperado: {Parser.tokenizer.next.type}")


    def parse_expression():

        filho_esquerdo = Parser.parse_term()

        while Parser.tokenizer.next.type in ["PLUS" , "MINUS", "PONTO"]:

            if Parser.tokenizer.next.type == "PLUS":
                Parser.tokenizer.select_next()
                node = BinOp("+", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MINUS":
                Parser.tokenizer.select_next()
                node = BinOp("-", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node
            
            elif Parser.tokenizer.next.type == "PONTO":
                Parser.tokenizer.select_next()
                node = BinOp(".", [filho_esquerdo, Parser.parse_term()])
                filho_esquerdo = node

            else:
                raise Exception()
            
        return filho_esquerdo
    

    # Método - Term

    def parse_term():

        filho_esquerdo = Parser.parse_factor()
        while Parser.tokenizer.next.type in ["MULTIPLY" , "DIVIDE"]:

            if Parser.tokenizer.next.type == "MULTIPLY":
                Parser.tokenizer.select_next()
                node = BinOp("*", [filho_esquerdo, Parser.parse_factor()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "DIVIDE":
                Parser.tokenizer.select_next()
                node = BinOp("/", [filho_esquerdo, Parser.parse_factor()])
                filho_esquerdo = node
            else:
                raise Exception()
        
        return filho_esquerdo
    

    # Método - Factor

    def parse_factor():

        if Parser.tokenizer.next.type == "INT":
            resultado_int = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return IntVal(resultado_int, [])
        
        elif Parser.tokenizer.next.type == "STRING":
            resultado_string = Parser.tokenizer.next.value
            Parser.tokenizer.select_next()
            return StringVal(resultado_string, [])

        elif Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.select_next()
            return UnOp("+", [Parser.parse_factor()])

        elif Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.select_next()
            return UnOp("-", [Parser.parse_factor()])
        
        elif Parser.tokenizer.next.type == "NOT":
            Parser.tokenizer.select_next()
            return UnOp("!", [Parser.parse_factor()])
        
        elif Parser.tokenizer.next.type == "PARENTESE ABERTO":
            Parser.tokenizer.select_next()
            Parser.resultado_factor = Parser.parse_bool_expression()

            if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                Parser.tokenizer.select_next()
                return Parser.resultado_factor
            
        elif Parser.tokenizer.next.type == "IDEN":
            retorno_iden = Identifier(None, [Parser.tokenizer.next.value])
            Parser.tokenizer.select_next()
            return retorno_iden
        
        elif Parser.tokenizer.next.type == "SCANEAR":
            Parser.tokenizer.select_next()

            if Parser.tokenizer.next.type == "PARENTESE ABERTO":
                Parser.tokenizer.select_next()
                valor_scan = int(input())

                if Parser.tokenizer.next.type == "PARENTESE FECHADO":
                    Parser.tokenizer.select_next()
                    return Escanear(valor_scan, [])


        raise Exception() 
    
    # Método - Bool_expression
    
    def parse_bool_expression():

        filho_esquerdo = Parser.parse_bool_term()

        while Parser.tokenizer.next.type in ["OR"]:

            Parser.tokenizer.select_next()
            node = BinOp("||", [filho_esquerdo, Parser.parse_bool_term()])
            filho_esquerdo = node

        # print("return do bool expression")
        return filho_esquerdo


    # Método - Bool_term

    def parse_bool_term():

        filho_esquerdo = Parser.parse_rel_expression()

        while Parser.tokenizer.next.type in ["AND"]:

            Parser.tokenizer.select_next()
            node = BinOp("&&", [filho_esquerdo, Parser.parse_rel_expression()])
            filho_esquerdo = node
            
        return filho_esquerdo
    
    # Método - Rel_expression

    def parse_rel_expression():

        filho_esquerdo = Parser.parse_expression()

        while Parser.tokenizer.next.type in ["IGUAL IGUAL", "MAIOR QUE", "MENOR QUE"]:

            if Parser.tokenizer.next.type == "IGUAL IGUAL":
                Parser.tokenizer.select_next()
                node = BinOp("==", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MAIOR QUE":
                Parser.tokenizer.select_next()
                node = BinOp(">", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node

            elif Parser.tokenizer.next.type == "MENOR QUE":
                Parser.tokenizer.select_next()
                node = BinOp("<", [filho_esquerdo, Parser.parse_expression()])
                filho_esquerdo = node
        
        return filho_esquerdo
    
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.select_next()
        program = Parser.parse_program()

        if Parser.tokenizer.next.type != "EOF":
            raise SyntaxError("Tokens inesperados após o final do programa")

        return program