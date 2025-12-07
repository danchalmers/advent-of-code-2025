

type Row = int
type Col = int
type LayoutCells = list[list[str]]

THRESHOLD = 4


def part1_count_accessible(input: str) -> int:
    layout, max_row, max_col = format_layout(input)
    accessibles = [
        (r, c)
        for r in range(max_row + 1)
        for c in range(max_col + 1)
        if is_accessible(layout, max_row, max_col, r, c)
    ]
    return len(accessibles)


def part2_count_accessible(input: str) -> int:
    layout, max_row, max_col = format_layout(input)
    return _part2_count_accessible(layout, max_row, max_col, 0)


def _part2_count_accessible(layout: LayoutCells, max_row: Row, max_col: Col, prev_count: int) -> int:
    accessibles = [
        (r, c)
        for r in range(max_row + 1)
        for c in range(max_col + 1)
        if is_accessible(layout, max_row, max_col, r, c)
    ]
    if len(accessibles) == 0:
        return prev_count
    for a in accessibles:
        layout[a[0]][a[1]] = '.'
    return _part2_count_accessible(layout, max_row, max_col, prev_count + len(accessibles))


def is_accessible(
        layout: LayoutCells,
        max_row: Row, max_col: Col,
        row: Row, col: Col
) -> bool:
    adjacents = adjacent(row, col, max_row, max_col)
    value = layout[row][col]
    if value != '@':
        return False
    adjacent_values = [layout[a[0]][a[1]] for a in adjacents]
    return sum([a == '@' for a in adjacent_values]) < THRESHOLD


def format_layout(layout: str) -> tuple[LayoutCells, Row, Col]:
    layout = [[c for c in r] for r in layout.splitlines()]
    max_row = len(layout) - 1
    max_col = len(layout[0]) - 1
    return layout, max_row, max_col


def adjacent(row: Row, col: Col, max_row: Row, max_col: Col) -> list[tuple[Row, Col]]:
    return [
        (r, c)
        for r in range(max(0, row-1), min(max_row+1, row+2))
        for c in range(max(0, col-1), min(max_col+1, col+2))
        if r != row or c != col
    ]


if __name__ == "__main__":
    with open("data/day4.txt") as f:
        layout = f.read()
        count_accessible = part1_count_accessible(layout)
        print(f"Part 1: {count_accessible}")
        count_accessible = part2_count_accessible(layout)
        print(f"Part 2: {count_accessible}")
