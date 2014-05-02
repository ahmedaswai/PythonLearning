__author__ = 'ahmedissawi'


def get_average():
    data=read_input()
    average=[]
    for ln in data:
        average.append(get_avg_array(ln))

    return average

def get_avg_array(line):
    lst=line.split(' ')
    total=0
    for item in lst:
        total+=float(item)
    result=round(total/len(lst),0)
    return int(result)


def read_input():
    f = open('avgarray.txt', 'r')
    file_contents = file.readlines(f)
    numbers = []
    for line in file_contents:
        numbers.append(line.replace('0\n', '').strip())

    return numbers[1:]

result=get_average()
result_out=''
for out in result:
    result_out+=str(out)+' '

print result_out
