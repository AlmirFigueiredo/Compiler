import re
import pandas as pd

TOKENS_DICT = {
    'NUM_INT': r'\d+',
    'NUM_DEC': r'\d+\.\d+',
    'Tipo': r'(int|float|double|char|boolean)',
    '[': r'\[',
    ']': r'\]',
    '=': r'=',
    '+=': r'\+=',
    '-=': r'-=',
    '*=': r'\*=',
    '/=': r'/=',
    '%=': r'%=',
    '&&=': r'&&=',
    '||=': r'\|\|=',
    'if': r'if',
    'else': r'else',
    'while': r'while',
    'for': r'for',
    ';': r';',
    ',': r',',
    'switch': r'switch',
    'case': r'case',
    'default': r'default',
    ':': r':',
    'break': r'break',
    'continue': r'continue',
    'return': r'return',
    'struct': r'struct',
    '&&': r'&&',
    '||': r'\|\|',
    '>': r'>',
    '>=': r'>=',
    '<': r'<',
    '<=': r'<=',
    '!=': r'!=',
    '==': r'==',
    '++': r'\+\+',
    '+': r'\+',
    '--': r'--',
    '-': r'-',
    '*': r'\*',
    '/': r'/',
    '%': r'%',
    '.': r'\.', 
    '->': r'->',
    'TEXTO': r'"[^"]*"',
    'void': r'void',
    'scanf': r'scanf',
    'println': r'println',
    'main': r'main',
    '(': r'\(',
    ')': r'\)',
    '{': r'\{',
    '}': r'\}',
    'ID': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'COMMENT': r'//.*',
}
special = ['(', ')', '!', '=', '[', ']', '/', '"', '*', '+', '-', ' ', '&', ';', ':', '<', '>', ',']
def convert_to_lexs(line_text):
    line_text_lexs = []
    final = len(line_text)
    i = 0
    while i < final:
            lexema = ''
            if line_text[i] == ' ':
                i += 1
            #Quando tiver texto
            elif line_text[i] == '"':
                lexema += '"'
                i += 1
                while i < final and line_text[i] != '"':
                    lexema += line_text[i]
                    i += 1
                lexema += line_text[i]
                i += 1
            #Quando tem barra pode ser varias coisas
            elif line_text[i] == '/':
                lexema += '/'
                i += 1
                #Quando for comment
                if i < final and line_text[i] == '/':
                    lexema += '/'
                    i += 1
                    while i < final:
                        lexema += line_text[i]
                        i += 1
                #Quando for divisao igual
                elif i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            #Colchete
            elif line_text[i] == '[':
                lexema += '['
                i += 1
            elif line_text[i] == ']':
                lexema += ']'
                i += 1
            #Chave
            elif line_text[i] == '{':
                lexema += '{'
                i += 1
            elif line_text[i] == '}':
                lexema += '}'
                i += 1
            #Parenteses
            elif line_text[i] == '(':
                lexema += '('
                i += 1
            elif line_text[i] == ')':
                lexema += ')'
                i += 1
            
            #Igual
            elif line_text[i] == '=':
                lexema += '='
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            #Mais
            elif line_text[i] == '+':
                lexema += '+'
                i += 1
                if i < final and line_text[i] == '+':
                    lexema += '+'
                    i += 1
                elif i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            #Menos
            elif line_text[i] == '-':
                lexema += '-'
                i += 1
                if i < final and line_text[i] == '-':
                    lexema += '-'
                    i += 1
                elif i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
                elif i < final and line_text[i] == '>':
                    lexema += '>'
                    i += 1
            # Multiplicacao
            elif line_text[i] == '*':
                lexema += '*'
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            # Modulo
            elif line_text[i] == '%':
                lexema += '%'
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            # E comercial
            elif line_text[i] == '&':
                lexema += '&'
                i += 1
                if i < final and line_text[i] == '&':
                    lexema += '&'
                    i += 1
                    if i < final and line_text[i] == '=':
                        lexema += '='
                        i += 1
            # Pipe
            elif line_text[i] == '|':
                lexema += '|'
                i += 1
                if i < final and line_text[i] == '|':
                    lexema += '|'
                    i += 1
                    if i < final and line_text[i] == '=':
                        lexema += '='
                        i += 1
            #Maior
            elif line_text[i] == '>':
                lexema += '>'
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            #Menor
            elif line_text[i] == '<':
                lexema += '<'
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            #Negacao
            elif line_text[i] == '!':
                lexema += '!'
                i += 1
                if i < final and line_text[i] == '=':
                    lexema += '='
                    i += 1
            # Dois ponto
            elif line_text[i] == ':':
                lexema += ':'
                i += 1
            # Semi collon
            elif line_text[i] == ';':
                lexema += ';'
                i += 1
            elif line_text[i] == ',':
                lexema += ','
                i += 1
            else:
                while i < final and line_text[i] not in special:
                    lexema += line_text[i]
                    i += 1
            if lexema != '':
                line_text_lexs.append(lexema)

    return line_text_lexs

def convert_to_tokens(line_text):
    tokens = []
    lexs_list = convert_to_lexs(line_text)

    for lexeme in lexs_list:
        found = False
        for token, regex in TOKENS_DICT.items():
            if re.fullmatch(regex, lexeme):
                tokens.append((lexeme, token))
                found = True
                break
        if not found:
            tokens.append((lexeme, 'ERRO'))

    return tokens