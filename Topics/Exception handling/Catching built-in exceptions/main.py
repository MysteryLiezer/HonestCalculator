a = int(input())
b = int(input())

try:
    division = a / b
except ZeroDivisionError:
    print('The Error!')
else:
    print(division)