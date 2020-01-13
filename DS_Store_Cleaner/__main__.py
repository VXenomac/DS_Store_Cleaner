import sys
from .DS_Store_Cleaner import *


def main():
    if len(sys.argv) > 1:
        files = all_file(sys.argv[1])
        remove_file(files)
    else:
        files = all_file(os.getcwd())
        remove_file(files)


if __name__ == '__main__':
    main()
