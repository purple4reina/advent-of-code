import pytest
from day import part1, part2, process

_test_input = """
A Y
B X
C Z
""".strip()
_test_part1_expect = 15
_test_part2_expect = 12

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
