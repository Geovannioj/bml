class Lexer():

    """
    _rules e o dicionario que recebe as regras do nosso lexer.
    """

    _rules = {
        'WORD' : r'[a-zA-Z]+',
        'STRING' :  r'([a-zA-Z])+\d+',
        'OPEN_PAREN' :  r'\(',
        'CLOSE_PAREN' :  r'\)',
        'INTEGER' : r'[^a-zA-Z\s\W]\d+',
        'EQUAL' : r'=',
        'COMMA' : r',',
        'DOT' :  r'\.',
        'TEXT' :  r'\"[\S\s]+\"',
        'COMMENT_INLINE' : r'\/\/'
    }

    #transforma o dicionario em uma lista de tuplas,
    rules = _rules.items()

    #retorna a lista de tokens
    token_list = list(_rules.keys())
