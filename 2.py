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
    print("\tTask 2:")
    words = ["treated", "tREaTed", "sDdS"]
    for word in words:
        print(word + " -> " + str(first_non_repeating_letter(word)))

if __name__ == "__main__":
    main()