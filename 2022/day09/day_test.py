import pytest

from day import part1, part2, process

_test_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()
_test_part1_expect = 13
_test_part2_expect = 1

with open('input.txt') as f:
    _actual_inputs = f.read()

_test_part1 = (
        (_test_input, _test_part1_expect),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_part2_second_example = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".strip()

_test_part2 = (
        (_test_input, _test_part2_expect),
        (_test_part2_second_example, 36),
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
