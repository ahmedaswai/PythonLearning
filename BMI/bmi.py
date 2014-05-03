__author__ = 'ahmedissawi'
def read_input():

    f = open('bmi.txt', 'r')
    file_contents = file.readlines(f)[1:]
    data=[]
    for line in file_contents:
        m=line.split(' ')
        body_index=float(m[0]) / pow(float(m[1]),2)
        data.append(body_index)
    return data

def bmi():
    output = ''
    data=read_input()
    bmi_obesity=(lambda weight :'obese' if weight > 30.0 else  bmi_overweight(weight))
    bmi_overweight=(lambda weight :'over' if weight < 30.0 and weight>25.0 else bmi_normal(weight))
    bmi_normal=(lambda weight :'normal' if weight < 25.0 and weight>18.5 else bmi_under_weight(weight) )
    bmi_under_weight=(lambda weight :'under' if weight < 30.0 else 'no_case')

    for item in data:
        output+=bmi_obesity(item)+' '
    return output
print(bmi())