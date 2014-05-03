def read_input():

    f = open('index.txt', 'r')
    file_contents = file.readlines(f)[1]
    data=[]
    count=1
    for number in file_contents.split(' '):

        array_item=count,int(number)
        data.append(array_item)
        count+=1
    return data
def bubble_sort():
    lst=read_input()

    for passesLeft in range(len(lst)-1, 0, -1):
         for index in range(passesLeft):
             _index,_item=lst[index]
             _index1,_item1=lst[index+1]
             if _item >_item1 :
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst

def main():
    output=''
    for index,count in bubble_sort() :
        output+=str(index)+' '
    print output



if __name__ == "__main__":
    main()