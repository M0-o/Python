def compute_result(a, b, operator):
    if operator == "+":
        return str(int(a) + int(b))
    return str(int(a) - int(b))

def arithmetic_arranger(problems, result=False):

    first = []
    second=[]
    op=[]

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if "+" not in problem and "-" not in problem:
            return "Error: Operator must be '+' or '-'."
        operand1,operator,operand2 = problem.split(" ")

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        first.append(operand1)
        op.append(operator)
        second.append(operand2)

    line1 = ""
    line2 = ""
    dashes =""
    results =""
    for i in range(len(problems)):
        line2 += op[i] + " "
        char_num = max(len(first[i]), len(second[i])) + 2
        calc = compute_result(first[i], second[i], op[i])
        calc = " " * (char_num - len(calc)) + calc
        if len(first[i]) <= len(second[i]):
            line1 += " " * (len(second[i]) - len(first[i]) + 2)
            line2 += " " * (len(first[i]) - len(second[i]))
        else:
            line1 += " " * 2
            line2 += " " 

        line1 += first[i]
        line2 += second[i]
        if i == len(problems) - 1:
            dashes += "-" * char_num
            results += calc
            break
        line1 += " " * 4
        line2 += " " * 4
        dashes += "-" * char_num + " " * 4
        results += calc + " " * 4

    return line1 + "\n" + line2 + "\n" + dashes + ("\n" + results if result else "");


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True))