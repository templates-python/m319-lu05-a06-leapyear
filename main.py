def main():
    year = int(input('Give a year:\n'))
    if year % 400 == 0:
        print('The year is a leap year.')
    elif (year % 4 == 0) and (year % 100 != 0):
        print('The year is a leap year.')
    else:
        print('The year is not a leap year.')


if __name__ == '__main__':
    main()
