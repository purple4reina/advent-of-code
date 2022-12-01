import pytest
from day import part1, part2, process

_test_input = """
target area: x=20..30, y=-10..-5
""".strip()
_test_part1_expect = 45
_test_part2_expect = 112

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
