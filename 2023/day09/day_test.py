import pytest

from day import part1, part2, process

_test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip()
_test_part1_expect = 114
_test_part2_expect = 2

with open('input.txt') as f:
    _actual_inputs = f.read().strip()

_test_part1 = (
        (_test_input, _test_part1_expect),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_part2 = (
        (_test_input, _test_part2_expect),
)

@pytest.mark.parametrize('raw,expect', _test_part2)
def test_part2(raw, expect):
    inputs = process(raw)
    assert expect == part2(inputs)

_part1_wrong_answers = (
        1938800267,  # too high
        1938800269,  # too high
        1938800271,  # too high
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
