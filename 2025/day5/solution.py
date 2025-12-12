def main():
    with open("input.txt", "r") as f:
        ingredients = [line.strip() for line in f.readlines()]

    pt1 = find_fresh(ingredients)

    print(f"Part 1: {pt1} fresh ingredients")


def find_fresh(ingredients: list) -> int:
    break_index = ingredients.index('')
    fresh_ranges = ingredients[:break_index]
    ingredient_ids = ingredients[break_index + 1:]
    fresh_ingredients = 0

    for i in ingredient_ids:
        i = int(i)
        for r in fresh_ranges:
            lower = int(r.split("-")[0])
            upper = int(r.split("-")[1])

            if lower <= i <= upper:
                fresh_ingredients += 1
                break

    return fresh_ingredients


if __name__ == "__main__":
    main()
