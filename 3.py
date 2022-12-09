def digital_root(num):
    string_num = str(num)
    print("\t" + string_num + ":")
    while len(string_num) > 1:
        sum = 0
        i = 0
        while i < len(string_num):
            if i == len(string_num) - 1:
                print(string_num[i])
            else:
                print(string_num[i], end=' + ')
            sum += int(string_num[i])
            i += 1
        string_num = str(sum)
        print(string_num)
    return int(string_num)


def main():
    print("\tTask №3")
    digital_root(942)
    digital_root(132189)


if __name__ == "__main__":
    main()
