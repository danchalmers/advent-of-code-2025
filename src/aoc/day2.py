from os.path import split
from typing import Iterable


def day2_part1_sum_invalid_ids_in_ranges(input_str: str) -> int:
    ranges = split_ranges(input_str)
    invalids = [i for r in ranges for i in invalid_in_range(r)]
    return sum(invalids)


def day2_part2_sum_invalid_ids_in_ranges(input_str: str) -> int:
    ranges = split_ranges(input_str)
    invalids = [i for r in ranges for i in pattern_in_range_part_2(r)]
    return sum(invalids)


def split_ranges(input_str: str) -> list[tuple[int, int]]:
    ranges = [r.split('-') for r in input_str.split(",")]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]
    return ranges


def is_valid(product_id: int) -> bool:
    product_id = str(product_id)
    length = len(product_id)
    split_at = length // 2
    return product_id[:split_at] != product_id[split_at:]


def invalid_in_range(id_range: tuple[int, int]) -> Iterable[int]:
    for product_id in range(id_range[0], id_range[1] + 1):
        if not is_valid(product_id):
            yield product_id



def pattern_in_range_part_2(id_range: tuple[int, int]) -> Iterable[int]:
    for product_id in range(id_range[0], id_range[1] + 1):
        if is_pattern_part_2(product_id):
            yield product_id


def is_pattern_part_2(product_id: int) -> bool:
    product_id = str(product_id)
    length = len(product_id)
    repeating = False
    for i in range(1, (length // 2) + 1):
        if divmod(length, i)[1] == 0:
            parts = [product_id[j:j+i] for j in range(0, length, i)]
            p0 = parts[0]
            repeating = repeating or all([p0 == p for p in parts[1:]])
    return repeating


if __name__ == "__main__":
    with open("data/day2.txt") as f:
        input_str = f.read()
        sum_invalid = day2_part1_sum_invalid_ids_in_ranges(input_str)
        print(f"Part 1: {sum_invalid}")
        sum_invalid = day2_part2_sum_invalid_ids_in_ranges(input_str)
        print(f"Part 2: {sum_invalid}")