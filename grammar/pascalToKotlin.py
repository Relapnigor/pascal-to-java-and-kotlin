from lark import Lark, Transformer
import re

class PascalToKotlin(Transformer):
    def BOOL(self, val):
        return str(val).lower()

    def INT(self, val):
        return str(val)

    def NUMBER(self, val):
        return str(val)

    def STRING(self, val):
        return '"' + str(val)[1:-1] + '"'

    def NAME(self, name):
        if str(name).lower() == "writeln":
            return "println"
        if str(name).lower() == "write":
            return "print"
        if str(name).lower() == "readln":
            return "readln"
        if str(name).lower() == "read":
            return "readln"
        return str(name)

    def TYPE(self, n):
        mapping = {
            "integer": "Int",
            "real": "Double",
            "string": "String",
            "char": "Char",
            "boolean": "Boolean",
        }
        return mapping.get(str(n).lower(), str(n))

    def add(self, c):   return f"{c[0]} + {c[1]}"
    def sub(self, c):   return f"{c[0]} - {c[1]}"
    def mul(self, c):   return f"{c[0]} * {c[1]}"
    def div(self, c):   return f"{c[0]} / {c[1]}"
    def int_div(self, c): return f"({c[0]} / {c[1]}).toInt()"
    def mod(self, c):   return f"{c[0]} % {c[1]}"
    def neg(self, c):   return f"-{c[0]}"
    def pow(self, c):   return f"{c[0]}.toDouble().pow({c[2]})"

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

    def lvalue(self, n):
        if len(n) == 1:
            return str(n[0])
        return f"{n[0]}[{n[1]}]"
    def array_access(self, c): return f"{c[0]}[{c[1]}]"

    def assign(self, c):      return "="
    def add_assign(self, c):  return "+="
    def sub_assign(self, c):  return "-="
    def mul_assign(self, c):  return "*="
    def div_assign(self, c):  return "/="

    def post_inc(self, c): return f"{c[0]}++"
    def post_dec(self, c): return f"{c[0]}--"
    def pre_inc(self, c):  return f"++{c[1]}"
    def pre_dec(self, c):  return f"--{c[1]}"

    def arg_list(self, c): return "(" + ", ".join(c) + ")"
    def proc_call(self, c):
        args = c[1] if len(c) > 1 else "()"
        return f"{c[0]}{args};"
    def func_call(self, c):
        args = c[1] if len(c) > 1 else "()"
        return f"{c[0]}{args}"

    def assignment(self, c): return f"{c[0]} {c[1]} {c[2]}"
    def return_statement(self, c): return f"return {c[0]}"
    def break_stmt(self, c): return "break"
    def continue_stmt(self, c): return "continue"

    def if_stmt(self, c):
        cond = c[0]
        then = self._indent(c[1])
        result = f"if ({cond}){{\n{then}\n}}"
        if len(c) == 3:
            else_body = c[2]
            if else_body.startswith("if ("):
                result += f"\nelse {else_body}"
            else:
                result += f"\nelse{{\n{self._indent(else_body)}\n}}"
        return result

    def while_stmt(self, c):
        body = self._indent(c[1])
        return f"while ({c[0]}) {{\n{body}\n}}"

    def for_stmt_up(self, c):
        var = c[0]
        start = c[2]
        stop = c[3]
        body = self._indent(c[4])
        return f"for ({var} in {start} .. {stop}) {{\n{body}\n}}"

    def for_stmt_down(self, c):
        var = c[0]
        start = c[2]
        stop = c[3]
        body = self._indent(c[4])
        return f"for ({var} in {start} downTo {stop}) {{\n{body}\n}}"

    def repeat_statement(self, c):
        body = self._indent(c[0])
        cond = c[1]
        return f"do {{\n{body}\n}} while (!({cond}));"


    def case_label(self, c):
        return str(c[0])

    def case_branch(self, c):
        label = c[0]
        stmt = c[1]
        return f"case {label}:\n{self._indent(stmt)}\n    break;"

    def case_else(self, c):
        return f"default:\n{self._indent(c[0])}\n    break;"

    def case_statement(self, c):
        expr    = c[0]
        branches = "\n".join(c[1:])
        return f"switch ({expr}) {{\n{self._indent(branches)}\n}}"

    def basic_statement(self,c): return "\n".join(c)
    def inner_statement(self, c):return c[0]
    def inner_stmt_list(self, c): return "\n".join(c)
    def inner_block(self, c): return c[0]
    def statement(self, c): return "".join(c)
    def stmt_list(self, c): return "\n".join(c)

    def block(self,c):
        return f"fun main(args: Array<String>){{\n{c[0]} \n}}"

    def name_list(self, c): return ", ".join(c)

    def param_decl(self,c):
        variables = str(c[0]).split(", ")
        variables = [v + f": {c[1]}" for v in variables]
        result = ", ".join(variables)
        return result

    def param_list(self, c): return ", ".join(c)

    def array_type(self, c):
        nums = [x for x in c if str(x) != ".."]
        start = int(str(nums[0]))
        end = int(str(nums[1]))
        size = end - start + 1
        elem = nums[2]
        return f"__ARRAY__{elem}__{size}__"

    def var_decl(self,c):
        variables = str(c[0]).split(", ")
        jtype = str(c[1])
        m = re.match(r'^__ARRAY__(.+)__(\d+)__$', jtype)
        if m:
            base = m.group(1)
            size = m.group(2)
            variables = [f"var {v}: Array<{base}> = Array({size}) {{ 0 as {base} }}" for v in variables]
        else:
            variables = [f"var {v}: {jtype}" for v in variables]
        return "\n".join(variables)

    def var_section(self,c): return c[0]

    def const_decl(self, c): return f"val {c[0]} = {c[1]}"

    def const_section(self,c): return "\n".join(c)

    def func_body(self, c): return "\n".join(c) + "\n"

    def function_decl(self,c):
        name = str(c[0])
        if len(c) == 3:
            args = ""
            returntype = c[1]
            body = str(c[2])
        else:
            args = c[1]
            returntype = c[2]
            body = str(c[3])

        if f"{name} = " in body:
            body = body.replace(f"{name} =", "return")
        return f"fun {name}({args}): {returntype}{{\n{body}}}"

    def procedure_decl(self,c):
        name = str(c[0])
        if len(c) == 2:
            args = ""
            body = str(c[1])
        else:
            args = c[1]
            body = str(c[2])

        if f"{name} = " in body:
            body = body.replace(f"{name} =", "return")
        return f"fun {name}({args}) {{\n{body}}}"


    def program_block(self, childern):
        i = 0
        if childern[0][:3] == "val":
            if childern[1][:3] == "var":
                childern[-1] = childern[-1].replace("{", f"{{\n{childern[1]}\n", 1)
                i += 1
            childern[-1] = childern[-1].replace("{", f"{{\n{childern[0]}\n",1)
            i+=1
        elif childern[0][:3] == "var":
            childern[-1] = childern[-1].replace("{", f"{{\n{childern[0]}\n",1)
            i += 1

        for index, child in enumerate(childern[i:]):
            childern[index + i] = child.replace("\n", "\n\t", child.count("\n")-1)

        lista = "\n".join(childern[i:])
        return lista

    def program(self, c): return c[1]

    def start(self, c): return c[0]

    def _indent(self, text):
        return "\t"+ text.replace("\n", "\n\t")





if __name__ == "__main__":
    with open("../test/03_petle.pas", "r") as f:
        pascal_code = f.read()

    parser = Lark.open("grammar.lark", parser="lalr", rel_to=__file__)
    tree = parser.parse(pascal_code)
    result = PascalToKotlin().transform(tree)

    print(result)