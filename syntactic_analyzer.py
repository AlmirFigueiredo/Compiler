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
    if check_grammar(tokens):
        print('Tudo Ok')
    else:
        print('Erro de sintaxe!')
# def atribuicao_declaracao_variavel_logica(tokens):
#     global i
#     global final

# def declaracao_de_variavel_logica(tokens):
#     global final
#     global i
#     if tokens[i] == 'Tipo':
#         i += 1
#         if i < final and tokens[i] == 'ID':
#             i += 1
#             if i < final and tokens[i] == ';':
#                 i += 1
#                 return True
#             elif i < final and tokens[i] == '=':
#                 i += 1
#                 if i < final and atribuicao_declaracao_variavel_logica(tokens):
#                     i += 1
#                     if i < final and tokens[i] == ';':
#                         i += 1
#                         return True
#     return False
def atribuicao_declaracao_variavel_expressao_complexa(tokens):
    global i 
    global final
    if i < final and tokens[i] == '(':
        i += 1
        result = False
        while i < final and tokens[i] != ')':
            if i < final and (tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DEC' or tokens[i] == 'ID'):
                i += 1
                if i < final and tokens[i] == ')':
                    result = True
                elif i < final and (tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '/' or tokens[i] == '*'):
                    i += 1
                    result = False
            elif i < final and tokens[i] == '(':
                if atribuicao_declaracao_variavel_expressao_complexa(tokens):
                    i += 1
                    result = True
            else:
                break
    return result or False
def atribuicao_declaracao_variavel_expressao(tokens):  
    global i
    global final
    if i < final and (tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DEC' or tokens[i] == 'ID'):
        if i+1 < final and(tokens[i+1] == '+' or tokens[i+1] == '-' or tokens[i+1] == '/' or tokens[i+1] == '*'):
            i += 2
            return atribuicao_declaracao_variavel_expressao(tokens)
        return True
    elif i < final and tokens[i] == '(':
        return atribuicao_declaracao_variavel_expressao_complexa(tokens)
    return False
def atribuicao_declaracao_variavel(tokens):
    global i
    global final
    if i < final and (tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DEC' or tokens[i] == 'ID' or tokens[i] == 'TEXTO'):
        if i+1 < final and (tokens[i+1] == '+' or tokens[i+1] == '-' or tokens[i+1] == '/' or tokens[i+1] == '*' or tokens[i+1] == '%'):
            i += 2
            return atribuicao_declaracao_variavel_expressao(tokens)
        return True
    elif i < final and tokens[i] == '(':
        return atribuicao_declaracao_variavel_expressao(tokens)
    return False

def declaracao_de_variavel(tokens):
    global final
    global i
    if tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == ';':
                i += 1
                return i == final
            elif i < final and tokens[i] == '=':
                i += 1
                if i < final and atribuicao_declaracao_variavel(tokens):
                    i += 1
                    if i < final and tokens[i] == ';':
                        i += 1
                        return True
                    while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%'):
                        if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                            i += 1
    return False
def check_grammar(tokens):
    global i
    global final
    while i < final:
        if(declaracao_de_variavel(tokens)):
            return True
        # if(declaracao_de_variavel_logica(tokens)):
        #     return True
            
        i += 1
    return False