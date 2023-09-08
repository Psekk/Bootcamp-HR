def get_data(years):
    return years * 12, years * 365


def try_parse_int(val):
    try:
        return int(val), True
    except ValueError:
        return -1, False


if __name__ == '__main__':
    string = input("Years: ")
    parsed, success = try_parse_int(string)
    if not success:
        print("Only enter integers!")
        exit(-1)
    data = get_data(parsed)
    print(f"Months: {data[0]}, Days: {data[1]}")
