def main():
    # read file and strip \n from each line for clean input
    with open('mini.txt', 'r') as f:
        rotations = [line.strip() for line in f.readlines()]

    part1 = part_1(rotations)
    part2 = part_2(rotations)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


def part_1(rotations: list[str]) -> str:
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


def part_2(rotations: list[str]) -> str:
    password = 0
    dial = 50

    for rotation in rotations:
        if rotation.startswith('L'):
            print(f"{dial} - {int(rotation.split('L')[1])}")
            dial = dial - int(rotation.split('L')[1])
        else:
            print(f"dial {dial} + {int(rotation.split('R')[1])}")
            dial = dial + int(rotation.split('R')[1])

        print(f"{dial} % 100 = {dial % 100}")
        if dial < 0 or dial > 100:
            password += 1
            print(f"dial is less than 0 or greather than 100: {dial}. \npassword: {password}")

        dial = dial % 100

        if dial == 0:
            password += 1

    return password


if __name__ == "__main__":
    main()