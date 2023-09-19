if __name__ == "__main__":
    width = int(input("Width: "))
    height = int(input("Height: "))

    count = 0
    for i in range(0, height):
        string = ""
        for j in range(0, width):
            string += f"{count % 10} "
            count += 1
        if i == height:
            string -= " "
        print(string)
