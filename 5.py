def task_5(str):
    str = str.upper()
    str = str.split(";")
    i = 0
    while i < len(str):
        a, b = str[i].split(":")
        str[i] = b + ", " + a
        i += 1
    str.sort()
    res = ") (".join(str)
    res = "(" + res + ")"
    print(res)


def main():
    print("\tTask 5:")
    s = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(s + "\n=>")
    task_5(s)


if __name__ == "__main__":
    main()
