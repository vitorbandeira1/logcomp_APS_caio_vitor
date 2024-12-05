# Importação de bibliotecas
import sys
from parser_sub import Parser
from pre_pro import PrePro
from nodes import SymbolTable

def main(file_path):
    # Leitura do arquivo
    with open(file_path, 'r') as go_file:
        go_code = go_file.read()

    # Pré-processamento do código
    prepro = PrePro()
    filtered_text = prepro.filter(go_code)

    # Inicialização da tabela de símbolos
    symbol_table = SymbolTable()

    # Parsing e avaliação do código
    root_node = Parser.run(filtered_text)
    root_node.evaluate(symbol_table)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_o_arquivo>")
        sys.exit(1)

    main(sys.argv[1])