__author__ = 'Ahmed Issawi'


def read_data():
    f = open('collatz_sequence.txt', 'r')
    file_contents = file.readlines(f)[1]
    data = []
    for number in file_contents.split(' '):
        data.append(int(number))
    return data


def collatz_sequence():
    result = []
    collatz_exp_even_odd = lambda num, count: collatz_exp_even_odd(num / 2, count) if num % 2 == 0 \
        else collatz_exp_even_odd(3 * num + 1, count)
    collatz_exp = lambda num, count=1: count if num == 1 else  collatz_exp_even_odd(num, count + 1)
    #collatz_count=lambda count , collatz_number : count if collatz_exp(collatz_number)==collatz_number else collatz_count(count+1,collatz_count)
    for count in read_data():
        result.append(collatz_exp(count))


def main():
    print (collatz_sequence())


if __name__ == "__main__":
    main()
