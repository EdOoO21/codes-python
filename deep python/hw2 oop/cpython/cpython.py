from pathlib import Path
import platform
import sysconfig
import sys
import shutil

def is_cpython() -> bool:
    """Проверить, что используется `CPython`."""
    return platform.python_implementation() == 'CPython'

def is_linux() -> bool:
    """Проверить, что используется `Linux`."""
    return platform.system() == 'Linux'


def is_windows() -> bool:
    """Проверить, что используется `Windows`."""
    return platform.system() == 'Windows'

def is_macos() -> bool:
    """Проверить, что используется `is_macOS`."""
    return platform.system() == 'Darwin'


def is_supported_platform() -> bool:
    """Проверить, что платформа поддерживается."""
    return platform.system() in ['Linux', 'Darwin', 'Windows']


def is_supported_python_version() -> bool:
    """Проверить, что версия `Python` поддерживается."""
    return (sys.version_info.minor >= 8)


def get_cpython_root() -> Path:
    """Получить путь до корня `CPython`."""
    return Path(sysconfig.get_path("data"))



def get_interface_library() -> Path | None:
    """Получить путь до библиотеки-интерфейса, если она требуется."""
    if is_windows():
        path = Path.joinpath(Path(sysconfig.get_path("data")), 'libs/')
        patt = f"python{sys.version_info.major}{sys.version_info.minor}.lib"
        ans = next(path.rglob(patt), None)
        return ans
    return None



def get_shared_library() -> Path:
    """Получить путь до разделяемой библиотеки."""
    if is_windows():
        path = Path(sysconfig.get_path("data" ))
        patt = f"python{sys.version_info.major}.{sys.version_info.minor}.dll"
    elif is_linux():
        path = Path(sysconfig.get_config_var("LIBDIR"))
        patt = f"libpython{sys.version_info.major}.{sys.version_info.minor}.so"
    elif is_macos():
        path = Path(sysconfig.get_config_var("LIBDIR"))
        patt = f"libpython{sys.version_info.major}.{sys.version_info.minor}.dylib"
    else:
        raise AssertionError


    return next(path.rglob(patt))


def get_header_files() -> list[Path]:
    """Получить список загловочных файлов."""
    return list(Path(sysconfig.get_path("include")).rglob("*.h"))

def get_build_file_contents() -> str:
    """Получить содержимое файла `BUILD.bazel`"""
    with open('./third_party/cpython/BUILD.bazel', 'r') as file:
        data = file.read()
    return data



def main() -> None:
    """Запустить скрипт."""
    #1
    if not is_cpython():
        raise AssertionError("У Вас не CPython !")
    if not is_supported_platform():
        raise AssertionError("Ваша платформа не поддерживается, поддерживаются только Windows, Linux и macOs!")
    if not is_supported_python_version():
        raise AssertionError("Ваша слишком старая версия Python, требуется >= 3.8.0 !")
    #2
    path = Path('./third_party/cpython/')
    shutil.rmtree(path,ignore_errors=True)
    Path('./third_party/cpython').mkdir(parents=True, exist_ok=True)
    Path('./third_party/cpython/internal').mkdir(parents=True, exist_ok=True)
    #3
    hdrs = get_header_files()
    shared_library = get_shared_library()
    interface_library = get_interface_library()
    #4

    if is_windows():
        shared_library_path = shared_library.relative_to(Path(sysconfig.get_path("data")))
    else:
        shared_library_path = shared_library.relative_to(sysconfig.get_config_var("LIBDIR"))
    shared_library_path_final = Path.joinpath(path, shared_library_path)
    shared_library_path_final.touch( exist_ok=True)

    if interface_library is not None:
        interface_library_path = interface_library.relative_to(Path(sysconfig.get_path("data")))

    hdrs_path = []
    for i in hdrs:
        hdrs_path.append(i.relative_to(Path(sysconfig.get_path("include"))))


    if interface_library is not None:
        interface_library_path_final = Path.joinpath(path , interface_library_path)
        interface_library_path_final.parent.mkdir(parents=True, exist_ok=True)
        interface_library_path_final.touch( exist_ok=True)



    print("================================================================")
    path1 = Path('./third_party/cpython/internal')
    for i in hdrs_path:
        path2 = Path.joinpath(path1, i)
        path2.parent.mkdir(parents=True, exist_ok=True)
        path2.touch(exist_ok=True)


    #5
    bazel_path = Path('./third_party/cpython/BUILD.bazel')

    bazel_content = f"""cc_import(
        name = "cpython",
        hdrs = [
    """

    for i in hdrs_path:
        bazel_content += f"""        "internal/{i}",\n"""
    bazel_content += "    ],\n"
    bazel_content += '    includes = ["internal"],\n'
    if interface_library is None:
        bazel_content += f"""    interface_library = "{None}",\n"""
    else:
        bazel_content += f"""    interface_library = "{interface_library}",\n"""
    bazel_content += f"""    shared_library = "{shared_library}",\n"""
    bazel_content += """    visibility = ["//visibility:public"],\n"""
    bazel_content += ')'

    with bazel_path.open('w') as file:
        file.write(bazel_content)

if __name__ == "__main__":
    main()
