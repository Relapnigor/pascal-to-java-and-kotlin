import re
from lark import Visitor, Tree, Token


class SemanticError(Exception):
    pass


class SemanticChecker(Visitor):
    BUILTIN = {"writeln", "write", "readln", "read", "length", "sqrt",
               "abs", "ord", "chr", "succ", "pred", "trunc", "round"}

    def __init__(self):
        self.variables = {}
        self.constants = {}
        self.functions = {}

    def var_decl(self, tree):
        """
        Rejestruje zmienne i ich typy w słowniku self.variables.
        Wywoływana dla każdego węzła var_decl w całym drzewie
        (zarówno globalnych jak i lokalnych wewnątrz funkcji).
        Przykład: 'x, y : integer' → {'x': 'integer', 'y': 'integer'}
        """
        name_list_tree = tree.children[0]
        type_node = tree.children[1]

        names = [str(child) for child in name_list_tree.children
                 if isinstance(child, Token)]

        if isinstance(type_node, Token):
            ptype = str(type_node).lower()
        else:
            ptype = "array"

        for name in names:
            self.variables[name.strip()] = ptype

    def const_decl(self, tree):
        """
        Rejestruje stałe i ich typy (wywnioskowane z wartości) w self.constants.
        Przykład: 'N = 10' → {'N': 'integer'}
        """
        name = str(tree.children[0])
        val_node = tree.children[1]
        self.constants[name] = self._infer_type(val_node)

    def function_decl(self, tree):
        """
        Rejestruje funkcje i ich typy zwracane w self.functions.
        Dzięki temu _infer_type może określić typ wywołania funkcji.
        Typ zwracany jest zawsze przedostatnim dzieckiem (przed func_body).
        Przykład: 'function Add(a,b: integer): integer' → {'Add': 'integer'}
        """
        name = str(tree.children[0])
        self.functions[name.lower()] = str(tree.children[-2]).lower()

    def check_undeclared(self, tree):
        """
        Rekurencyjnie sprawdza czy wszystkie użyte nazwy zmiennych
        są zadeklarowane w self.variables, self.constants lub self.functions.
        Wywołaj po _collect_declarations.
        """
        if isinstance(tree, Token):
            return

        if tree.data == "assignment":
            lval_tree = tree.children[0]
            lval = str(lval_tree.children[0])
            if (lval not in self.variables and
                    lval not in self.constants and
                    lval.lower() not in self.functions):
                raise SemanticError(f"Błąd: niezadeklarowana zmienna '{lval}'")

        if tree.data in ("func_call", "proc_call"):
            name = str(tree.children[0]).lower()
            if name not in self.functions and name not in self.BUILTIN:
                raise SemanticError(f"Błąd: niezadeklarowana funkcja/procedura '{name}'")

        if tree.data not in ("var_decl", "const_decl", "function_decl",
                             "procedure_decl", "param_decl", "name_list",
                             "program", "case_label"):
            for child in tree.children:
                if isinstance(child, Token) and child.type == "NAME":
                    name = str(child)
                    if (name not in self.variables and
                            name not in self.constants and
                            name.lower() not in self.functions):
                        raise SemanticError(f"Błąd: niezadeklarowana zmienna '{name}'")

        for child in tree.children:
            if isinstance(child, Tree):
                self.check_undeclared(child)

    def check_types(self, tree):
        """
        Główna metoda do sprawdzania typów.
        Pierwsze przejście zbiera wszystkie deklaracje zmiennych, stałych i funkcji.
        Drugie przejście (visit) sprawdza przypisania.
        Rozdzielenie jest konieczne bo Visitor działa bottom-up, przez co
        assignment dla zmiennych globalnych byłoby sprawdzane przed ich rejestracją.
        """
        self._collect_declarations(tree)
        self.check_undeclared(tree)
        self.visit(tree)

    def _collect_declarations(self, tree):
        """
        Rekurencyjnie przechodzi drzewo i rejestruje wszystkie deklaracje
        (var_decl, const_decl, function_decl) zanim nastąpi sprawdzanie przypisań.
        """
        if isinstance(tree, Token):
            return
        if tree.data == "var_decl":
            self.var_decl(tree)
        if tree.data == "const_decl":
            self.const_decl(tree)
        if tree.data == "function_decl":
            self.function_decl(tree)
        if tree.data == "procedure_decl":
            name = str(tree.children[0])
            self.functions[name.lower()] = "void"
        if tree.data == "param_decl":
            name_list_tree = tree.children[0]
            type_node = tree.children[1]
            names = [str(child) for child in name_list_tree.children
                     if isinstance(child, Token)]
            if isinstance(type_node, Token):
                ptype = str(type_node).lower()
            else:
                ptype = "array"
            for name in names:
                self.variables[name.strip()] = ptype
        for child in tree.children:
            if isinstance(child, Tree):
                self._collect_declarations(child)

    def assignment(self, tree):
        """
        Sprawdza czy typ wyrażenia po prawej stronie przypisania
        jest zgodny z typem zmiennej po lewej stronie.
        Rzuca SemanticError jeśli typy są niezgodne.
        Przykład: 'x := "hello"' gdzie x: integer → błąd
        """
        lval_tree = tree.children[0]
        lval = str(lval_tree.children[0])
        expr = tree.children[2]

        var_type = self.variables.get(lval)
        if var_type is None:
            return
        if var_type == "array":
            return

        expr_type = self._infer_type(expr)
        if expr_type and not self._types_compatible(var_type, expr_type):
            raise SemanticError(
                f"Błąd typów: nie można przypisać '{expr_type}' "
                f"do '{lval}' (typ '{var_type}')"
            )

    def _infer_type(self, node):
        """
        Próbuje wywnioskować typ pascalowy węzła wyrażenia.
        Obsługuje:
        - literały liczbowe całkowite (integer)
        - literały liczbowe rzeczywiste (real), w tym notację naukową
        - literały stringowe i znakowe (string)
        - literały boolean (true/false)
        - null — zwraca None (kompatybilny z każdym typem)
        - nazwy zmiennych i stałych (przez słowniki)
        - wywołania funkcji (przez self.functions)
        - negację — deleguje do typu operandu
        - złożone wyrażenia — zwraca None (brak inferencji)
        """
        if isinstance(node, Tree):
            if node.data == "func_call":
                name = str(node.children[0]).lower()
                return self.functions.get(name)
            if node.data == "neg":
                return self._infer_type(node.children[0])
            return None

        val = str(node)

        if hasattr(node, 'type'):
            if node.type == "STRING":
                return "string"
            if node.type == "BOOL":
                return "boolean"
            if node.type == "NULL":
                return None
            if node.type == "NUMBER":
                if re.match(r'^-?\d+$', val):
                    return "integer"
                return "real"
            if node.type == "NAME":
                return self.variables.get(val) or self.constants.get(val)

        if re.match(r'^-?\d+$', val):
            return "integer"
        if re.match(r'^-?\d+[\.\d+]', val):
            return "real"
        if val.startswith("'"):
            return "string"
        if val.lower() in ("true", "false"):
            return "boolean"
        if val.lower() == "null":
            return None

        return self.variables.get(val) or self.constants.get(val)

    def _types_compatible(self, var_type, expr_type):
        """
        Sprawdza czy expr_type można przypisać do zmiennej o typie var_type.
        integer i real są wzajemnie kompatybilne (Pascal to dopuszcza).
        Wszystkie inne kombinacje różnych typów są błędem.
        """
        if var_type == expr_type:
            return True
        if {var_type, expr_type} <= {"integer", "real"}:
            return True
        return False

    def check_breaks(self, tree, in_loop=False, in_case=False):
        """
        Rekurencyjnie sprawdza czy break i continue są użyte w dozwolonym miejscu.
        - break jest dozwolony wewnątrz pętli (for/while/repeat) lub case
        - continue jest dozwolony tylko wewnątrz pętli (nie w samym case)
        Rzuca SemanticError jeśli break/continue jest poza dozwolonym kontekstem.
        """
        if isinstance(tree, Token):
            return

        if tree.data in ("while_stmt", "for_stmt_up", "for_stmt_down", "repeat_statement"):
            in_loop = True

        if tree.data == "case_statement":
            for child in tree.children:
                self.check_breaks(child, in_loop=in_loop, in_case=True)
            return

        if tree.data == "break_stmt" and not in_loop and not in_case:
            raise SemanticError("Błąd: 'break' użyty poza pętlą lub instrukcją case")

        if tree.data == "continue_stmt" and not in_loop:
            raise SemanticError("Błąd: 'continue' użyty poza pętlą")

        for child in tree.children:
            self.check_breaks(child, in_loop, in_case)

    def clear(self):
        self.decision_tree = None
        self.variables = {}
        self.constants = {}
        self.functions = {}
