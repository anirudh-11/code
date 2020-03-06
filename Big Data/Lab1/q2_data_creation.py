import pandas as pd
from math import log10
def main():
    def_string = 'CSE20D'
    print("Enter the number of students : ")
    n = int(input())
    zero_String = '0'
    digit = int(log10(n))
    roll_number = []
    series = pd.Series()
    for i in range(n, 0, -1):
        if(digit == int(log10(i))):
            pass
        else:
            digit = digit - 1
            zero_String = zero_String + '0'
        roll_number.append(def_string + zero_String + str(i))
        if((i % 2) == 0):
            mark = 25 + ((i + 8) % 10)
        else:
            mark = 25 + ((i + 7) % 10)

        if(len(series) == 0):
            series = pd.Series(data = mark, index = [roll_number[-1]])
        else:
            series = series.append(pd.Series(data = mark, index = [roll_number[-1]]))

        if(i == n/2):
            median = mark

    mean = float(series.sum() / n)

    print(series)
    print("mean = {}, median = {}".format(mean, median))

if __name__ == "__main__":
    main()