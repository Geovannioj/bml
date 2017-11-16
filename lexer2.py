import ox

lexer = ox.make_lexer([
    ('ROOT', r'^.'),
    ('TAG', r'[a-zA-Z]+\('),
    ('C_BRACKET', r'\)'),
    ('PARAMETER', r'[a-z]+=\"[a-zA-Z0-9 ]*\"'),
    ('COMMA', r','),
    
])

tokens = ['ROOT', 'TAG', 'C_BRACKET', 'PARAMETER', 'COMMA']

st = input('expr: ')
tokens = lexer(st)
print('tokens:', tokens)
