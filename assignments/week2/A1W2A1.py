if __name__ == "__main__":
    split_input = input().split("-")
    if len(split_input) != 3 or False in [split.isnumeric() for split in split_input] or len(split_input[0]) != 4:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
        exit(-1)

    month = int(split_input[1])
    day = int(split_input[2])

    days_in_month = 30 if month & 1 else 31
    if month == 2:
        days_in_month = 28

    new_year = int(split_input[0])
    new_month = month
    new_day = day + 1

    if new_day > days_in_month:
        new_month += 1
        new_day = 1
    if new_month > 12:
        new_month = 1
        new_year += 1

    print(f"next date: {new_year}-{'0' if new_month < 10 else ''}{new_month}-{'0' if new_day < 10 else ''}{new_day}")
