def duplicate(arr):
    result = arr
    duplicates = []
    for i in range(len(result)):
        k = i + 1
        for j in range(k, len(result)):
            if result[i] == result[j]:
                duplicates.append(result[i])
    print(duplicates)


def main():
    file = open("day_1_input.txt", "r+")
    val = []
    for string in file:
        val.append(int(string))
    total = 0
    result = []
    for i in range(len(val)):

        total += val[i]
        result.append(total)
    print(result)
    print(duplicate(result))


if __name__ == "__main__":
    main()
