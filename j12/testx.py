from random import *


def rps(x):
    c_score, u_score, tie = 0
    valid = ["سنگ", "کاغذ", "قیچی"]
    c_choice = choice(valid)
    if x == c_choice:
        tie += 1
        return f"computer choose {c_choice} and you choose {x} tie"
    elif x == valid[0] and c_choice == valid[1]:
        c_score += 1
        return f"computer choose {c_choice} and you choose {x} lose"
    elif x == valid[1] and c_choice == valid[2]:
        c_score += 1
        return f"computer choose {c_choice} and you choose {x} lose"
    elif x == valid[2] and c_choice == valid[0]:
        c_score += 1
        return f"computer choose {c_choice} and you choose {x} lose"
    else:
        if x in valid:
            return f"computer choose {c_choice} and you choose {x} win"
            u_score += 1
        else:
            return "invalid input"

print(rps("rock"))