import ox
import re


whitespace = re.compile(r'^\s*')
# whitespace = re.compile(r'^\s+')
# whitespace = re.compile(r'^\s*')
line_lexer = ox.make_lexer([
    ('TAG', r'\w+'),
    ('OPEN_BRACKET', r'\('),
    ('CLOSE_BRACKET', r'\)'),
    ('PARAMETER', r'[a-z]+=\"\w*\"'),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('TEXT', r'\"[\S\s]+\"'),
    ('COMMENT_INLINE', r'\/\/[\S\s]+'),
])



def my_lexer(src):
    stack = [0]
    for line in src.split('\n'):
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

tag = lambda x: ('tag', x)
indent = lambda x: ('indent',)
tokens_list = ['TAG', 'INDENT', 'DEDENT']
parser = ox.make_parser([

    """
    Nomes em MAIUSCULO sao os TOKENS definidos e achados no lexer. 

    Precisamos mudar o lexer para ATOMIZAR mais os achados. 

    Deixar de fazer o papel do parser durante o lexer. (Isso simplifica o lexer)
    Entretanto, o parser vai ficar maior. (Dica do prof)


    """

    ('block : NEWLINE INDENT stms DEDENT', lambda a,b,c,d: c),
    ('stms : stm', lambda x: [x]),
    ('stms : stm NEWLINE smts', lambda x, y: [x] + y),
    ('stm : block', lambda x: x),
    ('stm : expr', lambda x: x),
    
    ('expr : TAG OPEN_PAREN args CLOSE_PAREN ', lambda a,b,c,d : [a, c]),
    ('args : arg', lambda x: [x]),
    ('args : arg COMMA args', lambda a,b,c: [a] + c),
    ('arg : NAME EQUAL value', lambda a,b,c: (a,c)),

    ('value : INTEGER', lambda x: int(x)),
    ('value : STRING', lambda x: str(x)),

    ('expr : tag attr', lambda x,y:...),
    ('expr : tag', lambda x: ...),
    ('attr : attr', lambda x,y: ... ),
    ('tag : tag', lambda x: ...)
], tokens_list)

ast = parser(tokens)
print('AST:', ast)