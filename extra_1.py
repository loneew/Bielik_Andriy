def ex_task_1(dig):
    string_dig = str(dig)
    print(string_dig, end=' => ')
    if len(string_dig) == 1:
        return -1
    i = len(string_dig) - 1
    while i > 0:
        j = 1
        while i - j > -1:
            if int(string_dig[i - j]) < int(string_dig[i]):
                list_digit = list(string_dig)
                temp = list_digit[i - j]
                list_digit[i - j] = list_digit[i]
                list_digit[i] = temp
                return int(''.join(map(str, list_digit)))
            j += 1
        i -= 1
    return -1


def main():
    print("\tExtra task №1")
    print(ex_task_1(513))
    print(ex_task_1(111))


if __name__ == "__main__":
    main()
