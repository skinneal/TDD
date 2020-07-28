# Title: check_pwd.py (A2)
# Author: Allison Skinner
# Date: 7/27/2020

def check_pwd(pwd):
    if pwd == '' :
        return False

    if len(pwd) < 8 :
        return False

    if len(pwd) > 20 :
        return False

    var = 0
    for char in pwd:
        if char.islower():
            var += 1
    if var == 0:
        return False

    var = 0
    for char in pwd:
        if char.isupper():
            var += 1
    if var == 0:
        return False

    var = 0
    for char in pwd:
        if char.isdigit():
            var += 1
    if var == 0:
        return False

    symCount = 0
    symbols = '~`!@#$%^&*()_+-='
    for char in pwd:
        for sym in symbols:
            if ((char) == sym):
                symCount += 1
        if symCount == 0:
            return False

    return True

