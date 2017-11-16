from pygments.lexer import RegexLexer
from pygments.token import *

class BmlLexer(RegexLexer):
    
    tokens = {
        'root': [
            (r'^.', Text),
            (r'[a-zA-Z]+(', 'tag')
            
        ],
        'tag': [
            (r')', 'tag'),
            (r'[a-Z]+=\"[a-Z]\"+(, [a-Z]+=\"[a-Z]\"+)*', "tag" ),
        ]
        
    }