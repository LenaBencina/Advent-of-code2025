

def get_max_and_position(x: list, max_from: int, n_remaining: int) -> tuple[int, int]:

    max_to = len(x) - n_remaining
    largest = max(x[max_from: (max_to + 1)])
    # get indices of all maximums and take first that is >= max_from to skip the invalid ones
    # eg [4,1,4,1,4] in the second iteration you want [2,4] and then take 2 not [0,2,4], first one not revelant anymore
    largest_indices = [i for i, j in enumerate(x) if j == largest and i >= max_from]
    largest_index = largest_indices[0]

    return largest, largest_index


def get_total_joltage_output(file_path: str, n_digits: int) -> int:
    with open(file_path, "r") as f:
        data = f.read().splitlines()

    max_jltgs = []
    for bank in data:
        bank_digits = [int(i) for i in bank]  # str to list of ints

        max_jlt = ''
        max_from = 0
        n_remaining = n_digits

        for i in range(n_digits):
            biggest, biggest_index = get_max_and_position(bank_digits, max_from, n_remaining)
            max_from = biggest_index + 1  # next max has to be on the right from the chosen one
            max_jlt += str(biggest)  # add digit to form the number
            n_remaining = n_remaining - 1  # one more used

        max_jltgs.append(int(max_jlt))

    return sum(max_jltgs)


# part1
print(get_total_joltage_output("inputs/input_day3_example.txt", n_digits=2))
print(get_total_joltage_output("inputs/input_day3.txt", n_digits=2))

# part2
print(get_total_joltage_output("inputs/input_day3_example.txt", n_digits=12))
print(get_total_joltage_output("inputs/input_day3.txt", n_digits=12))
