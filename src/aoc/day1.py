
type Count = int
type Position = int


def part1():
    with open("data/day1.txt") as f:
        count_zeros = count_at_zero(f.read())
    print(f"Part 1: {count_zeros}")


def count_at_zero(sequence, start: Position=50) -> Position:
    count = 0
    position = start
    for line in sequence.splitlines():
        position = make_move(line, position)
        if position == 0:
            count += 1
    return count


def part2():
    with open("data/day1.txt") as f:
        final_position, count_zeros = count_through_zero(f.read())
    print(f"Part 2: {count_zeros}")



def count_through_zero(sequence, start=50) -> tuple[Position, Count]:
    rows = 0
    count = 0
    position = start
    for line in sequence.splitlines():
        position, c = make_move_through_zero(line, position)
        count += c
        rows += 1
    print(f"processed {rows} rows, final position {position}, count zeros {count}")
    return position, count


def make_move(move_line: str, start: int) -> Position:
    return make_move_through_zero(move_line, start)[0]


def make_move_through_zero(move_line: str, start: int) -> tuple[Position, Count]:
    direction = move_line[0]
    move = int(move_line[1:])
    direction = 1 if direction == "R" else -1
    if direction == -1 and start == 0:
        start = 100
    quotient, remainder = divmod(start + (move * direction), 100)
    count = abs(quotient)
    if direction == -1 and remainder == 0:
        count += 1
    return remainder, count


if __name__ == "__main__":
    part1()
    part2()


"""
dan@Dans-MacBook-Pro-2 advent-of-code-2025 % uv run src/aoc/day1.py
Part 1: 1040
processed 4239 rows, final position 98, count zeros 6027
Part 2: 6027
"""