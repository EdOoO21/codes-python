import random
import string


def generate_unique_strings(n: int) -> list[str]:
    if n < 0:
        raise ValueError("n < 0, excpected >= 0")
    ans = set()
    while len(ans) <n:
        s = ""
        amount = random.randint(5,10)
        tp = random.randint(1, 3)
        for i in range(amount):
            if tp == 1:
                s += chr(random.randint(48,57))
            elif tp == 2:
                s += chr(random.randint(65,90))
            else:
                s += chr(random.randint(97,122))
        ans.add(s)
    return list(ans)