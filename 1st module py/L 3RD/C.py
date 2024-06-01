import sys



def check(a : list, b: list) -> int:
    if set(a) == set(b):
        return 1
    return 0



exec(sys.stdin.read())