__author__ = 'ahmedissawi'
def array_count(n=2):
    notebook,data=read_input()
    for item in data :
        notebook[item-1]+=1

    return notebook

def read_input():

    f = open('arraycount.txt', 'r')
    file_contents = file.readlines(f)

    notebook=[]
    header=int(file_contents[0].split(' ')[1])
    for i in range(1,header+1):
        notebook.append(0)

    file_contents = file_contents[1:]  #replace the first integer

    numbers = []
    for line in file_contents:
        line_data = line.split(' ')
        for num in line_data:
            numbers.append(int(num))
    return notebook,numbers
output=""
for num in array_count():
    output+=str(num)+" "
print(output)

