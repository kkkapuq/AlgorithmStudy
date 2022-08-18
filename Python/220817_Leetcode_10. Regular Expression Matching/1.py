import re


def isMatch(s: str, p: str):
    if re.fullmatch(p, s):
        return True
    else:
        return False

isMatch('aa', 'a')