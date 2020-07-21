import sys
from .DS_Store_Cleaner import *


def main():
    if len(sys.argv) > 1:
        remove_file(sys.argv[1])
    else:
        remove_file(os.getcwd())


if __name__ == '__main__':
    main()
