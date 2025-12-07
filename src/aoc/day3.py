

def part1_total_output_joltage(banks: list[str]) -> int:
    how_many = 2
    js = [biggest_sequence(bank, how_many) for bank in banks]
    return sum(js)


def part2_total_output_joltage(banks: list[str]) -> int:
    how_many = 12
    js = [biggest_sequence(bank, how_many) for bank in banks]
    return sum(js)


def biggest_sequence(bank: str, how_many: int) -> int:
    bank = [int(x) for x in bank]
    bank_length = len(bank)
    start_idx = 0
    vals = []
    for i in range(how_many):
        up_to = bank_length - how_many + i + 1
        val, idx = _max_from_to(bank, start_idx, up_to)
        vals.append(val)
        start_idx = idx + 1
    return int("".join([str(v) for v in vals]))


def _max_from_to(bank: list[int], start: int, end: int) -> tuple[int, int]:
    max_val = 0
    max_idx = 0
    for idx, val in enumerate(bank[start:end]):
        if val > max_val:
            max_val = val
            max_idx = idx
    return max_val, start + max_idx


if __name__ == "__main__":
    with open("data/day3.txt") as f:
        input_banks = f.read().splitlines()
        total_joltage = part1_total_output_joltage(input_banks)
        print(f"Part 1: {total_joltage}")
        total_joltage = part2_total_output_joltage(input_banks)
        print(f"Part 2: {total_joltage}")
