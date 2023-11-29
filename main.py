from lexical_analyzer import convert_to_tokens
from syntactic_analyzer import analyze
if __name__ == '__main__':
        with open('texto.txt', 'r') as file:
            text = file.read()
        lines = text.split('\n')
        lexs_and_tokens = convert_to_tokens(lines[0])
        print(analyze(lexs_and_tokens))
        
