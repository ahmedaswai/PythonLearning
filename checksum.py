__author__ = 'ahmedissawi'


def check_sum():
    arr = read_input()
    result = 0
    seed = 113
    limit = 10000007
    for num in arr:
        result = ((result + num) * seed) % limit
    return result


def read_input():
    f = open('checksum.txt', 'r')
    file_contents = file.readlines(f)
    file_contents = file_contents[1:]  #replace the first integer

    numbers = []
    for line in file_contents:
        line_data = line.split(' ')
        for num in line_data:
            numbers.append(int(num))

    return numbers


print check_sum()