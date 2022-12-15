import pytest

from day import part1, part2, process

_test_input = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".strip()
_test_part1_expect = 26
_test_part2_expect = 56000011

with open('input.txt') as f:
    _actual_inputs = f.read()

_test_part1 = (
        (_test_input, 10, _test_part1_expect),
)

@pytest.mark.parametrize('raw,y,expect', _test_part1)
def test_part1(raw, y, expect):
    inputs = process(raw)
    assert expect == part1(inputs, _y=y)

_test_part2 = (
        (_test_input, 20, _test_part2_expect),
)

@pytest.mark.parametrize('raw,most,expect', _test_part2)
def test_part2(raw, most, expect):
    inputs = process(raw)
    assert expect == part2(inputs, most)

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
