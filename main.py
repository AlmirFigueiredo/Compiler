from lexical_analyzer import convert_to_tokens
from syntactic_analyzer import analyze
if __name__ == '__main__':
        with open('texto.txt', 'r') as file:
            text = file.read()
        lines = text.split('\n')
        result = True
        for i,line in enumerate(lines):
            tokens_per_line = []    
            if len(line) == 0:
                
                continue
            line_tokens = convert_to_tokens(line)
            for tup in line_tokens:
                if tup[1] == 'COMMENT':
                    continue
                    
                tokens_per_line.append(tup[1])
            print(f"Linha {i+1}")
            if not analyze(tokens_per_line):
                result = False
                print("==============================================")
                break
            print(f"Nenhum erro de sintaxe encontrado na linha")
            print("=================================================")

        from syntactic_analyzer import blocks
        if blocks != 0:
            print("Erro de abertura/fechamento de bloco encontrado!")
        if result and blocks == 0:
            print("Nenhum erro de sintaxe encontrado!!")

    


            
        
