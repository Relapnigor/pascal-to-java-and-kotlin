from gui.grammar import Grammar
from gui.modernApp import ModernApp2
from grammar.pascalToKotlin import PascalToKotlin


grammar = Grammar("grammar/grammar.lark", kotlin_generator=PascalToKotlin)
app = ModernApp2(grammar)
app.run()