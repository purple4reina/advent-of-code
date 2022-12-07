import pytest

from day import part1, part2, process

with open('input.txt') as f:
    _actual_inputs = f.read()

_test_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip()
_test_part1_expect = 95437
_test_part2_expect = 24933642

_test_part1 = (
        (_test_input, _test_part1_expect),
        (_actual_inputs, 1648397),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_part2 = (
        (_test_input, _test_part2_expect),
        (_actual_inputs, 1815525),
)

@pytest.mark.parametrize('raw,expect', _test_part2)
def test_part2(raw, expect):
    inputs = process(raw)
    assert expect == part2(inputs)

_part1_wrong_answers = (
        1172073,
)

@pytest.mark.parametrize('ans', _part1_wrong_answers)
def test_part1_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part1(inputs)

_part2_wrong_answers = (
        41735494,
)

@pytest.mark.parametrize('ans', _part2_wrong_answers)
def test_part2_wrong_answers(ans):
    inputs = process(_actual_inputs)
    assert ans != part2(inputs)
