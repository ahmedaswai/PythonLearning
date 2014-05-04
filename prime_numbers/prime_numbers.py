__author__ = 'ahmedissawi'

from math import sqrt
def prime_numbers_generator(lim,size=200000):
    pp = 2
    ep = [pp]
    pp += 1
    tp = [pp]
    ss = [2]

    while pp < int(lim) and len(tp)< size:
        pp += ss[0]
        test = True
        sqrtpp = sqrt(pp)
        for a in tp:
            if a > sqrtpp: break
            if pp % a == 0:
                test = False
                break
        if test: tp.append(pp)
    ep.reverse()
    [tp.insert(0, a) for a in ep]


    return tp
def read_data():
    f = open('prime_numbers.txt', 'r')
    file_contents = file.readlines(f)[1]
    data = []
    for number in file_contents.split(' ') :
        data.append(int(number))
    return data
def main():
   print get_lst_prime_index()

def get_lst_prime_index():
    prime_numbers=prime_numbers_generator(10000000)
    print prime_numbers.__len__()
    input_data=read_data()
    return ''.join(str(prime_numbers[x-1])+' ' for x in input_data)


if __name__ == "__main__":
    main()
