if __name__ == '__main__':
    raw_license = input("")
    if len(raw_license) > 8:
        print("invalid")
        exit(-1)
    split_license = raw_license.split("-")
    if False in [part.isalnum() for part in split_license]:
        print("invalid")
        exit(-1)
    if True in [len(part) < 1 for part in split_license]:
        print("invalid")
        exit(-1)
    if split_license[0].isalpha() and split_license[1].isalpha() and len(split_license[0]) != len(split_license[1]):
        print("invalid")
        exit(-1)
    print("valid")