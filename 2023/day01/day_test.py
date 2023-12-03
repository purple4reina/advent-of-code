import pytest

from day import part1, part2, process

_test_input_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()
_test_part1_expect = 142
_test_input_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()
_test_part2_expect = 281

with open('input.txt') as f:
    _actual_inputs = f.read()

_test_part1 = (
        (_test_input_1, _test_part1_expect),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_part2 = (
        (_test_input_2, _test_part2_expect),
)

@pytest.mark.parametrize('raw,expect', _test_part2)
def test_part2(raw, expect):
    inputs = process(raw)
    assert expect == part2(inputs)

_part1_wrong_answers = (
)

@pytest.mark.parametrize('ans', _part1_wrong_answers)
def test_part1_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part1(inputs)

_part2_wrong_answers = (
)

@pytest.mark.parametrize('ans', _part2_wrong_answers)
def test_part2_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part2(inputs)
