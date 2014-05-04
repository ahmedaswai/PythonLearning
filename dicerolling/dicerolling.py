__author__ = 'ahmedissawi'
def read_data():
    f = open('dicerolling.txt', 'r')
    file_contents = file.readlines(f)[1:]
    data = []
    for number in file_contents :
        data.append(float(number.replace('\n','')))

    return data
def dicerolling():
    dice_rolling_exp =lambda number : int(number*6)+1
    print (' '.join(str(dice_rolling_exp(x)) for x in read_data()))
def main():
   dicerolling()


if __name__ == "__main__":
    main()

