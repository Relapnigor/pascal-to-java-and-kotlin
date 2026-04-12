from lark import Lark

with open("pascal_code.pas", "r") as f:
    pascal_code = f.read()

parser = Lark.open("../grammar/main.lark", parser="lalr", rel_to=__file__)

tree = parser.parse(pascal_code)
print(tree.pretty())
