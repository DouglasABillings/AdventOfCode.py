def frequency(input):
    i = 0
    current = 0
    freq_list = {0}
    while True:
        current += input[i]
        if current in freq_list:
            return current
        freq_list.add(current)
        i += 1
        if i == len(input):
            i = 0


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

    print(total)
    print(frequency(val))


if __name__ == "__main__":
    main()
