if __name__ == '__main__':
    raw_input = input("In: ")
    sides = [int(string[2:len(string)]) for string in raw_input.split("," + (" " if ", " in raw_input else ""))]
    a, b, c = sides

    triangle_type = "Scalene"
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"

    print(triangle_type)
