import argparse
import math
import string


def div_by_zero(function):
    def wrapped(a, b):
        if b == 0:
            print("Division by zero!")
            exit()
    return wrapped


def numbers_sum(a, b):
    return a + b


def numbers_sub(a, b):
    return a - b


def numbers_mul(a, b):
    return a * b


@div_by_zero
def numbers_div(a, b):
    return a / b


@div_by_zero
def numbers_div_integer(a, b):
    return a // b


@div_by_zero
def numbers_div_mod(a, b):
    return a % b


def numbers_pow(a, b):
    return a ** b


def numbers_equal(a, b):
    return a == b


def numbers_not_equal(a, b):
    return a != b


def is_less(a, b):
    return a < b


def is_less_or_equal(a, b):
    return a <= b


def is_bigger_or_equal(a, b):
    return a >= b


def is_bigger(a, b):
    return a > b


functions = {"abs": abs, "round": round, "ceil": math.ceil, "copysign": math.copysign, "fabs": math.fabs,
             "factorial": math.factorial, "floor": math.floor, "fmod": math.fmod, "frexp": math.frexp,
             "ldexp": math.ldexp, "fsum": math.fsum, "isfinite": math.isfinite, "isinf": math.isinf,
             "isnan": math.isnan, "modf": math.modf, "trunc": math.trunc, "exp": math.exp, "expm1": math.expm1,
             "log": math.log, "log1p": math.log1p, "log10": math.log10, "log2": math.log2, "pow": math.pow,
             "sqrt": math.sqrt, "acos": math.acos, "asin": math.asin, "atan": math.atan, "atan2": math.atan2,
             "cos": math.cos, "sin": math.sin, "tan": math.tan, "hypot": math.hypot, "degrees": math.degrees,
             "radians": math.radians, "cosh": math.cosh, "sinh": math.sinh, "tanh": math.tanh, "acosh": math.cosh,
             "asinh": math.asinh, "atanh": math.atanh, "erf": math.erf, "erfc": math.erfc, "gamma": math.gamma,
             "lgamma": math.lgamma}
math_operations_prioritizes = {"+": 2, "-": 2, "/": 3, "*": 3, "//": 3, "%": 3, "^": 4, "==": 1, "!=": 1, "<": 1,
                               "<=": 1, ">=": 1, ">": 1}
math_operations = {"+": numbers_sum, "-": numbers_sub, "/": numbers_div, "*": numbers_mul, "//": numbers_div_integer,
                   "%": numbers_div_mod, "^": numbers_pow, "==": numbers_equal, "!=": numbers_not_equal, "<": is_less,
                   "<=": is_less_or_equal, ">=": is_bigger_or_equal, ">": is_bigger}
can_be_in_math_operations = ["+", "-", "/", "*", "%", "^", ">", "=", "!", "<"]
constants = {"pi": math.pi, "e": math.e}


def functions_evaluation(expression):
    function_end = 0
    function_start = 0
    elements_of_expression = []
    number, function, operand = '', '', ''  # double operands
    for index, elem in enumerate(expression):
        if elem == " ":
            print("You entered unnecessary space!")
        if function_end - function_start != 0:  # after getting arguments
            function_start += 1
            continue
        if elem in "()":
            if number != '':
                elements_of_expression.append(float(number))
                number = ''
            if operand != '' and operand in math_operations:
                elements_of_expression.append(operand)
                operand = ''
            if function != '':  # if wrong function anf next elem brackets
                print("There is no function:", function, "!")
            elements_of_expression.append(elem)
        elif (elem in "1234567890" and not function) or (elem == "." and elem not in number):
            if operand != '':
                if operand not in math_operations:
                    print("You made mistake in math operation", operand, "!")
                    exit()
                elements_of_expression.append(operand)
                operand = ''
            number += elem
        elif elem in can_be_in_math_operations:
            if number != '':
                elements_of_expression.append(float(number))
                number = ''
            if elem in '+-' and (elements_of_expression == [] or (elements_of_expression != [] and expression[index - 1]
                                                                  in math_operations)):
                # we are checking numbers because before can be more than on sign
                if operand != '':
                    if operand not in math_operations:
                        print("You made mistake in math operation", operand, "!")
                        exit()
                    elements_of_expression.append(operand)
                    operand = ''
                if expression[index + 1] in '0123456789':
                    number += elem
                elif expression[index + 1] in string.ascii_lowercase or expression[index + 1] == '(':
                    # for escaping situations such as"++"
                    elements_of_expression.append(0.0)
                    elements_of_expression.append(elem)
                else:
                    print("Something wrong with your operands!")
                    exit()
            else:
                operand += elem
        else:
            function += elem
            if function in constants:
                elements_of_expression.append(constants[function])
                function = ""
            elif function in functions:
                if expression[index + 1] != "(":
                    continue
                function_start = index
                brackets_sum = 0
                if expression[index + 1] != "(":
                    print("You made mistake in function", function, "params!")
                    exit()
                for index_1, elem_1 in enumerate(expression[function_start + 1::]):
                    if elem_1 == "(":
                        brackets_sum += 1
                    if elem_1 == ")":
                        brackets_sum -= 1
                    if brackets_sum == 0:
                        function_end = index_1 + function_start + 1
                        break
                func = functions.get(function)
                # print(get_params(expression[function_start+2:function_end]))

                try:
                    elements_of_expression.append(func(functions_evaluation(*get_params(expression[function_start + 2:
                                                                                                   function_end]))))
                except TypeError and ValueError:
                    print("You made mistake in function arguments!")
                    exit()
    if number:
        elements_of_expression.append(float(number))
    result = polish_notation_evaluation(turn_in_polish_notation(elements_of_expression))
    # print(turn_in_polish_notation(elements_of_expression))
    # print(polish_notation_evaluation(turn_in_polish_notation(elements_of_expression)))
    # print(result)
    if result is False:
        print("False in you expression!")
        exit()
    return result


def turn_in_polish_notation(elements_of_expression):
    elements_of_expression_in_polish = []
    operation_stack = []
    for elem in elements_of_expression:
        if elem in math_operations_prioritizes:
            if operation_stack and operation_stack[-1] != "(":
                if math_operations_prioritizes.get(elem) <= math_operations_prioritizes.get(operation_stack[-1]):
                    elements_of_expression_in_polish.append(operation_stack[-1])
                    operation_stack.pop()
                    operation_stack.append(elem)
                else:
                    operation_stack.append(elem)
            else:
                operation_stack.append(elem)
        elif elem == "(":
            operation_stack.append(elem)
        elif elem == ")":
            while operation_stack[-1] != "(":
                elements_of_expression_in_polish.append(operation_stack[-1])
                operation_stack.pop()
            operation_stack.pop()
        else:
            elements_of_expression_in_polish.append(elem)
    while operation_stack:
        elements_of_expression_in_polish.append(operation_stack[-1])
        operation_stack.pop()
    return elements_of_expression_in_polish


def polish_notation_evaluation(elements_of_expression_in_polish):
    count_stack = []
    for elem in elements_of_expression_in_polish:
        if isinstance(elem, float):
            count_stack.append(elem)
        elif elem in math_operations:
            function = math_operations.get(elem)
            function_result = function(count_stack[-2], count_stack[-1])
            count_stack.pop()
            count_stack.pop()
            count_stack.append(function_result)
    return count_stack[0]


def get_params(expression):
    params = []
    sum_of_brackets = 0
    function_end = 0
    function_start = 0
    for index, elem in enumerate(expression):
        if elem == "(":
            sum_of_brackets += 1
        if elem == ")":
            sum_of_brackets -= 1
        if sum_of_brackets == 0 and elem == ",":
            function_end = index + 1
            params.append(expression[function_start:function_end - 1])
            function_start = function_end  # if more than 1 var
    params.append(expression[function_end::])
    # print(params)
    return params


def checking_brackets(expression):
    sum_of_brackets = 0
    for index, elem in enumerate(expression):
        if elem == "(":
            sum_of_brackets += 1
            if expression[index + 1] == ")":
                print("You were entered empty brackets!")
                exit()
        if elem == ")":
            sum_of_brackets -= 1
            if expression[index - 1] not in "0123456789)":
                print("You were entered wrong expression in brackets!")
                exit()
        if sum_of_brackets < 0:
            print("You made mistake in count of brackets!")
            exit()
    return sum_of_brackets

def main():
    parser = argparse.ArgumentParser(description='Pure-python command-line calculator')
    parser.add_argument('EXPRESSION', type=str, help='expression string to evaluate')
    """write exception in this place!"""
    if parser.parse_args().EXPRESSION[-1] not in '0123456789)':
        print("Wrong input!")
        exit()
    if checking_brackets(parser.parse_args().EXPRESSION):
        print("You made mistake in count of brackets!")
        exit()
    print(functions_evaluation(parser.parse_args().EXPRESSION))
