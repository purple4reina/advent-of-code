import pytest

from day import part1, part2, process

_test_input = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".strip()
_test_part1_expect = 1651
_test_part2_expect = None

with open('input.txt') as f:
    _actual_inputs = f.read()

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
