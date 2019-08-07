def main():
    file = open("day_1_input.txt", "r+")
    val = []
    for string in file:
        val.append(int(string))
    total = 0
    for i in range(len(val)):
        total += val[i]

    print(total)


if __name__ == "__main__":
    main()
