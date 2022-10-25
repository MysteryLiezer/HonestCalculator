msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0
answer = ""
cont = ""
bacon = True

def check(x,y,oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y) == True:
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)

def is_one_digit(v):
    if (v > -10 and v < 10) and v.is_integer() == True:
        output = True
    else:
        output = False
    return output

while bacon == True:
    cont = ""
    print(msg_0)
    (x, oper, y) = input().split()
    if x == 'M':
        x = str(memory)
    if y == 'M':
        y = str(memory)

    if x.isalpha() or y.isalpha():
        print(msg_1)
    elif oper not in ["+", "-", "*", "/"]:
        print(msg_2)
    else:
        x = float(x)
        y = float(y)
        check(x, y, oper)
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/" and y != 0:
            result = x / y
        else:
            print(msg_3)
            continue
        print(result)
        answer = ""

        while answer == "":
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result) == True:
                    msg_index = 10
                    print(msg_10)
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            print(msg_11)
                            answer = input()
                            if answer == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                    print(msg_12)
                                    answer = input()
                                    if answer == "y":
                                        memory = result
                        else:
                            memory = result
                            break
                else:
                    memory = result
            elif answer == "n":
                break
            else:
                answer = ""

        while cont == "":
            print(msg_5)
            cont = input()
            if cont == "y":
                break
            elif cont == "n":
                bacon = False
            else:
                cont == ""





