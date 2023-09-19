if __name__ == "__main__":
    for i in range(1, 11):
        string = f"{i} "
        for j in range(1, 11):
            string += f"{i*j} "
        print(string)