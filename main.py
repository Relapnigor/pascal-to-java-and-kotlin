from gui.grammar import Grammar
from gui.modernApp import ModernApp2
from grammar.pascalToKotlin import PascalToKotlin
from grammar.pascalToJava import PascalToJava


grammar = Grammar("grammar/grammar.lark", java_ganerator=PascalToJava, kotlin_generator=PascalToKotlin)
app = ModernApp2(grammar)
app.run()