import math

if __name__ == "__main__":
    print("°C °F")
    for i in range(0, 11):
        celsius = i * 10
        fahrenheit = celsius * (9 / 5) + 32
        print(f"{celsius} {math.floor(fahrenheit)}")
