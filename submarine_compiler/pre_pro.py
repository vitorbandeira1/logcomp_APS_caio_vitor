# Classe PrePro

class PrePro:
    @staticmethod
    def filter(text):
        in_comment_block = False
        filtered_lines = []

        for line in text.splitlines():
            line_without_whitespace = line.strip()

            if not in_comment_block:
                if line_without_whitespace.startswith('/*'):
                    if '*/' not in line_without_whitespace:
                        in_comment_block = True
                    else:
                        line = line_without_whitespace.split('*/', 1)[1]
                elif '//' in line_without_whitespace:
                    line = line_without_whitespace.split('//', 1)[0]
            else:
                if '*/' in line_without_whitespace:
                    in_comment_block = False
                    line = line_without_whitespace.split('*/', 1)[1]

            if not in_comment_block:
                filtered_lines.append(line)

        return '\n'.join(filtered_lines) + '\n'