from colorama import Fore, Style
from pathlib import Path
import argparse, os

path_separator = os.sep
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Path", help="Absolute path to root directory")
args = parser.parse_args()


def print_folder(folder_name):
    print(Fore.BLUE + folder_name)


def print_file(file_name):
    print(Fore.GREEN + file_name)


def get_clear_name(path, prefix):
    return str(path).removeprefix(prefix + path_separator).split(path_separator)[0]


def get_formated_string(text, level):
    gap = " " * (level * 4)
    return f"{gap}{text}"


def print_directory_content(dir, level):
    parent = str(dir.parents[0])
    print_folder(get_formated_string(get_clear_name(dir, parent) + path_separator, level))

    level += 1
    for item in dir.iterdir():
        if item.is_dir():
            print_directory_content(item, level)
        else:
            print_file(get_formated_string(get_clear_name(item, str(item.parents[0])), level))


try:
    root_path = Path(args.Path)

    if not root_path.exists() or not root_path.is_dir():
        raise FileExistsError(f"Directory '{str(root_path)}' does not exist")
    
    print_directory_content(root_path, 0)
    

except (FileExistsError) as e:
    print(Fore.RED + f"ERROR: {e}")
finally:
    print(Fore.RESET)