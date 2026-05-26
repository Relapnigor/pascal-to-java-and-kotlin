from gui.grammar import Grammar
from gui.guiApp import GuiApp
from grammar.pascalToKotlin import PascalToKotlin
from grammar.pascalToJava import PascalToJava
from grammar.SemanticChecker import SemanticChecker


grammar = Grammar("grammar/grammar.lark",
                  semantic_checker = SemanticChecker,
                  java_ganerator=PascalToJava,
                  kotlin_generator=PascalToKotlin)
app = GuiApp(grammar)
app.run()