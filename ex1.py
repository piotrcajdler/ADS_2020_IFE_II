# my stack

my_stack = []
top_index = 0
size = 50

def is_empty(stack):
    return len(stack) == 0


def push(argument):
    global my_stack,size,top_index

    if  0 <= top_index <= size-1:
        my_stack += [argument]
        top_index += 1
        return True
    if 0 > top_index >= size:
      return False

def pop():

    global my_stack,top_index
    if is_empty(my_stack):
        return False
    else:
        a = my_stack[top_index-1]
        my_stack = my_stack[:top_index-1]
        top_index -= 1
        return a


def top():
    global my_stack,top_index
    if is_empty(my_stack):
        return False
    else: return my_stack[top_index-1]


def rpn():
    """
    RPN functions returns False when there are less than 3 indexes in
    lise and calculates using the operator 2 previous numbers
    """
    global my_stack,top_index
    if top_index - 3 < 0:
        return False
    if isinstance(my_stack[top_index-3], int) and isinstance(my_stack[top_index-2], int):

        if my_stack[top_index-1] == "+":
            (my_stack[top_index-3]) = int(my_stack[top_index-2]) + int(my_stack[top_index-3])
            my_stack = my_stack[:-2]
            top_index -= 2
        elif my_stack[top_index-1] == "-":
            my_stack[top_index - 3] = my_stack[top_index - 3] - my_stack[top_index - 2]
            my_stack= my_stack[:-2]
            top_index -= 2
        elif my_stack[top_index-1] == '*':
            my_stack[top_index - 3] = my_stack[top_index - 3] * my_stack[top_index - 2]
            my_stack = my_stack[:-2]
            top_index -= 2
        elif my_stack[top_index-1] == '/':
            my_stack[top_index - 3] = int(my_stack[top_index - 3] / my_stack[top_index - 2])
            my_stack = my_stack[:-2]
            top_index -= 2

def put_on_stack():
    global operators, out, top_ind
    out += [operators[top_ind - 1]]
    top_ind -= 1
    operators = operators[:top_ind]


def check_operator(token):

    global operators, out, top_ind

    if operators[top_ind - 1] == '+' and token == '-':
        put_on_stack()
    elif operators[top_ind - 1] == '-' and token == '+':
        put_on_stack()
    elif operators[top_ind - 1] == '-' and token == '*':
        put_on_stack()
    elif operators[top_ind - 1] == '-' and token == '/':
        put_on_stack()
    elif operators[top_ind - 1] == '+' and token == '/':
        put_on_stack()
    elif operators[top_ind - 1] == '-' and token == '-':
        put_on_stack()
    elif operators[top_ind - 1] == '+' and token == '*':
        put_on_stack()
    elif operators[top_ind - 1] == '+' and token == '+':
        put_on_stack()
    elif operators[top_ind - 1] == '*' and token == '/':
        put_on_stack()
    elif operators[top_ind - 1] == '/' and token == '*':
        put_on_stack()
    elif operators[top_ind - 1] == '*' and token == '*':
        put_on_stack()
    elif operators[top_ind - 1] == '/' and token == '/':
        put_on_stack()


def change(expression):
    global my_stack, operators, out, top_ind, operation_signs
    operation_signs = ['+','-','*','/','(',')']
    top_ind = 0
    tokens = expression.split()
    print(tokens)
    operators = []
    out = []

    for token in tokens:
        try:
            if token not in operation_signs and not token.isalpha():
                out += [int(token)]
        except ValueError:
            print("Wrong equation")
            quit(1)
        if len(operators) != 0 and token in operation_signs:
            check_operator(token)
            if token == ')':
                while len(operators) != 0:
                    out += [operators[top_ind-1]]
                    top_ind -= 1
                    operators = operators[:top_ind]
                    if operators[top_ind-1] == '(':
                        top_ind -= 1
                        operators = operators[:top_ind]
                        break
            if token != ')':
                operators += [token]
                top_ind += 1

        if len(operators) == 0 and token in operation_signs and token != ')':
            operators += [token]
            top_ind += 1

    while top_ind-1 >= 0:
        out += operators[top_ind-1]
        top_ind -= 1

    return out


def calculate():
    global my_stack, operation_signs
    equation = change(input("EQUATION: "))
    print(equation)
    try:
        for i in equation:
            push(i)
            rpn()
    except TypeError:
        print("Wrong equation")
        return 0
    if (len(my_stack) != 1) or my_stack[0] in operation_signs:
        print("WRONG EQUATION")
        my_stack = []
        quit(1)


if __name__ == "__main__":
    calculate()
    print(my_stack)
    input()
