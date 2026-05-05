from lark import Lark
import json

class Grammar:
    """
    Klasa do obsługi gramatyki,
    jest wykorzystywana przez GuiApp
    """
    def __init__(self, grammar_file, java_ganerator=None, kotlin_generator=None):
        """
        wczytwanie plikiów gramatyki dla pascala, javy i kotlina
        przypisywane są generatory kodu do javi i kotlina

        :param grammar_file: plik w którym jest prawidłowo zdefiniowana gramatyka w lark do Pascala
        :param java_ganerator: klasa odpowidzialna za przekształacanie pascala na jave
        :param kotlin_generator: klasa odpowidzialna za przekształacanie pascala na jave
        """
        self.parser = Lark.open(f"../{grammar_file}", parser="lalr", rel_to=__file__)
        self.parserKotlin = Lark.open(f"../grammar/kotlin.lark", parser="lalr", rel_to=__file__)
        with open("grammar/pascal_style.json", "r", encoding="utf-8") as f:
            self.pascal_style = json.load(f)
        with open("grammar/kotlin_style.json", "r", encoding="utf-8") as f:
            self.kotlin_style = json.load(f)
        self.java_ganerator = java_ganerator
        self.kotlin_generator = kotlin_generator
        self.file_content = None
        self.decision_tree = None

    def load(self, path):
        """
        wszytanie pliku zapisanie do zmiennej self.file_content
        z którego póżniej bedzie towrzone drzewo składniowe (jest to kod pascala)

        :param path: scieżka do pliku
        :return: zawartosc tekstowa pliku
        """
        with open(path, "r") as f:
            self.file_content = f.read()
        return self.file_content

    def get_pascal_tokens(self):
        """
        zwaraca tokeny Pascala potrzebne do kolorwania składni

        :return: lista tokenów (type, line, column, end_column)
        """
        if self.file_content:
            return [(t.type, t.line, t.column-1, len(t.value)+t.column-1) for t in self.parser.lex(self.file_content)]
        else:
            raise Exception("File not loaded!")

    def get_kotlin_tokens(self, file_content):
        """
         zwaraca tokeny Pascala potrzebne do kolorwania składni

        :param file_content: tekst kotlina
        :return: lista tokenów (type, line, column, end_column)
        """
        if file_content:
            return [(t.type, t.line, t.column - 1, len(t.value) + t.column - 1) for t in self.parserKotlin.lex(file_content)]
        else:
            raise Exception("Empty content!")


    def get_pascal_style(self):
        """
        zwraca tagi opisujeca w jaki sposób ma byc kolorowana skladnia  Pascala

        :return: dane z pascal_style
        """
        return self.pascal_style

    def get_kotlin_style(self):
        """
        zwraca tagi opisujeca w jaki sposób ma byc kolorowana skladnia  Kotlina

        :return: dane z kotlin_style
        """
        return self.kotlin_style

    def make_tree(self):
        """
        tworzy drzewo składniowe na postawie załadowanego pliku w Pascalu
        """
        if self.file_content:
            self.decision_tree = self.parser.parse(self.file_content)
        else:
            raise Exception("File not loaded!")

    def get_java(self):
        """
        zamienia pascala na jave jesli klasa posiada generator dla javy
        w przeciwnym razie zwraca kod zródłowy w Pascalu

        :return: kod w javie lub w pascalu
        """
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.java_ganerator:
            return self.java_ganerator().transform(self.decision_tree)
        return self.file_content

    def get_kotlin(self):
        """
        zamienia pascala na Kotlina jesli klasa posiada generator dla Kotlina
        w przeciwnym razie zwraca kod zródłowy w Pascalu

        :return: kod w Kotlinie lub w pascalu
        """
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.kotlin_generator:
            return self.kotlin_generator().transform(self.decision_tree)
        return self.file_content
