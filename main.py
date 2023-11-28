from lexical_analyzer import convert_to_tokens

if __name__ == '__main__':
        with open('texto.txt', 'r') as file:
            text = file.read()
        lines = text.split('\n')
        
        
