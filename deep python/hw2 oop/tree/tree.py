import dataclasses

from argparse import ArgumentParser, Namespace
from pathlib import Path


@dataclasses.dataclass
class RecursionSettings:
    """Настройки рекурсии."""
    indent: int = 4
    prune: bool = False
    depth: int | None = -1
    extension: list[str] | None = None
    output: Path | None = None


def get_parser() -> ArgumentParser:
    """Получить парсер аргументов командной строки."""
    parser = ArgumentParser("tree",description="Сделай дерево директории")
    parser.add_argument('path', type=Path,default=Path("."),help="Директория, по которой строим дерево")
    parser.add_argument("-i",'--indent',metavar='VALUE',type=int,default=4,help="Кол-во пробелов, по умолчанию = 4")
    parser.add_argument("-p",'--prune',action='store_true',help='Флаг для игнорирования пустых директорий\
                                    и директорий, в которые вложены пустые директории, по умолчанию = False')
    parser.add_argument('-d','--depth',metavar='VALUE',type=int,default=-1,help='Ограничение глубины погружения\
                        по умолчанию ограничания нет')
    parser.add_argument('-o','--output',metavar='PATH',type=Path,help='Вывод в файл, требуется указать \
                        файл, в который надо записать вывод')
    parser.add_argument('-e','--extension',action='append',type=str, help="Файлы какого расширения включить в вывод")
    return parser



def has_valid_args(args: Namespace) -> tuple[bool, str]:
    """Проверить, что аргументы валидны."""
    args.path = args.path.resolve()
    if (not args.path.is_dir()):
        return False, "Директории нет или переданный путь - не директория"
    if args.output is not None:
        if args.output.exists():
            if args.output.is_dir() or args.output.is_symlink():
                return False, "Неверный тип файла вывода"
        else:
            args.output.touch()
    if args.depth < -1:
        return False, "Глубина отрицательная, должна быть >= 0"
    if args.indent <= 0:
        return False, "Отступ неположительный, должен быть > 0"






    return True, 'OK'


def get_extension(path: Path) -> str:
    return ''.join(path.suffixes)

def dfs1(curr,settings) -> bool:
    if curr.is_file():
        if ((settings.extension is None) or (get_extension(curr) in settings.extension)):
            return True
    elif curr.is_symlink():
        return False
    elif curr.is_dir():
        for neigh in curr.iterdir():
            if dfs1(neigh, settings):
                return True
    return False

def comparator(path) -> tuple[bool, str]:
    return not path.is_dir(), str(path.name)


def dfs(now: Path, dep: int, ind: int, settings, res) -> None:

    if ((settings.depth < dep) and (settings.depth != -1)):
        return None

    elif now.is_symlink():
        return None

    elif now.is_file():
        if ((settings.extension is None) or (get_extension(now) in settings.extension)):
            res.append(" " * ind + str(now.name))

    elif now.is_dir() and (dep != 0):
        if not(settings.prune and (not dfs1(now,settings))):
            res.append(" " * ind + str(now.name) + '/')
            neighs = list(now.iterdir())
            neighs.sort(key=comparator)
            for i in neighs:
                dfs(i, dep + 1, ind + settings.indent,settings,res)
    else:
        neighs = list(now.iterdir())
        neighs.sort(key=comparator)
        for i in neighs:
            dfs(i, dep + 1, ind + settings.indent,settings,res)


def tree(path: Path, settings) -> None:
    res = [str(path)+'/']
    dfs(path, 0, 0,settings,res)
    if settings.output is None:
        for i in res:
            print(i)
    else:
        with open(settings.output, "w") as file:
            for i in res:
                file.write(i + "\n")


def main(argv: list[str] | None = None) -> None:

    parser = get_parser()
    if not argv:
        args = parser.parse_args(str(Path('.')))
    else:
        args = parser.parse_args(argv)

    checker = has_valid_args(args)
    if not checker[0]:
        raise ArgumentParser.error(parser, checker[1])

    if args.extension is None:
        settings = RecursionSettings(
            indent=args.indent,
            prune=args.prune,
            depth=args.depth,
            extension=args.extension,
            output=args.output
        )
    else:
        settings = RecursionSettings(
            indent=args.indent,
            prune=True,
            depth=args.depth,
            extension=[i if (not i or i[0] == '.') else ('.' + i) for i in args.extension],
            output=args.output
        )

    tree(args.path, settings)

if __name__ == "__main__":
    main()
