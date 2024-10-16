from pathlib import Path


def is_circular_symlink(symlink: Path) -> bool:
    """Проверить, что символическая ссылка циклична."""
    if not symlink.exists(follow_symlinks = False):
        raise FileNotFoundError
    if not symlink.is_symlink():
        raise RuntimeError
    if not Path.readlink(symlink).exists(follow_symlinks = False):
        return False

    used = set()
    now = symlink
    while (True):
        if Path.readlink(now).is_symlink():
            if Path.readlink(now) in used:
                return True
            else:
                used.add(now)
                now = Path.readlink(now)
        else:
            return False

# first_symlink = Path("first_symlink")
# second_symlink = Path("second_symlink")

# second_symlink.symlink_to(first_symlink)
# first_symlink.symlink_to(second_symlink)

# assert is_circular_symlink(first_symlink)
# assert is_circular_symlink(second_symlink)