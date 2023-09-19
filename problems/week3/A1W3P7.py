if __name__ == "__main__":
    combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]

    print("\nAND")
    for i in range(0, len(combinations)):
        combi = combinations[i]
        a = combi[0]
        b = combi[1]
        print(f"{bool(a)} + {bool(b)} = {a & b == True}")

    print("\nOR")
    for i in range(0, len(combinations)):
        combi = combinations[i]
        a = combi[0]
        b = combi[1]
        print(f"{bool(a)} + {bool(b)} = {a | b == True}")

    print("\nNOT")
    for i in range(0, len(combinations)):
        combi = combinations[i]
        a = combi[0]
        b = combi[1]
        print(f"{bool(a)} + {bool(b)} = {a ^ b == True}")

    print("\nXOR")
    for i in range(0, len(combinations)):
        combi = combinations[i]
        a = combi[0]
        b = combi[1]
        print(f"{bool(a)} + {bool(b)} = {a != b}")

    print("\nNAND")
    for i in range(0, len(combinations)):
        combi = combinations[i]
        a = combi[0]
        b = combi[1]
        print(f"{bool(a)} + {bool(b)} = {not a & b}")