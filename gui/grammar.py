from lark import Lark
import json

class Grammar:
    def __init__(self, grammar_file, java_ganerator=None, kotlin_generator=None):
        self.parser = Lark.open(f"../{grammar_file}", parser="lalr", rel_to=__file__)
        self.parserK = Lark.open(f"../grammar/kotlin.lark", parser="lalr", rel_to=__file__)
        with open("grammar/pascal_grammar.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        with open("grammar/kotlin_grammar.json", "r", encoding="utf-8") as f:
            self.data_k = json.load(f)
        self.java_ganerator = java_ganerator
        self.kotlin_generator = kotlin_generator
        self.file_content = None
        self.decision_tree = None

    def load(self, path):
        with open(path, "r") as f:
            self.file_content = f.read()
        return self.file_content

    def get_tokens(self):
        if self.file_content:
            return [(t.type, t.line, t.column-1, len(t.value)+t.column-1) for t in self.parser.lex(self.file_content)]
        else:
            raise Exception("File not loaded!")
    def get_tokens_k(self, file_content):
        if file_content:
            return [(t.type, t.line, t.column - 1, len(t.value) + t.column - 1) for t in self.parserK.lex(file_content)]
        else:
            raise Exception("Empty content!")


    def get_data(self):
        return self.data
    def get_data_k(self):
        return self.data_k
    def make_tree(self):
        if self.file_content:
            self.decision_tree = self.parser.parse(self.file_content)
        else:
            raise Exception("File not loaded!")

    def get_java(self):
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.java_ganerator:
            return self.java_ganerator().transform(self.decision_tree)
        return self.file_content

    def get_kotlin(self):
        if not self.decision_tree:
            raise Exception("Decision tree missing!")

        if self.kotlin_generator:
            return self.kotlin_generator().transform(self.decision_tree)
        return self.file_content
