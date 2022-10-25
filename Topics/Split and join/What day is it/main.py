date = str(input())
new_date = date.replace('-', ' ').split(' ')
date = '\n'.join(new_date)

print(date)

