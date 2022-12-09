def first_non_repeating_letter(string):
    count = 0
    string1 = string.lower()
    while count < len(string1):
        letter = string1[count]
        if string1.count(letter) == 1:
            return string[count]
        count += 1
    return None

def main():
    print("\tTask №2")
    print(first_non_repeating_letter("treated"))
    print(first_non_repeating_letter("tREaTed"))
    print(first_non_repeating_letter("sDdS"))

if __name__ == "__main__":
    main()