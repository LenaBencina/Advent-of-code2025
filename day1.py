
def get_number_of_zeros(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().splitlines()

    state = 50
    zeros_count1 = 0
    zeros_count2 = 0

    for rotation in data:
        direction, amount = rotation[0], int(rotation[1:])
        sign = 1 if direction == "R" else -1
        previous_state = state

        state_real = previous_state + sign * amount
        state = state_real % 100

        # part1
        if state == 0:
            zeros_count1 = zeros_count1 + 1

        # part 2
        over_count = abs(state_real) // 100

        if state_real <= 0 and previous_state != 0:
            over_count = over_count + 1

        zeros_count2 = zeros_count2 + over_count

    return zeros_count2

print(get_number_of_zeros("inputs/input_day1_example.txt"))
print(get_number_of_zeros("inputs/input_day1.txt"))


