from lexical_analyzer import convert_to_tokens
from syntactic_analyzer import analyze
if __name__ == '__main__':
        with open('texto.txt', 'r') as file:
            text = file.read()
        lines = text.split('\n')
        for i in range(0, len(lines)):
            lexs_and_tokens = convert_to_tokens(lines[i])
            print(f'Linha {i+1}: {analyze(lexs_and_tokens)}')
            
        
