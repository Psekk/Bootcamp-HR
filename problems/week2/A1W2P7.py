if __name__ == '__main__':
    position = input("Position: ")
    column_index = ord(position[0]) - 65 + 1  # 65 == A
    row_index = int(position[1])

    is_black = column_index & 1 == True
    if not row_index & 1:
        is_black = not is_black

    print("black" if is_black else "white")
