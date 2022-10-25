snake_case = ''

for letter in input():
    if letter.isupper():
        snake_case += '_'
    snake_case += letter

print(snake_case.lower().lstrip('_'))
