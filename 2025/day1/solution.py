def main():
    # read file and strip \n from each line for clean input
    with open('input.txt', 'r') as f:
        rotations = [line.strip() for line in f.readlines()]

    password = part_1(rotations)
    print(f"PASSWORD: {password}")


def part_1(rotations: list) -> str:
    password = 0
    dial = 50

    for rotation in rotations:
        if rotation.startswith('L'):
            dial = dial - int(rotation.split('L')[1])
        else:
            dial = dial + int(rotation.split('R')[1])

        # print(f"{dial} % 100 = {dial % 100}")
        dial = dial % 100

        if dial == 0:
            password += 1

    return password


if __name__ == "__main__":
    main()