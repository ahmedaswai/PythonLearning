def read_input():
    f = open('bubblesort.txt', 'r')
    file_contents = file.readlines(f)[1]
    data=[]

    for number in file_contents.split(' '):

        data.append(int(number))

    return data
def bubble_sort():
    lst=read_input()

    for passesLeft in range(len(lst)-1, 0, -1):
         for index in range(passesLeft):
             if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


def main():
    print (bubble_sort())


if __name__ == "__main__":
    main()