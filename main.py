import sys
import datetime
from dateutil import relativedelta as rdelta

lvl_1 = datetime.datetime(2019, 4, 30)
lvl_2 = datetime.datetime(2019, 6, 30)
lvl_4 = datetime.datetime(2019, 9, 30)
lvl_5 = datetime.datetime(2019, 12, 31)
lvl_7 = datetime.datetime(2020, 3, 31)
lvl_14 = datetime.datetime(2021, 3, 31)
lvl_16 = datetime.datetime(2022, 3, 31)
lvl_21 = datetime.datetime(2023, 3, 31)

def level(level):
    now = datetime.datetime.now()
    rd = rdelta.relativedelta(level, now)
    if rd.hours < 0:
        print("\t *** You fucked up! Say goodbye to School 21! :( ***")
    else:
        print("\t *** Your deadline will be in {0.months} months {0.days} days {0.hours} hours ***".format(rd))

def main():
    if len(sys.argv) == 2:
        if int(sys.argv[1]) == '0':
            level(lvl_1)
        elif int(sys.argv[1]) < 2:
            level(lvl_2)
        elif int(sys.argv[1]) < 4:
            level(lvl_4)
        elif int(sys.argv[1]) < 5:
            level(lvl_5)
        elif int(sys.argv[1]) < 7:
            level(lvl_7)
        elif int(sys.argv[1]) < 14:
            level(lvl_14)
        elif int(sys.argv[1]) < 16:
            level(lvl_16)
        elif int(sys.argv[1]) < 21:
            level(lvl_21)
        else:
            print("usage: deadline [your_level]")
    else:
        print("usage: deadline [your_level]")

if __name__ == '__main__':
    main()