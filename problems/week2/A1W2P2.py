if __name__ == '__main__':
    year = int(input("Year: "))

    is_leap_year = year % 400 == 0
    if year % 4 == 0 and year % 100 != 0:
        is_leap_year = True

    print("Leap year" if is_leap_year else "Not a leap year")
