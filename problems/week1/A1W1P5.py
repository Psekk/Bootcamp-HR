if __name__ == '__main__':
    string = input("Sum: ")
    total = sum([int(char) for char in string])
    calculation_string = '+'.join([char for char in string])
    print(f"{calculation_string}={total}")
