__author__ = 'Ahmed Issawi'


def read_data():
    f = open('collatz_sequence.txt', 'r')
    file_contents = file.readlines(f)[1]
    data = []
    for number in file_contents.split(' '):
        data.append(int(number))
    return data


def counter_collatz(number):
    counter = 0
    while (number != 1):
        counter += 1
        if (number % 2 == 0):
            number = number / 2
        else:
            number = 3 * number + 1
    return counter


def collatz_sequence():
    result = []
    for numb in read_data():
        result.append(counter_collatz(numb))
    return result


def main():
    print (' '.join(str(x) for x in collatz_sequence()))


if __name__ == "__main__":
    main()
