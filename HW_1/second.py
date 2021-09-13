def min_3():
    from random import choice
    tot = 0
    for i in range(10):
        string = ""
        while "H H H" not in string and "T T T" not in string:
            string += choice(["H", "T"]) + " "
        tot += len(string)//2
        print(f"{string} ({len(string)//2} flips)")
    return tot/10

print(f"\nOn average, {min_3()} flips were needed.")