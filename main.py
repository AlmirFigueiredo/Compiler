from lexical_analyzer import convert_to_tokens
from syntactic_analyzer import analyze
if __name__ == '__main__':
        with open('texto.txt', 'r') as file:
            text = file.read()
        lines = text.split('\n')
        for line in lines:
            tokens_per_line = []    
            if len(line) == 0:
                continue
            line_tokens = convert_to_tokens(line)
            for tup in line_tokens:
                if tup[1] == 'COMMENT':
                    continue
                tokens_per_line.append(tup[1])

            print(analyze(tokens_per_line))
    
        
            
        
