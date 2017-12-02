LEXER  = [
    ('WORD', r'[a-zA-Z]+'),
    ('STRING', r'([a-zA-Z])+\d+'),
    # ('NEWLINE', r'\n'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    # ('PARAMETER', r'[a-z]+=\"\w*\"'),
    ('INTEGER',r'[^a-zA-Z\s]\d+'),
    ('EQUAL',r'='),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('TEXT', r'\"[\S\s]+\"'),
    ('COMMENT_INLINE', r'\/\/[\S\s]+'),
]
