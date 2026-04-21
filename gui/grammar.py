from lark import Lark

class Grammar:
    def __init__(self):
        self.parser = Lark.open("../grammar/grammar.lark", parser="lalr", rel_to=__file__)

    def get_tokens(self, path):
        with open(path, "r") as f:
            pascal_code = f.read()
        return [(t.type, t.line, t.column-1, len(t.value)+t.column-1) for t in self.parser.lex(pascal_code)]