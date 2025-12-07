import pytest

from aoc.day3 import biggest_sequence, part1_total_output_joltage, part2_total_output_joltage

TEST_BANKS = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1_max_joltage_987654321111111():
    result = biggest_sequence("987654321111111", 2)
    assert result == 98


def test_part1_max_joltage_811111111111119():
    result = biggest_sequence("811111111111119", 2)
    assert result == 89


def test_part1_max_joltage_234234234234278():
    result = biggest_sequence("234234234234278", 2)
    assert result == 78


def test_part1_max_joltage_818181911112111():
    result = biggest_sequence("818181911112111", 2)
    assert result == 92


def test_part1_total_output_joltage():
    banks = TEST_BANKS.splitlines()
    result = part1_total_output_joltage(banks)
    assert result == 357


def test_part2_max_joltage_987654321111111():
    result = biggest_sequence("987654321111111", 12)
    assert result == 987654321111


def test_part2_max_joltage_811111111111119():
    result = biggest_sequence("811111111111119", 12)
    assert result == 811111111119


def test_part2_max_joltage_234234234234278():
    result = biggest_sequence("234234234234278", 12)
    assert result == 434234234278


def test_part2_max_joltage_818181911112111():
    result = biggest_sequence("818181911112111", 12)
    assert result == 888911112111


def test_part2_total_output_joltage():
    banks = TEST_BANKS.splitlines()
    result = part2_total_output_joltage(banks)
    assert result == 3121910778619



"""
    In 987654321111111, you can make the largest joltage possible, 
    98, by turning on the first two batteries.
    In 811111111111119, you can make the largest joltage possible 
    by turning on the batteries labeled 8 and 9, producing 89 jolts.
    In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    In 818181911112111, the largest joltage you can produce is 92.

The total output joltage is the sum of the maximum joltage from each bank, 
so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.
"""