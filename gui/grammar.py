from lark import Lark
from grammar.SemanticChecker import SemanticChecker
import sys
import os

def resource_path(relative_path):
    """ Zwraca ścieżkę do zasobu"""
    if hasattr(sys, '_MEIPASS'):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

class Grammar:
    """
    Klasa do obsługi gramatyki,
    jest wykorzystywana przez GuiApp
    """
    def __init__(self, grammar_file, semantic_checker, java_ganerator=None, kotlin_generator=None):
        """
        wczytwanie plikiów gramatyki dla pascala, javy i kotlina
        przypisywane są generatory kodu do javi i kotlina

        :param grammar_file: plik w którym jest prawidłowo zdefiniowana gramatyka w lark do Pascala
        :param java_ganerator: klasa odpowidzialna za przekształacanie pascala na jave
        :param kotlin_generator: klasa odpowidzialna za przekształacanie pascala na jave
        """
        self.parser = Lark.open(resource_path("grammar/grammar.lark"), parser="lalr")
        self.parserKotlin = Lark.open(resource_path("grammar/kotlin.lark"), parser="lalr")
        self.parserPascal = Lark.open(resource_path("grammar/pascal.lark"), parser="lalr")
        self.parserJava = Lark.open(resource_path("grammar/java.lark"), parser="lalr")
        self.java_ganerator = java_ganerator()
        self.kotlin_generator = kotlin_generator()
        self.decision_tree = None
        self.checker = semantic_checker()

    def get_pascal_tokens(self, content):
        """
        zwaraca tokeny Pascala potrzebne do kolorwania składni

        :param content: tekst pascala
        :return: lista tokenów (type, line, column, end_column)
        """
        if not content:
            raise Exception("No content to parse!")

        return [(t.type, t.line, t.column-1, len(t.value)+t.column-1) for t in self.parserPascal.lex(content)]


    def get_kotlin_tokens(self, content):
        """
         zwaraca tokeny Kotlina potrzebne do kolorwania składni

        :param content: tekst kotlina
        :return: lista tokenów (type, line, column, end_column)
        """
        if not content:
            raise Exception("No content to parse!")

        return [(t.type, t.line, t.column - 1, len(t.value) + t.column - 1) for t in self.parserKotlin.lex(content)]

    def get_java_tokens(self, content):
        """
        zwraca tokeny Javy potrzebne do kolorowania składni

        :param content: tekst java
        :return: lista tokenów (type, line, column, end_column)
        """

        if not content:
            raise Exception("No content to parse!")

        return [(t.type, t.line, t.column - 1, len(t.value) + t.column - 1) for t in self.parserJava.lex(content)]

    def make_tree(self, content):
        """
        tworzy drzewo składniowe na postawie paramtru content

        :param content: tekst w pascalu
        """
        if not content:
            raise Exception("No content to parse!")

        self.decision_tree = self.parser.parse(content)

        self.checker.check_types(self.decision_tree)
        self.checker.check_breaks(self.decision_tree)


    def get_java(self):
        """
        zamienia pascala na jave jesli klasa posiada generator dla javy
        w przeciwnym razie 'error'

        :return: kod w javie
        """
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.java_ganerator:
            return self.java_ganerator.transform(self.decision_tree)
        return "error"

    def get_kotlin(self):
        """
        zamienia pascala na Kotlina jesli klasa posiada generator dla Kotlina
        w przeciwnym razie 'error'

        :return: kod w Kotlinie
        """
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.kotlin_generator:
            return self.kotlin_generator.transform(self.decision_tree)
        return "error"
