__author__ = 'ahmedissawi'
def read_data():
    f = open('weightedsum.txt', 'r')
    file_contents = file.readlines(f)[1]
    data = []
    for number in file_contents.split(' '):
        data.append(number)

    return data
def weighted_sum():

    print (' '.join(str(weighted_count(x)) for x in read_data()))
def main():
    weighted_sum()

def weighted_count(number):
    total=0
    for indx,num in enumerate(number):
        total += int(num)*(indx+1)

    return total
if __name__ == "__main__":
    main()

