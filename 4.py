def task_4(arr, target):
    i = 0
    count = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == target:
                count += 1
            j += 1
        i += 1
    print("The number of pairs in the array " + str(arr) + ", the sum of which will give " + str(target) + " - " + str(
        count))


def main():
    print("\tTask №4")
    task_4([1, 3, 6, 2, 2, 0, 4, 5], 5)
    task_4([4, 1, 2, 3], 3)


if __name__ == "__main__":
    main()