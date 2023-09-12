if __name__ == '__main__':
    sides = [int(string[2]) for string in input("In: ").split(", ")]
    a, b, c = sides[0], sides[1], sides[2]

    triangle_type = "Scalene"
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"

    print(triangle_type)