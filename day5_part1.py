

def in_any_range(ingredient: int, ranges: list[list[int]]) -> bool:

    for r in ranges:
        start, end = r[0], r[1]
        if ingredient > end:  # move to next range
            continue
        elif ingredient >= start:
            return True
    return False


def count_fresh_ingredients(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().split("\n\n")
        ranges = [list(map(int, i.split("-"))) for i in data[0].split("\n")]
        available = [int(i) for i in data[1].split("\n")]

    ranges.sort(key=lambda x: x[1])  # sort by last

    count = 0
    for ingredient in available:
        count += in_any_range(ingredient, ranges)

    return count


print(count_fresh_ingredients("inputs/input_day5_example.txt"))
print(count_fresh_ingredients("inputs/input_day5.txt"))
