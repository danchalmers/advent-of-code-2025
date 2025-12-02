import pytest

from aoc.day1 import make_move, count_at_zero, make_move_through_zero, count_through_zero

test_sequence = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_part1_move_right():
    result = make_move("R1", 5)
    assert result == 6


def test_part1_move_left():
    result = make_move("L1", 5)
    assert result == 4


def test_part1_move_right_across_zero():
    result = make_move("R3", 99)
    assert result == 2


def test_part1_move_left_across_zero():
    result = make_move("L3", 1)
    assert result == 98


def test_part1_example_sequence():
    result = count_at_zero(test_sequence)
    assert result == 3


def test_part2_move_right():
    pos, count = make_move_through_zero("R1", 5)
    assert pos == 6
    assert count == 0


def test_part2_move_left():
    pos, count = make_move_through_zero("L1", 5)
    assert pos == 4
    assert count == 0


def test_part2_move_right_across_zero():
    pos, count = make_move_through_zero("R3", 99)
    assert pos == 2
    assert count == 1


def test_part2_move_left_across_zero():
    pos, count = make_move_through_zero("L3", 1)
    assert pos == 98
    assert count == 1


def test_part2_big_move_right():
    pos, count = make_move_through_zero("R310", 95)
    assert count == 4


def test_part2_big_move_left():
    pos, count = make_move_through_zero("L310", 5)
    assert count == 4


def test_part2_left_stop_at_zero_counts_once():
    pos, count = make_move_through_zero("L5", 5)
    assert pos == 0
    assert count == 1
    pos, count = make_move_through_zero("L5", 0)
    assert pos == 95
    assert count == 0


def test_part2_right_stop_at_zero_counts_once():
    pos, count = make_move_through_zero("R5", 95)
    assert pos == 0
    assert count == 1
    pos, count = make_move_through_zero("R5", 0)
    assert pos == 5
    assert count == 0


def test_part2_lr_stop_at_zero_counts_once():
    pos, count = make_move_through_zero("L5", 5)
    assert pos == 0
    assert count == 1
    pos, count = make_move_through_zero("R5", 0)
    assert pos == 5
    assert count == 0


def test_part2_rl_stop_at_zero_counts_once():
    pos, count = make_move_through_zero("R5", 95)
    assert pos == 0
    assert count == 1
    pos, count = make_move_through_zero("L5", 0)
    assert pos == 95
    assert count == 0


def test_part2_example_sequence():
    position, result = count_through_zero(test_sequence)
    assert result == 6
    assert position == 32
