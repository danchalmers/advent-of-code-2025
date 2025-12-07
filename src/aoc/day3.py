

def part1_total_output_joltage(banks: list[str]) -> int:
    js = [biggest_pair(bank) for bank in banks]
    return sum(js)


def biggest_pair(bank: str) -> int:
    max_val = 0
    max_idx = 0
    for idx, val in enumerate(bank[:-1]):
        val = int(val)
        if val > max_val:
            max_val = val
            max_idx = idx
    max_val2 = 0
    for val2 in bank[max_idx + 1:]:
        val2 = int(val2)
        if val2 > max_val2:
            max_val2 = val2
    return int(f"{max_val}{max_val2}")


if __name__ == "__main__":
    with open("data/day3.txt") as f:
        input_banks = f.read().splitlines()
        total_joltage = part1_total_output_joltage(input_banks)
        print(f"Part 1: {total_joltage}")
