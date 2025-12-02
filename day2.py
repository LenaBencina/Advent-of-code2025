import re


def get_invalid_id_if_exists(pattern: str, id_i: int, invalid_ids: list[int]) -> list[int]:
    match = re.search(pattern, str(id_i))
    if match:
        matched = int(match.group())
        if matched == id_i:
            invalid_ids.append(matched)
    return invalid_ids


def get_sum_of_invalid_ids(file_path: str) -> int:
    with open(file_path, "r") as f:
        data = f.read().split(",")

    pattern1 = r'(\d+)\1'
    pattern2 = r'(\d+)\1+$'  # $ ensures the repetition forms the complete number, not just a substring within it
    invalid_ids1, invalid_ids2 = [], []

    for id_range in data:
        id_first, id_last = id_range.split('-')

        for id_i in range(int(id_first), int(id_last) + 1):
            invalid_ids1 = get_invalid_id_if_exists(pattern1, id_i, invalid_ids1)
            invalid_ids2 = get_invalid_id_if_exists(pattern2, id_i, invalid_ids2)

    return sum(invalid_ids1), sum(invalid_ids2)


print(get_sum_of_invalid_ids("input_day2_example.txt"))
print(get_sum_of_invalid_ids("input_day2.txt"))
