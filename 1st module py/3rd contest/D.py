from typing import Iterable, Generator, Any


def flat_it(sequence: Iterable[Any]) -> Generator[Any, None, None]:
    for i in sequence:
        try:
            if not (type(i) == str and len(i) == 1):
                iter(i)
            else:
                raise TypeError
        except TypeError :
            yield i
        else:
            yield from flat_it(i)


a = flat_it(("1", 2, [1, [1, [range(4),[1,2]]]]))
for i in range(10):
    print(next(a))
