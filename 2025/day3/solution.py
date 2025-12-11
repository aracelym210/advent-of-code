def main():
    with open('input.txt', 'r') as f:
        battery_banks = [line.strip() for line in f.readlines()]

    highest_jolts_pt1 = []
    highest_jolts_pt2 = []
    part1 = 0
    part2 = 0
    for bank in battery_banks:
        highest_jolts_pt1.append(find_highest_nums(bank))
        highest_jolts_pt2.append(find_highest_sequence(bank))

    for jolts in highest_jolts_pt1:
        part1 += jolts

    for jolts in highest_jolts_pt2:
        part2 += jolts

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


def find_highest_nums(bank: str) -> int:
    battery = list(map(int, bank))  # convert string input into list of ints

    jolt_a = max(battery[:-1]) 
    jolt_a_index = battery.index(jolt_a)

    right = battery[jolt_a_index + 1:]  # split off a second list to the right of jolt_a

    jolt_b = max(right)

    return int(f"{jolt_a}{jolt_b}")


def find_highest_sequence(bank: str) -> int:
    battery = list(map(int, bank))

    remaining_jolts = 11
    jolts = ""

    while remaining_jolts >= 0:
        if remaining_jolts != 0:
            jolt = max(battery[:-remaining_jolts])
        else:
            jolt = max(battery)

        index = battery.index(jolt)
        battery = battery[index + 1:]
        remaining_jolts -= 1
        jolts += str(jolt)

    return int(jolts)


if __name__ == "__main__":
    main()
