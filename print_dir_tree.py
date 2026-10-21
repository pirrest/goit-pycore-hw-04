import sys
from pathlib import Path
from colorama import Fore, Style, init


def print_tree(directory, prefix=""):
    """Recursively print the directory structure with colors."""
    entries = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "┗ " if is_last else "┣ "
        if entry.is_dir():
            print(f"{prefix}{branch}{Fore.BLUE}📂{entry.name}{Style.RESET_ALL}")
            print_tree(entry, prefix + ("  " if is_last else "┃ "))
        else:
            print(f"{prefix}{branch}{Fore.GREEN}📜{entry.name}{Style.RESET_ALL}")


def show_directory(path_arg):
    path = Path(path_arg)
    if not path.exists():
        print(f"{Fore.RED}Path does not exist: {path}{Style.RESET_ALL}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Path is not a directory: {path}{Style.RESET_ALL}")
        return
    print(f"{Fore.BLUE}📦{path.resolve().name}{Style.RESET_ALL}")
    try:
        print_tree(path)
    except PermissionError as error:
        print(f"{Fore.RED}Permission denied: {error}{Style.RESET_ALL}")


if __name__ == "__main__":
    init(autoreset=False)
    # Fall back to the current working directory when no path is given
    show_directory(sys.argv[1] if len(sys.argv) > 1 else Path.cwd())
