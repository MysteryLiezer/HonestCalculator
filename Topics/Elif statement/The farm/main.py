money = int(input())

if money < 23:
    print(None)
elif money < 678:
    n_chickens = money // 23
    if n_chickens == 1:
        print(n_chickens, "chicken")
    else:
        print(n_chickens, "chickens")
elif money < 1296:
    n_goats = money // 678
    if n_goats == 1:
        print(n_goats, "goat")
    else:
        print(n_goats, "goats")
elif money < 3848:
    n_pigs = money // 1296
    if n_pigs == 1:
        print(n_pigs, "pig")
    else:
        print(n_pigs, "pigs")
elif money < 6769:
    n_cows = money // 3848
    if n_cows == 1:
        print(n_cows, "cow")
    else:
        print(n_cows, "cows")
else:
    n_sheep = money // 6769
    print(n_sheep, "sheep")