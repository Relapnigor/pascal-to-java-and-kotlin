from lark import Transformer

class PascalToJava(Transformer):

    # Tokens

    def INT(self, val):
        return str(val)

    def NUMBER(self, val):
        return str(val)

    def STRING(self, val):
        return '"' + str(val)[1:-1] + '"'

    def NAME(self, name):
        if str(name).lower() == "writeln":
            return "System.out.println"
        if str(name).lower() == "write":
            return "System.out.print"
        if str(name).lower() == "readln":
            return "scanner.nextLine"
        if str(name).lower() == "read":
            return "scanner.next"
        return str(name)

    def TYPE(self, n):
        mapping = {
            "integer": "int",
            "real":    "double",
            "string":  "String",
            "char":    "char",
            "boolean": "boolean",
        }
        return mapping.get(str(n).lower(), str(n))

    # Expressions

    def add(self, c):   return f"{c[0]} + {c[1]}"
    def sub(self, c):   return f"{c[0]} - {c[1]}"
    def mul(self, c):   return f"{c[0]} * {c[1]}"
    def div(self, c):   return f"{c[0]} / {c[1]}"
    def int_div(self, c): return f"(int)({c[0]} / {c[1]})"
    def mod(self, c):   return f"{c[0]} % {c[1]}"
    def neg(self, c):   return f"-{c[0]}"
    def pow(self, c):   return f"Math.pow({c[0]}, {c[1]})"

    # Conditions

    def gt(self, c):  return f"{c[0]} > {c[1]}"
    def lt(self, c):  return f"{c[0]} < {c[1]}"
    def eq(self, c):  return f"{c[0]} == {c[1]}"
    def ge(self, c):  return f"{c[0]} >= {c[2]}"
    def le(self, c):  return f"{c[0]} <= {c[2]}"
    def ne(self, c):  return f"{c[0]} != {c[2]}"
    def and_(self, c): return f"{c[0]} && {c[1]}"
    def or_(self, c):  return f"{c[0]} || {c[1]}"
    def not_(self, c): return f"!({c[0]})"

    def and_cond_rule(self, c): return self.and_(c)
    and_ = lambda self, c: f"{c[0]} && {c[1]}"
    or_  = lambda self, c: f"{c[0]} || {c[1]}"
    not_ = lambda self, c: f"!({c[0]})"
    locals()["and"] = lambda self, c: f"{c[0]} && {c[1]}"
    locals()["or"]  = lambda self, c: f"{c[0]} || {c[1]}"
    locals()["not"] = lambda self, c: f"!({c[0]})"

    # Assignment operators

    def lvalue(self, n):      return str(n[0])
    def array_access(self, c): return f"{c[0]}[{c[1]}]"

    def assign(self, c):      return "="
    def add_assign(self, c):  return "+="
    def sub_assign(self, c):  return "-="
    def mul_assign(self, c):  return "*="
    def div_assign(self, c):  return "/="

    def post_inc(self, c): return f"{c[0]}++;"
    def post_dec(self, c): return f"{c[0]}--;"
    def pre_inc(self, c):  return f"++{c[1]};"
    def pre_dec(self, c):  return f"--{c[1]};"

    # Calls

    def arg_list(self, c):
        return "(" + ", ".join(c) + ")"

    def proc_call(self, c):
        args = c[1] if len(c) > 1 else "()"
        return f"{c[0]}{args};"

    def func_call(self, c):
        args = c[1] if len(c) > 1 else "()"
        return f"{c[0]}{args}"

    # Statements

    def assignment(self, c):
        return f"{c[0]} {c[1]} {c[2]};"

    def return_statement(self, c):
        return f"return {c[0]};"

    def break_stmt(self, c):
        return "break;"

    def continue_stmt(self, c):
        return "continue;"

    def if_stmt(self, c):
        cond = c[0]
        then = _indent(c[1])
        result = f"if ({cond}) {{\n{then}\n}}"
        if len(c) == 3:
            else_ = _indent(c[2])
            result += f" else {{\n{else_}\n}}"
        return result

    def while_stmt(self, c):
        body = _indent(c[1])
        return f"while ({c[0]}) {{\n{body}\n}}"

    def for_stmt(self, c):
        var   = c[0]
        start = c[2]
        end   = c[3]
        body  = _indent(c[4])
        return f"for (int {var} = {start}; {var} <= {end}; {var}++) {{\n{body}\n}}"

    def repeat_statement(self, c):
        body = _indent(c[0])
        cond = c[1]
        return f"do {{\n{body}\n}} while (!({cond}));"

    def case_label(self, c):
        return str(c[0])

    def case_label_list(self, c):
        return list(c)
    def case_branch(self, c):
        labels = c[0]
        stmt   = c[1]
        cases  = "\n".join(f"case {lbl}:" for lbl in labels)
        return f"{cases}\n{_indent(stmt)}\nbreak;"

    def case_else(self, c):
        return f"default:\n{_indent(c[0])}\nbreak;"

    def case_statement(self, c):
        expr    = c[0]
        branches = "\n".join(c[1:])
        return f"switch ({expr}) {{\n{_indent(branches)}\n}}"

    # Statement lists / blocks

    def basic_statement(self, c):
        return "\n".join(c)

    def inner_statement(self, c):
        return c[0]

    def inner_stmt_list(self, c):
        return "\n".join(c)

    def inner_block(self, c):
        return c[0]

    def statement(self, c):
        return "".join(c)

    def stmt_list(self, c):
        return "\n".join(c)

    def block(self, c):
        body = _indent(c[0])
        return f"public static void main(String[] args) {{\n{body}\n}}"

    # Declarations

    def name_list(self, c):
        return ", ".join(c)

    def param_decl(self, c):
        variables = str(c[0]).split(", ")
        jtype = c[1]
        return ", ".join(f"{jtype} {v}" for v in variables)

    def param_list(self, c):
        return ", ".join(c)

    def array_type(self, c):
        return f"{c[2]}[]"

    def var_decl(self, c):
        variables = str(c[0]).split(", ")
        jtype = c[1]
        if isinstance(jtype, str) and jtype.endswith("[]"):
            base = jtype[:-2]
            size = None
            lines = [f"{jtype} {v} = new {base}[0]" for v in variables]
        else:
            lines = [f"{jtype} {v}" for v in variables]
        return ";\n".join(lines) + ";"

    def var_section(self, c):
        return c[0]

    def const_decl(self, c):
        return f"static final var {c[0]} = {c[1]};"

    def const_section(self, c):
        return "\n".join(c)

    def func_body(self, c):
        return "\n".join(c) + "\n"

    def function_decl(self, c):
        name       = str(c[0])
        if len(c) == 3:
            params     = ""
            returntype = c[1]
            body       = str(c[2])
        else:
            params     = c[1]
            returntype = c[2]
            body       = str(c[3])

        if f"{name} = " in body:
            body = body.replace(f"{name} =", "return")

        body_indented = _indent(body.rstrip())
        return f"public static {returntype} {name}({params}) {{\n{body_indented}\n}}"

    def procedure_decl(self, c):
        name = str(c[0])
        if len(c) == 2:
            params = ""
            body   = str(c[1])
        else:
            params = c[1]
            body   = str(c[2])

        body_indented = _indent(body.rstrip())
        return f"public static void {name}({params}) {{\n{body_indented}\n}}"

    # Top-level

    def program_block(self, c):
        statics = []
        rest = []

        for item in c:
            if isinstance(item, tuple) and item[0] in ("VAR_SECTION", "CONST_SECTION"):
                statics.append(item[1])
            else:
                rest.append(_indent_method(item))

        parts = statics + rest
        return "\n\n".join(parts)

    def program(self, c):
        prog_name = str(c[0])
        body      = c[1]
        body_indented = _indent(body)
        return (
            f"public class {prog_name} {{\n"
            f"{body_indented}\n"
            f"}}"
        )

    def start(self, c):
        return c[0]

def _indent(text: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else line
                     for line in text.split("\n"))

def _indent_method(text: str, spaces: int = 4) -> str:
    return _indent(text, spaces)
