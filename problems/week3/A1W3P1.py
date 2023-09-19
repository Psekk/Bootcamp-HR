from functools import reduce

if __name__ == "__main__":
    name = input("Name: ").lower()
    for i in range(33, 64):
        name = name.replace(chr(i), "")
    print(f"{name} is{' ' if name[::-1] == name else ' not '}a palindrome")
