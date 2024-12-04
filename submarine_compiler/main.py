# Importação de bibliotecas
import sys
from parser_sub import Parser
from pre_pro import PrePro
from nodes import SymbolTable

def main(file_path):
    try:
        # Leitura do arquivo
        print("[INFO] Lendo o arquivo...")
        with open(file_path, 'r') as go_file:
            go_code = go_file.read()

        # Pré-processamento do código
        print("[INFO] Pré-processando o código...")
        prepro = PrePro()
        filtered_text = prepro.filter(go_code)

        # Inicialização da tabela de símbolos
        symbol_table = SymbolTable()

        # Parsing e avaliação do código
        print("[INFO] Analisando e executando o programa...")
        root_node = Parser.run(filtered_text)
        root_node.evaluate(symbol_table)

        print("[INFO] Execução concluída com sucesso!")

    except FileNotFoundError:
        print(f"[ERRO] Arquivo '{file_path}' não encontrado.")
    except SyntaxError as e:
        print(f"[ERRO] Erro de sintaxe: {e}")
    except Exception as e:
        print(f"[ERRO] Erro durante a execução: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <caminho_para_o_arquivo>")
        sys.exit(1)

    main(sys.argv[1])
