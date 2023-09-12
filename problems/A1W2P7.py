if __name__ == '__main__':
    position = input("Position: ")
    column_index = ord(position[0]) - 65  # 65 == A
    row_index = int(position[1])

    print("white" if column_index & 1 and row_index & 1 else "black")