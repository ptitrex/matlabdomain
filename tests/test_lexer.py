from __future__ import print_function, unicode_literals
from sphinxcontrib.mat_lexer import MatlabLexer, Token

def test_strings():
    tokens = list(MatlabLexer().get_tokens("'happy'\"happy\""))
    assert tokens[0:2] == [(Token.Literal.String, "'"), (Token.Literal.String, "happy'")]
    assert tokens[2:4] == [(Token.Literal.String, '"'), (Token.Literal.String, 'happy"')]

def test_function_names():
    tk_name, _ = zip(*MatlabLexer().get_tokens("function_name;functions;function;"))
    assert not Token.Name.Function in tk_name
