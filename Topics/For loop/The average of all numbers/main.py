a = int(input())
b = int(input())

a = a - (a % -3)
r = range(a, b + 1, 3)
print(sum(r) / len(r))