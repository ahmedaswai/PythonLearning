__author__ = 'ahmedissawi'
import ast

def read_input():
    f = open('moduls_parser.txt', 'r')

    return ''.join(file.readlines(f)).replace('\n',' ')

def parser():
    exp = read_input()
    return eval(exp)


def main():
    print parser()


if __name__ == "__main__":
    main()