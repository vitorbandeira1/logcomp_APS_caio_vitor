# Classe PrePro

class PrePro:
    @staticmethod
    def filter(text):
        in_comment_block = False
        filtered_lines = []

        for line in text.splitlines():
            line_without_whitespace = line.strip()

            if not in_comment_block:
                if line_without_whitespace.startswith("/*"):
                    if "*/" in line_without_whitespace:
                        # Comentário de bloco na mesma linha
                        line = line_without_whitespace.split("*/", 1)[1]
                    else:
                        # Início de comentário de bloco
                        in_comment_block = True
                        continue
                elif "//" in line_without_whitespace:
                    # Comentário de linha única
                    line = line_without_whitespace.split("//", 1)[0]

            else:
                if "*/" in line_without_whitespace:
                    # Fim de comentário de bloco
                    in_comment_block = False
                    line = line_without_whitespace.split("*/", 1)[1]
                else:
                    # Ignorar linha dentro de comentário de bloco
                    continue

            # Preservar linha vazia para não alterar índices de linha
            filtered_lines.append(line if line.strip() else "")

        return "\n".join(filtered_lines) + "\n"
