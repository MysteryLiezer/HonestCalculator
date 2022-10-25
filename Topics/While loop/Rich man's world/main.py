deposit = int(input())
interest = 7.1 / 100
counter = 0

while deposit < 700000:
    updated_deposit = (deposit * interest) + deposit
    deposit = updated_deposit
    counter += 1

print(counter)