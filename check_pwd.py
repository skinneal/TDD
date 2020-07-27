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

    for char in pwd:
        if char.islower():
            return True
    return True

