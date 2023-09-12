if __name__ == "__main__":
    human_years = int(input("Human years: "))
    if human_years < 0:
        print("invalid input")
        exit(0)
    dog_years = min(2, human_years) * 10.5
    print(dog_years + max(0, human_years - 2) * 4)
