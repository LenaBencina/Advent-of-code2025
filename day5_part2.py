
def count_fresh_ingredients(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().split("\n\n")
        ranges = [list(map(int, i.split("-"))) for i in data[0].split("\n")]

    ranges.sort(key=lambda x: x[0])  # sort by first

    start_previous, end_previous = ranges[0][0], ranges[0][1]  # initialize with the first one
    sum_total = 0
    for r in ranges[1:]:  # skip the first one
        start, end = r[0], r[1]

        # check if overlap with previous
        if start <= end_previous:  # if overlap
            # extend the privous one and go to the next
            start_previous = min(start_previous, start)
            end_previous = max(end_previous, end)
            continue
        else:
            sum_total += end_previous - start_previous + 1  # finish with the previous/sum up
            start_previous = start  # start new one
            end_previous = end

    # add the final one
    sum_total += end_previous - start_previous + 1
    return sum_total


print(count_fresh_ingredients("inputs/input_day5_example.txt"))
print(count_fresh_ingredients("inputs/input_day5.txt"))
