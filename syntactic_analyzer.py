from lexical_analyzer import TOKENS_DICT

valid_tokens = TOKENS_DICT.keys()
tokens = []
i = 0
final = 0
def analyze(lexs_and_tokens):
    global final
    for token in lexs_and_tokens:
        tokens.append(token[1])
    final = len(tokens)
    return check_grammar(tokens)



def atribuicao(tokens):
    global final
    global i
    if tokens[i] == 'ID':
        i += 1
        if i < final and (tokens[i] == '=' or tokens[i] == '+=' or tokens[i] == '-=' or tokens[i] == '*=' or tokens[i] == '/=' or tokens[i] == '%=' or tokens[i] == '&&='):
            i += 1
            if i < final:
                return expressao(tokens)
    return False
def primaria(tokens):
    global final
    global i
    
    if tokens[i] == 'ID' or tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DEC' or tokens[i] == 'TEXTO':
        i += 1
        return True
    if tokens[i] == '(':
        i += 1
        if i < final:
            if(expressao(tokens)):
                i += 1
                if i < final and tokes[i] == ')':
                    i += 1
                    return True
    return False
def expressao_lista(tokens):
    return True

def expressao_postfix(tokens):
    global final
    global i
    if(primaria(tokens)):
        i += 1
        if i == final:
            return True
        if tokens[i] == '[':
            i += 1
            if i < final and expressao(tokens):
                i += 1
                if i < final and tokens[i] == ']':
                    i += 1
                    return True
        elif tokens[i] == '(':
            i += 1
            if i < final and expressao_lista(tokens):
                i += 1
            elif i < final and tokens[i] == ')':
                i += 1
                return True
        elif tokens[i] == '.':
            i += 1
            if i < final and tokens[i] == 'ID':
                i += 1
                return True
        elif tokens[i] == '->':
            i += 1
            if i < final and tokens[i] == 'ID':
                i += 1
                return True

    return False
    
def expressao_unaria(tokens):
    global final
    global i
    if(expressao_postfix(tokens)):
        return True
    elif tokens[i] == '++' or tokens[i] == '--':
        i += 1
        if(expressao_postfix(tokens)):
            return True
    elif tokens[i] == '-':
        i += 1
        if(expressao_unaria(tokens)):
            i += 1
            return True
    return False
    

def expressao_multiplicativa(tokens):
    global final
    global i
    if(expressao_unaria(tokens)):
        return True
    if(expressao_multiplicativa(tokens)):
        if i < final and tokens[i] == '*' or tokens[i] == '/' or tokens[i] == '%':
            i += 1
            if i < final and expressao_unaria(tokens[i]):
                i += 1
                return True
    return False
def expressao_aritmetica(tokens):
    global i
    global final
    if(expressao_multiplicativa(tokens)):
        return True
    elif(expressao_aritmetica(tokens)):
        i += 1
        if i < final and (tokens[i] == '+' or tokens[i] == '-'):
            i += 1
            return expressao_multiplicativa(tokens)
    return False

def expressao_relacional(tokens):
    global i
    global final
    if(expressao_aritmetica(tokens)):
        i += 1
        if i == final:
            return True
        if tokens[i] == '>' or tokens[i] == '>=' or tokens[i] == '<' or tokens[i] == '<=' or tokens[i] == '!=' or tokens[i] == '==':
            i += 1
            return expressao_aritmetica(tokens)

    return False

def expressao_logica(tokens):
    global final
    global i
    if(expressao_relacional(tokens)):
        i += 1
        if i == final:
            return True
        if expressao_logica(tokens):
            i += 1
            if i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                return expressao_relacional(tokens)
    if i < final and tokens[i] == '!':
        i += 1
        if i < final and expressao_relacional(tokens):
            i += 1
            return True
    return False

def expressao(tokens):
    if atribuicao(tokens):
        return True
    return expressao_logica(tokens)

def declaracao_de_variavel(tokens):
    global final
    global i
    if tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == ';':
                i += 1
                return True
            elif i < final and tokens[i] == '=':
                i += 1
                if i < final and expressao(tokens[i]):
                    i += 1
                    if i < final and tokens[i] == ';':
                        i += 1
                        return True
    return False
def check_grammar(tokens):
    global i
    global final
    while i < final:
        #Declaracao
        if(declaracao_de_variavel(tokens)):
            return True
        i += 1
    return False