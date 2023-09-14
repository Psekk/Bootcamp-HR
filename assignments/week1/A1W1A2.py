import math


def try_parse_float(val):
    try:
        return float(val), True
    except ValueError:
        return -1, False


if __name__ == '__main__':
    parsed, success = try_parse_float(input("Cost of the meal: "))
    if not success:
        print("Enter only float")
        exit(-1)
    costs = parsed*.21, parsed*.15
    print(f"Tax: {round(costs[0], 3)}, Tip: {round(costs[1], 3)}, Total: {round(parsed + math.fsum(costs), 3)}")
