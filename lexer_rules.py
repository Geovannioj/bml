LEXER  = [
    ('WORD', r'\w+'),
    ('OPEN_PAREN', r'\('),
    ('CLOSE_PAREN', r'\)'),
    ('PARAMETER', r'[a-z]+=\"\w*\"'),
    ('COMMA', r','),
    ('DOT', r'\.'),
    ('TEXT', r'\"[\S\s]+\"'),
    ('COMMENT_INLINE', r'\/\/[\S\s]+'),
]
