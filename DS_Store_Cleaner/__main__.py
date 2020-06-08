import sys
from .DS_Store_Cleaner import *


def main():
    files = all_file(sys.argv[1]) if len(sys.argv) > 1 else all_file(os.getcwd())
    remove_file(files)


if __name__ == '__main__':
    main()
