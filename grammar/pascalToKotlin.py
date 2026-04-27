from lark import Lark, Transformer

class PascalToKotlin(Transformer):
    def INT(self, val):
        return str(val)
    def NUMBER(self, val):
        return str(val)
    def STRING(self, val):
        return '"' + str(val)[1:-1] + '"'
    def arg_list(self, childern):
        result = ", ".join(childern)
        return f"({result})"
    def NAME(self, name):
        if str(name).lower() == "writeln":
            newname = "println"
        else:
            newname = str(name)
        return newname
    def proc_call(self, childern):
        return f"{childern[0]}{childern[1]}"
    def func_call(self, childern):
        return f"{childern[0]}{childern[1]}"
    def statement(self, childern):
        return "".join(childern)
    def stmt_list(self, childern):
        return "\n".join(childern)
    def block(self,childern):
        return f"fun main(args: Array<String>){{\n{childern[0]} \n}}"
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
    def program(self, childern):
        return childern[1]
    def start(self, childern):
        return childern[0]
    def add(self, childern):
        a,b = childern
        return f"{a} + {b}"
    def sub(self, childern):
        a,b = childern
        return f"{a} - {b}"
    def lvalue(self, n):
        return str(n[0])
    def assignment(self, childern):
        return f"{childern[0]} {childern[1]} {childern[2]}"
    def inner_statement(self, childern):
        return childern[0]
    def inner_stmt_list(self, childern):
        return "\n".join(childern)
    def inner_block(self, childern):
        return childern[0]
    def func_body(self, childern):
        return "\n".join(childern) + "\n"
    def TYPE(self, n):
        if str(n).lower() == "integer":
            return "Int"
        else:
            return str(n)
    def name_list(self, childern):
        lista = ", ".join(childern)
        return str(lista)
    def param_decl(self,childern):
        variables = str(childern[0]).split(", ")
        variables = [variable + f": {childern[1]}" for variable in variables]
        result = ", ".join(variables)
        return result

    def param_list(self, childern):
        lista = ", ".join(childern)
        return str(lista)

    def function_decl(self,childern):
        name = str(childern[0])
        if len(childern) == 3:
            args = ""
            returntype = childern[1]
            body = str(childern[2])
        else:
            args = childern[1]
            returntype = childern[2]
            body = str(childern[3])

        if f"{name} = " in body:
            body = body.replace(f"{name} =", "return")
        return f"fun {name}({args}): {returntype}{{\n{body}}}"
    def var_decl(self,childern):
        variables = str(childern[0]).split(", ")
        variables = ["var " + variable + f": {childern[1]}" for variable in variables]
        result = "\n".join(variables)
        return result
    def var_section(self,childern):
        return childern[0]
    def const_decl(self, childern):
        return f"val {childern[0]} = {childern[1]}"
    def const_section(self,childern):
        return "\n".join(childern)
    def assign(self,childern):
        return "="
    def add_assign(self,childern):
        return "+="
    def sub_assign(self,childern):
        return "-="
    def div_assign(self, childern):
        return "/="
    def mul_assign(self, childern):
        return "*="
    def gt(self,childern):
        return f"{childern[0]} > {childern[1]}"
    def if_stmt(self, childern):
        lista1 = childern[1].replace("\n", "\n\t")
        result = f"if ({childern[0]}){{\n\t{lista1}\n}}"
        if len(childern) == 3:
            lista2 = childern[2].replace("\n", "\n\t")
            result += f"\nelse{{\n\t{lista2}\n}}"
        return result
    def basic_statement(self,childern):
        return "\n".join(childern)




if __name__ == "__main__":
    with open("../test/pascal_code2.pas", "r") as f:
        pascal_code = f.read()

    parser = Lark.open("grammar.lark", parser="lalr", rel_to=__file__)
    tree = parser.parse(pascal_code)
    result = PascalToKotlin().transform(tree)

    print(result)