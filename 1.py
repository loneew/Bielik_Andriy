def filter_list(list):
    count = 0
    while count < len(list):
        if type(list[count]) != int:
            list.pop(count)
            count -= 1
        count += 1
    return list

def main():
    print("\tTask 1:")
    list1 = [1, 2, 'aasf', '1', '123', 123]
    list2 = ["qwerty", 34, "ASAP", 89]
    list3 = [1,2,'a','b']
    print("filter_list(" + str(list1) + ") == " + str(filter_list(list1)))
    print("filter_list(" + str(list2) + ") == " + str(filter_list(list2)))
    print("filter_list(" + str(list3) + ") == " + str(filter_list(list3)))

if __name__ == "__main__":
    main()