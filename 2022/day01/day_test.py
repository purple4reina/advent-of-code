import pytest
from day import part1, part2, process

_test_input = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()
_test_part1_expect = 24000
_test_part2_expect = 45000

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)
