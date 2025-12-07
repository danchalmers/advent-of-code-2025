import pytest

from aoc.day4 import adjacent, format_layout, is_accessible, part1_count_accessible, part2_count_accessible

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_accessible_row0_col1():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 0, 1)
    assert result == False


def test_accessible_row0_col2():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 0, 2)
    assert result == True


def test_accessible_row0_col7():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 0, 7)
    assert result == False


def test_accessible_row1_col0():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 1, 0)
    assert result == True


def test_accessible_row1_col1():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 1, 1)
    assert result == False


def test_accessible_row2_col6():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 2, 6)
    assert result == True

def test_accessible_row9_col0():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 9, 0)
    assert result == True


def test_accessible_row9_col1():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 9, 1)
    assert result == False


def test_accessible_row9_col2():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 9, 2)
    assert result == True


def test_accessible_row9_col8():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 9, 8)
    assert result == True


def test_accessible_row9_col9():
    layout, max_row, max_col = format_layout(EXAMPLE)
    result = is_accessible(layout, max_row, max_col, 9, 9)
    assert result == False


def test_part1_count_accessible():
    result = part1_count_accessible(EXAMPLE)
    assert result == 13


def test_part2_count_accessible():
    result = part2_count_accessible(EXAMPLE)
    assert result == 43


def test_adjacent_zero_corner():
    result = adjacent(0, 0, 10, 10)
    assert (0, 1) in result
    assert (1, 0) in result
    assert (1, 1) in result
    assert (1, 2) not in result
    assert (2, 1) not in result
    assert (-1, -1) not in result


def test_adjacent_end_corner():
    result = adjacent(10, 10, 10, 10)
    assert (9, 9) in result
    assert (9, 10) in result
    assert (10, 9) in result
    assert (10, 10) not in result
    assert (10, 11) not in result
    assert (11, 10) not in result
    assert (11, 11) not in result


def test_adjacent_middle():
    result = adjacent(3, 3, 10, 10)
    assert (2, 2) in result
    assert (2, 3) in result
    assert (2, 4) in result
    assert (3, 2) in result
    assert (3, 4) in result
    assert (4, 2) in result
    assert (4, 3) in result
    assert (4, 4) in result
    assert (3, 3) not in result
