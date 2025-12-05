import itertools


def count_rolls(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().split("\n")

    rof_accesssible = 0
    n = len(data)
    for y in range(n):
        for x in range(n):
            state = data[y][x]
            if state == "@":

                # get all adjacent positions
                indices = [(y - 1, y, y + 1), (x - 1, x, x + 1)]
                f_positions = list(itertools.product(indices[0], indices[1]))
                f_positions.remove((y, x))  # remove itself

                rof_adj = 0
                for pos in f_positions:
                    y_adj, x_adj = pos[0], pos[1]

                    if 0 <= y_adj < n and 0 <= x_adj < n:  # out of grid bounds
                        state_adj = data[y_adj][x_adj]
                        if state_adj == "@":
                            rof_adj += 1

                if rof_adj < 4:
                    rof_accesssible += 1

    return rof_accesssible


print(count_rolls("inputs/input_day4_example.txt"))
print(count_rolls("inputs/input_day4.txt"))
