from functools import reduce

if __name__ == "__main__":
    sentence = input("Sentences: ").lower()
    for i in range(33, 64):
        sentence = sentence.replace(chr(i), "")
    no_whitespace_sentence = sentence.replace(" ", "")
    print(f"{sentence} is{' ' if no_whitespace_sentence[::-1] == no_whitespace_sentence else ' not '}a palindrome")
