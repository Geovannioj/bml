LEXER  = [
    ('WORD', r'[a-zA-Z]+'),
    ('STRING', r'([a-zA-Z])+\d+'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    ('INTEGER',r'[^a-zA-Z\s\W]\d+'),
    ('EQUAL',r'='),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('TEXT', r'\"[\S\s]+\"'),
    ('COMMENT_INLINE', r'\/\/'),
]
