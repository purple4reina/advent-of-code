import pytest
from day import part1, part2, process

_test_input = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
_test_part1_expect = 'CMZ'
_test_part2_expect = 'MCD'

def test_part1():
    inputs = process(_test_input)
    assert _test_part1_expect == part1(inputs)

def test_part2():
    inputs = process(_test_input)
    assert _test_part2_expect == part2(inputs)

with open('input.txt') as f:
    _actual_inputs = f.read()

_part1_wrong_answers = (
)

@pytest.mark.parametrize('ans', _part1_wrong_answers)
def test_part1_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part1(inputs)

_part2_wrong_answers = (
        'HZGJCLZBC',
)

@pytest.mark.parametrize('ans', _part2_wrong_answers)
def test_part2_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part2(inputs)
