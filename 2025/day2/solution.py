def main():
    invalid_count = 0

    with open('input.txt', 'r') as f:
        pids = f.readline()
        pids = pids.split(',')

    for pid in pids:
        first = int(pid.split('-')[0])
        last = int(pid.split('-')[1]) + 1

        rng = range(first, last)

        for id in rng:
            if is_invalid(str(id)) is True:
                invalid_count += id

    print(f"Part 1: {invalid_count}")


def is_invalid(id):
    # use divmod() to divide and mod % length of the string in half
    # divmod() returns a tuple (quotient, remainder)
    q, r = divmod(len(id), 2)

    # string slicing
    first, second = id[:q + r], id[q + r:]

    # repeated sequence = invalid
    if first == second:
        return True


if __name__ == "__main__":
    main()