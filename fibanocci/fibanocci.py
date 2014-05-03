from math import *
def read_input():

    f = open('fibanocci.txt', 'r')
    data=[]
    for number in file.readlines(f)[ 1: ]:

        data.append(long(number))

    return data
def fibanocci_index():
    lst=read_input()

    fib_index =lambda  fibnonci : 0 if fibnonci==0 else int(round(log(fibnonci*(sqrt(5)+0.5),1.618033989),0))
    result = []
    for num in lst :
        result.append(fib_index(num))

    return result

def main():
    output=''
    for index in fibanocci_index() :
        output+=str(index)+' '
    print output



if __name__ == "__main__":
    main()