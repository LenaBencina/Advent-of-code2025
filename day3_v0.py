def get_total_joltage_output(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().splitlines()

    max_jltgs = []
    for bank in data:
        max_jlt = 0
        for i1 in range(len(bank)):
            for i2 in range(i1+1, len(bank)):
                tmp_jlt = int(bank[i1] + bank[i2])
                if tmp_jlt > max_jlt:
                    max_jlt = tmp_jlt
        max_jltgs.append(max_jlt)

    return sum(max_jltgs)


print(get_total_joltage_output("inputs/input_day3_example.txt"))
print(get_total_joltage_output("inputs/input_day3.txt"))
