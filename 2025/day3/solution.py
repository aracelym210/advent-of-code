def main():
    with open('input.txt', 'r') as f:
        battery_banks = [line.strip() for line in f.readlines()]

    highest_jolts = []
    part1 = 0
    for bank in battery_banks:
        highest_jolts.append(find_highest_nums(bank))

    for jolts in highest_jolts:
        part1 += jolts

    print(f"Part 1: {part1}")


def find_highest_nums(bank: str) -> int:
    battery = list(map(int, bank))  # convert string input into list of numbers 

    jolt_a = max(battery[:-1]) 
    jolt_a_index = battery.index(jolt_a)

    right = battery[jolt_a_index + 1:]  # split off a second list to the right of jolt_a

    jolt_b = max(right)

    return int(f"{jolt_a}{jolt_b}")


if __name__ == "__main__":
    main()
