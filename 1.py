def filter_list(list):
    count = 0
    while count < len(list):
        if type(list[count]) != int:
            list.pop(count)
            count -= 1
        count += 1
    return list

def main():
    print("\tTask №1")
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))
    print(filter_list(["qwerty", 34, "ASAP", 89]))

if __name__ == "__main__":
    main()