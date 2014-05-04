__author__ = 'ahmedissawi'
from math import *


def read_input():
    f = open('gcd.txt', 'r')
    data = []
    for line in file.readlines(f)[1:]:
        numbers = line.split(' ')
        nums = int(numbers[0]), int(numbers[1])
        data.append(nums)

    return data

def gcd():
    lst = read_input()

    gcd_inside = lambda a, b: a if b == 0 else gcd_inside(b, a % b)
    result = []
    for num in lst:
        a , b = num
        _gcd = gcd_inside(a, b)
        _lcd = (a * b) / _gcd
        _result = _gcd, _lcd
        result.append(_result)

    return result


def main():
    print 7959974+5525047


if __name__ == "__main__":
    main()