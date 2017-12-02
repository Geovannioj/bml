import ox
import re
from lexer_rules import LEXER


whitespace = re.compile(r'^\s*')
line_lexer = ox.make_lexer(LEXER)

def my_lexer(src):
    stack = [0]
    for line in src.split('\n'):
        yield ox.Token('NEWLINE',r'\n')
        m = whitespace.match(line).span(0)[1]
        if m > stack[-1]:
            # espacos += 1
            yield ox.Token('INDENT', m)
            stack.append(m)
        elif m < stack[-1]:
            contador = 0
            for i in reversed(stack[:-1]):
                yield ox.Token('DEDENT', i)
                if m == i:
                    stack.pop()
                    contador = 0
                    break
                else:
                    contador = 1
            if contador:
                raise(TypeError)
        else:
            pass

        yield from line_lexer(line)

f = open("entrada.bml", "r")
tokens = list(my_lexer(f.read()))
print('tokens:', tokens)




tokens_list = [
    'WORD',
    'INDENT',
    'DEDENT',
    'STRING',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'INTEGER',
    'EQUAL',
    'COMMA',
    'DOT',
    'TEXT',
    'COMMENT_INLINE'
    ]
parser = ox.make_parser([


    #Nomes em MAIUSCULO sao os TOKENS definidos e achados no lexer.
    #Precisamos mudar o lexer para ATOMIZAR mais os achados.
    #Deixar de fazer o papel do parser durante o lexer. (Isso simplifica o lexer)
    #Entretanto, o parser vai ficar maior. (Dica do prof)


    ('block : NEWLINE INDENT stms DEDENT', lambda a,b,c,d: c),
    ('stms : stm', lambda x: [x]),
    ('stms : stm NEWLINE smts', lambda x, y: [x] + y),
    ('stm : block', lambda x: x),
    ('stm : expr', lambda x: x),

    ('expr : TAG OPEN_PAREN args CLOSE_PAREN ', lambda a,b,c,d : [a, c]),
    ('expr : tag', lambda x: x),
    ('args : arg COMMA args', lambda a,b,c: [a] + c),
    ('args : arg', lambda x: [x]),
    ('arg : STRING value', lambda a,b: (a,b)),

    ('value : EQUAL INTEGER', lambda a,b: int(b)),
    ('value : EQUAL STRING', lambda a,b: str(b)),
    ('tag : WORD', lambda a: a)
], tokens_list)

ast = parser(tokens)
print('AST:', ast)
