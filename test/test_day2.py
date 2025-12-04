import pytest

from aoc.day2 import split_ranges, is_valid, invalid_in_range, day2_part1_sum_invalid_ids_in_ranges

TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_split_input():
    ranges = split_ranges(TEST_INPUT)
    assert len(ranges) == 11
    assert ranges[0] == (11, 22)
    assert ranges[1] == (95, 115)


def test_valid_101():
    valid = is_valid(101)
    assert valid is True


def test_valid_1112():
    valid = is_valid(1112)
    assert valid is True


def test_valid_2111():
    valid = is_valid(2111)
    assert valid is True


def test_valid_12():
    valid = is_valid(12)
    assert valid is True


def test_invalid_55():
    valid = is_valid(55)
    assert valid is False


def test_invalid_6464():
    valid = is_valid(6464)
    assert valid is False


def test_invalid_123123():
    valid = is_valid(123123)
    assert valid is False


def test_filter_invalid_11_22():
    ranges = split_ranges("11-22")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 2
    assert 11 in invalids
    assert 22 in invalids


def test_filter_invalid_95_115():
    ranges = split_ranges("95-115")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 99 in invalids


def test_filter_invalid_998_1012():
    ranges = split_ranges("998-1012")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 1010 in invalids


def test_filter_invalid_1188511880_1188511890():
    ranges = split_ranges("1188511880-1188511890")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 1188511885 in invalids


def test_filter_invalid_222220_222224():
    ranges = split_ranges("222220-222224")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 222222 in invalids


def test_filter_invalid_1698522_1698528():
    ranges = split_ranges("1698522-1698528")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 0


def test_filter_invalid_446443_446449():
    ranges = split_ranges("446443-446449")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 446446 in invalids


def test_filter_invalid_38593856_38593862():
    ranges = split_ranges("38593856-38593862")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 1
    assert 38593859 in invalids


def test_filter_invalid_565653_565659():
    ranges = split_ranges("565653-565659")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 0


def test_filter_invalid_824824821_824824827():
    ranges = split_ranges("824824821-824824827")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 0


def test_filter_invalid_2121212118_2121212124():
    ranges = split_ranges("2121212118-2121212124")
    invalids = list(invalid_in_range(ranges[0]))
    assert len(invalids) == 0


def test_sum_invalid_ids():
    sum_of_invalid = day2_part1_sum_invalid_ids_in_ranges(TEST_INPUT)
    assert sum_of_invalid == 1227775554

"""
The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. 
So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.
"""

