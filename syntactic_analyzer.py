from lexical_analyzer import TOKENS_DICT

valid_tokens = TOKENS_DICT.keys()
i = 0
final = 0
blocks = 0
def analyze(tokens):
    global i
    global final
    i = 0    
    final = len(tokens)
    return check_grammar(tokens)

def atribuicao_de_valores_declaracao_array(tokens):
    global i, final
    if i < final and tokens[i] != '{':
        return False
    i += 1
    while i < final:
        if tokens[i] == 'ID' or tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DECIMAL' or tokens[i] == 'Logic_value' or atribuicao_de_valor_aritmetico(tokens) or atribuicao_de_valor_logico(tokens) or atribuicao_valor_logico_relacional(tokens):
            i += 1
            if i < final and tokens[i] == '}':
                return True
            elif i < final and tokens[i] == ',':
                i += 1
                continue
            else:
                return False
        else:
            return False
    return False
def inicializacao_array(tokens):
    global i, final
    if i < final and tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == '[':
                i += 1        
                if i < final and tokens[i] == ']':
                    i += 1
                    if i < final and tokens[i] == '=':
                        i += 1
                        if i < final and atribuicao_de_valores_declaracao_array(tokens):
                            i += 1
                            if i < final and tokens[i] == ';':
                                i += 1
                                return i == final

    return False
    
def condicional_basica(tokens):
    global i
    global final
    global blocks
    if i < final and (tokens[i] == 'if' or tokens[i] == 'while'):
        i += 1
        if i < final and tokens[i] == '(':
            i += 1
            relacional = False
            if i+1 < final:
                relacional = tokens[i+1] == '>' or tokens[i+1] == '>=' or tokens[i+1] == '<' or tokens[i+1] == '<=' or tokens[i+1] == '!='or tokens[i+1] == '=='
            if i < final and atribuicao_declaracao_variavel_logica(tokens) and not relacional:
                i += 1
                recursions_value = True
                if i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                    recursions_value = False
                    while i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                        i += 1
                        if i < final:
                            recursions_value = atribuicao_declaracao_variavel_expressao_logica(tokens)
                            i += 1
            elif i < final and atribuicao_valor_logico_relacional(tokens) and relacional:
                recursions_value = True
                while i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao_logica(tokens)
                        i += 1
                if i < final and tokens[i] == ')' and recursions_value:
                    i += 1
                    if i == final:
                        return True
                    elif i < final and tokens[i] == '{':
                        blocks += 1
                        i += 1
                        if i == final:
                            return True
                        elif i < final and tokens[i] == '}':
                            blocks -= 1
                            i += 1
                            return i == final

def funcao_de_retorno_logico_e_texto(tokens):
    global i
    global final
    if i < final and tokens[i] == 'return':
        i += 1
        if i < final and atribuicao_declaracao_variavel_logica(tokens):
            i += 1
            recursions_value = True
            if i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                recursions_value = False
                while i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao_logica(tokens)
                        i += 1
            if i < final and tokens[i] == ';' and recursions_value:
                i += 1
                return i == final
    return False
def funcao_de_retorno_aritmetico(tokens):
    global i
    global final
    if i < final and tokens[i] == 'return':
        i += 1
        if i < final and atribuicao_declaracao_variavel(tokens):
            i += 1
            recursions_value = True
            if i < final and(tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                recursions_value = False
                while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                        i += 1
            if i < final and tokens[i] == ';' and recursions_value:
                i += 1
                return i == final
    return False

def atribuicao_de_valor_array(tokens):
    global i
    global final
    if i < final and tokens[i] == 'ID':
        i += 1
        if i < final and tokens[i] == '[':
            i += 1
            if i < final and atribuicao_declaracao_variavel(tokens):
                i += 1
                recursions_value = True
                if i < final and(tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                    recursions_value = False
                    while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                        i += 1
                        if i < final:
                            recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                            i += 1
                if i < final and tokens[i] == ']' and recursions_value:
                    i += 1
                    if i < final and tokens[i] == '=':
                        i += 1
                        if i < final and atribuicao_declaracao_variavel(tokens):
                            i += 1
                            recursions_value = True
                            if i < final and(tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                                recursions_value = False
                                while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                                    i += 1
                                    if i < final:
                                        recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                                        i += 1
                            if i < final and tokens[i] == ';' and recursions_value:
                                i += 1
                                return i == final
    return False                                
def declaracao_de_variavel_array(tokens): 
    global i
    global final
    if i < final and tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == '[':
                i += 1        
                if i < final and tokens[i] == ']':
                    i += 1
                    if i < final and tokens[i] == ';':
                        i += 1
                        return i == final

    return False

def atribuicao_de_valor_logico(tokens):
    global i
    global final
    if i < final and tokens[i] == 'ID':
        i += 1
        if i < final and (tokens[i] == '='):
            i += 1
            if i < final and atribuicao_declaracao_variavel_expressao_logica(tokens):
                i += 1
                if i < final and tokens[i] == ';':
                    i += 1
                    return i == final
                recursions_value = False
                while i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao_logica(tokens)
                        i += 1
                if i < final and tokens[i] == ';' and recursions_value:
                    i += 1
                    return i == final
            elif i < final and atribuicao_declaracao_variavel_expressao(tokens):
                i += 1
                if i < final and tokens[i] == ';':
                    i += 1
                    return i == final
                while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                        i += 1
                if i < final and tokens[i] == ';' and recursions_value:
                    i += 1
                    return i == final


    return False
def atribuicao_de_valor_aritmetico(tokens):
    global final
    global i
    if i < final and tokens[i] == 'ID':
        i += 1
        if i < final and (tokens[i] == '=' or tokens[i] == '+=' or tokens[i] == '-=' or tokens[i] == '/=' or tokens[i] == '*=' or tokens[i] == '%=' or tokens[i] == '&&=' or tokens[i] == '||='):
            i += 1
            if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                i += 1
                if i < final and tokens[i] == ';':
                    i += 1
                    return i == final
                recursions_value = False
                while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                    i += 1
                    if i < final:
                        recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                        i += 1
                if i < final and tokens[i] == ';' and recursions_value:
                    i += 1
                    return i == final
    return False

def declaracao_texto(tokens):
    global final
    global i
    if i < final and tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == ';':
                i += 1
                return i == final
            elif i < final and tokens[i] == '=':
                i += 1
                if i < final and tokens[i] == 'TEXTO':
                    i += 1
                    if i < final and tokens[i] == ';':
                        i += 1
                        return i == final
                    else:
                        loop_validation = False
                        while i < final:
                            if i < final and tokens[i] == ';':
                                break
                            if i < final and tokens[i] == '+':
                                loop_validation = False
                            elif i < final and tokens[i] == 'TEXTO':
                                loop_validation = True
                            i += 1
                        if i < final and loop_validation and tokens[i] == ';':
                            i += 1
                            return i == final
                                                    
def declaracao_de_variavel_logica_relacional(tokens):
    global i
    global final
    if i < final and tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == ';':
                i += 1
                return i == final
            elif i < final and tokens[i] == '=':
                i += 1
                if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                    i += 1 
                    if i < final and (tokens[i] == '>' or tokens[i] == '>=' or tokens[i] == '<' or tokens[i] == '<=' or tokens[i] == '!='or tokens[i] == '=='):
                        i += 1
                        if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                            i += 1
                            if i < final and (tokens[i] == '||' or tokens[i] == '&&'):
                                i += 1
                                return atribuicao_valor_logico_relacional(tokens)
                            if i < final and tokens[i] == ';':
                                i += 1
                                return i == final
    return False
def atribuicao_valor_logico_relacional(tokens):
    global final, i
    if i < final and atribuicao_declaracao_variavel_expressao(tokens):
        i += 1 
        if i < final and (tokens[i] == '>' or tokens[i] == '>=' or tokens[i] == '<' or tokens[i] == '<=' or tokens[i] == '!='or tokens[i] == '=='):
            i += 1
            if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                i += 1                   
                return True
    return False
def expressao_logica_composta(tokens):
    global i 
    global final
    if i < final and (tokens[i] == '||' or tokens[i] == '&&'):
        i += 1
        if i < final and tokens[i] == '!':
            i += 1

        if i < final and atribuicao_declaracao_variavel_expressao(tokens):
            i += 1
            if i < final and (tokens[i] == '>' or tokens[i] == '>=' or tokens[i] == '<' or tokens[i] == '<=' or tokens[i] == '!='or tokens[i] == '=='):
                i += 1
                if i < final and atribuicao_declaracao_variavel_expressao(tokens):
                    i += 1
                    return True
        elif i < final and atribuicao_declaracao_variavel_expressao_logica(tokens):
            i += 1
            return True


def atribuicao_declaracao_variavel_expressao_logica_complexa(tokens):
    global i 
    global final
    if i < final and tokens[i] == '(':
        i += 1
        result = False
        while i < final and tokens[i] != ')':
            if i < final and tokens[i] == '!':
                i += 1
            if i < final and (tokens[i] == 'Logic_value'or tokens[i] == 'ID'):
                i += 1
                if i < final and tokens[i] == ')':
                    result = True
                elif i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                    i += 1
                    result = False
            elif i < final and tokens[i] == '(':
                if atribuicao_declaracao_variavel_expressao_logica_complexa(tokens):
                    i += 1
                    result = True
            else:
                break
    return result or False
def atribuicao_declaracao_variavel_expressao_logica(tokens):  
    global i
    global final
    if i < final and tokens[i] == '!':
        i += 1
    if i < final and (tokens[i] == 'Logic_value' or tokens[i] == 'ID'):
        if i+1 < final and(tokens[i+1] == '&&' or tokens[i+1] == '||'):
            i += 2
            return atribuicao_declaracao_variavel_expressao_logica(tokens)
        return True
    elif i < final and tokens[i] == '(':
        return atribuicao_declaracao_variavel_expressao_logica_complexa(tokens)
    return False    

def atribuicao_declaracao_variavel_logica(tokens):
    global i
    global final
    if i < final and tokens[i] == '!':
        i += 1
    if i < final and (tokens[i] == 'ID' or tokens[i] == 'Logic_value'):
        if i+1 < final and (tokens[i+1] == '||' or tokens[i+1] == '&&'):
            i += 2
            return atribuicao_declaracao_variavel_expressao_logica(tokens)
        return True
    elif i < final and tokens[i] == '(':
        return atribuicao_declaracao_variavel_expressao_logica(tokens)
    return False
def declaracao_de_variavel_logica(tokens):
    global final
    global i
    if i < final and tokens[i] == 'Tipo':
        i += 1
        if i < final and tokens[i] == 'ID':
            i += 1
            if i < final and tokens[i] == ';':
                i += 1
                return i == final
            elif i < final and tokens[i] == '=':
                i += 1
                if i < final and atribuicao_declaracao_variavel_logica(tokens):
                    i += 1
                    if i < final and tokens[i] == ';':
                        i += 1
                        return i == final
                    recursions_value = False
                    while i < final and (tokens[i] == '&&' or tokens[i] == '||'):
                        i += 1
                        if i < final:
                            recursions_value = atribuicao_declaracao_variavel_expressao_logica(tokens)
                            i += 1
                    if i < final and tokens[i] == ';' and recursions_value:
                        i += 1
                        return i == final
    return False
def atribuicao_declaracao_variavel_expressao_complexa(tokens):
    global i 
    global final
    if i < final and tokens[i] == '(':
        i += 1
        result = False
        while i < final and tokens[i] != ')':
            if i < final and tokens[i] == '-':
                i += 1
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
    if i < final and tokens[i] == '-':
        i += 1
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
    if i < final and tokens[i] == '-':
        i += 1
    if i < final and (tokens[i] == 'NUM_INT' or tokens[i] == 'NUM_DEC' or tokens[i] == 'ID'):
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
    if i < final and tokens[i] == 'Tipo':
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
                        return i == final
                    recursions_value = False
                    while i < final and (tokens[i] == '-' or tokens[i] == '+' or tokens[i] == '/' or tokens[i] == '%' or tokens[i] == '*'):
                        i += 1
                        if i < final:
                            recursions_value = atribuicao_declaracao_variavel_expressao(tokens)
                            i += 1
                    if i < final and tokens[i] == ';' and recursions_value:
                        i += 1
                        return i == final
    return False
def check_grammar(tokens):
    global i
    global final
    if(declaracao_texto(tokens)):
        return True
    i = 0
    if(declaracao_de_variavel(tokens)):
        return True
    i = 0
    if(declaracao_de_variavel_logica(tokens)):
        return True
    i = 0
    if(declaracao_de_variavel_logica_relacional(tokens)):
        return True
    i = 0
    if(atribuicao_de_valor_aritmetico(tokens)):
        return True
    i = 0
    if(atribuicao_de_valor_logico(tokens)):
        return True
    i = 0
    if(declaracao_de_variavel_array(tokens)):
        return True
    i = 0
    if(atribuicao_de_valor_array(tokens)):
        return True
    i = 0
    if(funcao_de_retorno_aritmetico(tokens)):
        return True
    i = 0
    if(funcao_de_retorno_logico_e_texto(tokens)):
        return True
    i = 0 
    if(condicional_basica(tokens)):
        return True
    i = 0
    if(inicializacao_array(tokens)):
        return True

    return False