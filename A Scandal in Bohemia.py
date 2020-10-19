import re


def key(extract):
    x = extract[0:300].split()
    for z in range(0, 8850):
        y = a_scandal_in_bohemia[z:z+300].split()
        if len(x) == len(y):
            exit = 1
            for i in range(0, len(x)):
                if len(x[i]) != len(y[i]):
                    exit = 0
                    break
            if exit == 1:
                break
    encrypted_letters = []
    letters = []
    print(a_scandal_in_bohemia[z])
    if a_scandal_in_bohemia[z] == ' ' and extract[0] != ' ':
        z += 1
    for i in range(z, len(extract)):
        if extract[i-z].isalpha():
            if not extract[i-z].lower() in encrypted_letters:
                encrypted_letters.append(extract[i-z].lower())
                letters.append(a_scandal_in_bohemia[i].lower())
        if len(encrypted_letters) >= 26:
            break
    letters = [x for _,x in sorted(zip(letters,encrypted_letters))]
    key = ''.join(letters)
    return key
