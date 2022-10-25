group_a = abs(int(input()))
group_b = abs(int(input()))
group_c = abs(int(input()))

class_a = group_a // 2 + group_a % 2
class_b = group_b // 2 + group_b % 2
class_c = group_c // 2 + group_c % 2

desks = class_a + class_b + class_c

print(desks)