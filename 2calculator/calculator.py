import io
import math
from tokenize import TokenError
from tokenizer import TokenizeWrapper

track_var = {'e': 2.718281828459045, "PI": 3.141592653589793, "ZERO": 0}


class CalculatorException(Exception):
    def __init__(self, *arg):
        self.arg = arg


def assignment(wtok):
    result = expression(wtok)

    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            track_var[str(wtok.get_current())] = result
        else:
            raise CalculatorException(f"Expected variable after ’=’ {wtok.get_current()}")
        wtok.next()

    track_var['ans'] = result
    return result


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() in ['+', '-'] :
        operator = wtok.get_current()
        wtok.next()  # bypass +
        if operator == '+':
            result = result + term(wtok)
        else:
            result = result - term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() in ['*', '/']:
        operator = wtok.get_current()
        wtok.next()  # bypass *
        if operator == '*':
            result = result * factor(wtok)
        else:
            divisor = factor(wtok)   
            if divisor == 0:  
                raise CalculatorException("Division by zero")
            result = result / divisor
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()  # bypass (
        result = assignment(wtok)
        if wtok.get_current() == ')':
            wtok.next()  # bypass )
        else:
            raise CalculatorException("Unbalanced parentheses")

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok)
    elif wtok.get_current() == 'sin':
        wtok.next()
        result = factor(wtok)
        result = math.sin(result)
    elif wtok.get_current() == 'cos':
        wtok.next()
        result = factor(wtok)
        result = math.cos(result)
    elif wtok.get_current() == 'exp':
        wtok.next()
        result = factor(wtok)
        result = math.exp(result)
    elif wtok.get_current() == 'log':
        wtok.next()
        result = factor(wtok)
        result = math.log(result)

    elif wtok.is_name():
        if wtok.get_current() not in track_var.keys():
            raise CalculatorException(f"{wtok.get_current()} is Undefined variable")
        else:
            result = track_var[wtok.get_current()]

        if wtok.is_at_end():
             print(wtok.get_current())
        else:
            wtok.next()


    elif wtok.is_number():  # should be a number
        result = float(wtok.get_current())
        wtok.next()  # bypass the number


    else:
        raise CalculatorException(f"Expected number, name or ’(’ {wtok.get_current()}", wtok )
    return result


def statement(wtok):
    if wtok.get_current() == 'quit':
        print('Bye!')
        exit()
    elif wtok.get_current() == 'vars':
        print(track_var)
        wtok.next()

    else:
        return assignment(wtok)


def main():
    print("calculator")
    while True:
        line = input('> ').strip()
        try:
            wtok = TokenizeWrapper(line)
            result = statement(wtok)
            print('Result: ', result)
        except TokenError:
            print('Unbalanced parentheses')
        except CalculatorException as e:
            print(e)


if __name__ == "__main__":
    main()
    

			