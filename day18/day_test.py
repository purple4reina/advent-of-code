import pytest
from day import part1, process, magnitude, add, explode, split, read_inputs

_test_part1 = (
        ("""
[1,1]
[2,2]
[3,3]
[4,4]""".strip(), magnitude([[[[1,1],[2,2]],[3,3]],[4,4]])),
        ("""
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]""".strip(), magnitude([[[[3,0],[5,3]],[4,4]],[5,5]])),
        ("""
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]""".strip(), magnitude([[[[5,0],[7,4]],[5,5]],[6,6]])),
        ("""
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]""".strip(), magnitude(
                [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])),
        ("""
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".strip(), 4140),
)

@pytest.mark.parametrize('raw,expect', _test_part1)
def test_part1(raw, expect):
    inputs = process(raw)
    assert expect == part1(inputs)

_test_magnitude = (
        ([9,1], 29),
        ([1,9], 21),
        ([[9,1],[1,9]], 129),
        ([[1,2],[[3,4],5]], 143),
        ([[[[0,7],4],[[7,8],[6,0]]],[8,1]], 1384),
        ([[[[1,1],[2,2]],[3,3]],[4,4]], 445),
        ([[[[3,0],[5,3]],[4,4]],[5,5]], 791),
        ([[[[5,0],[7,4]],[5,5]],[6,6]], 1137),
        ([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]], 3488),
        ([[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]], 4140),
)

@pytest.mark.parametrize('n,expect', _test_magnitude)
def test_magnitude(n, expect):
    assert expect == magnitude(n)

_test_add = (
        ([1,2],
            [[3,4],5],
            [[1,2],[[3,4],5]]),
        ([[[[4,3],4],4],[7,[[8,4],9]]],
            [1,1],
            [[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
        ([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
            [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
            [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]),
        ([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],
            [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
            [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]),
        ([[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
            [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
            [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]),

        ([[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],
            [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
            [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]),

        ([[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]],
            [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
            [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]),
        ([[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]],
            [7,[5,[[3,8],[1,4]]]],
            [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]),
        ([[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]],
            [[2,[2,2]],[8,[8,1]]],
            [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]),
        ([[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]],
            [2,9],
            [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]),
        ([[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]],
            [1,[[[9,3],9],[[9,0],[0,7]]]],
            [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]),
        ([[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]],
            [[[5,[7,4]],7],1],
            [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]),
        ([[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]],
            [[[[4,2],2],6],[8,7]],
            [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]),
)

@pytest.mark.parametrize('n1,n2,expect', _test_add)
def test_add(n1, n2, expect):
    assert expect == add(n1, n2)

_test_explode = (
        ([[[[[9,8],1],2],3],4],
            [[[[0,9],2],3],4]),
        ([[[[9,8],1],2],3],
            [[[[9,8],1],2],3]),
        ([7,[6,[5,[4,[3,2]]]]],
            [7,[6,[5,[7,0]]]]),
        ([6,[5,[4,[3,2]]]],
            [6,[5,[4,[3,2]]]]),
        ([[6,[5,[4,[3,2]]]],1],
            [[6,[5,[7,0]]],3]),
        ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]],
            [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
        ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]],
            [[3,[2,[8,0]]],[9,[5,[7,0]]]]),
        ([9,[5,[4,[3,2]]]],
            [9,[5,[4,[3,2]]]]),
        ([[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[0,[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[0,[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,0],[[11,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,0],[[11,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[0,[13,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[0,[13,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[0,[11,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[11,0]],[[[10,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[11,0]],[[[10,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[11,10]],[[0,8],[7,[1,6]]]]]),
        ([[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[0,[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[0,[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,0],[[11,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,0],[[11,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[0,[13,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[0,[13,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,0],[[14,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[15,0],[[14,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,14],[0,[14,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[15,14],[0,[14,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]),
        ([[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]],
            [[[[5,11],[13,0]],[[15,14],[14,0]]],[[2,[0,[11,4]]],[[[6,7],1],[7,[1,6]]]]]),
)

@pytest.mark.parametrize('n,expect', _test_explode)
def test_explode(n, expect):
    assert expect == explode(n)

_test_split = (
        ([[[[0,7],4],[15,[0,13]]],[1,1]], [[[[0,7],4],[[7,8],[0,13]]],[1,1]]),
        ([[[[0,7],4],[[7,8],[0,13]]],[1,1]],
            [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]),
        ([0,0], [0,0]),
        ([[10,10],[10,10]], [[[5,5],10],[10,10]]),
)

@pytest.mark.parametrize('n,expect', _test_split)
def test_split(n, expect):
    assert expect == split(n)

_test_not_part1 = (
        (process(read_inputs()), 2605),  # too low
)

@pytest.mark.parametrize('n,expect', _test_not_part1)
def test_not_part1(n, expect):
    assert expect != part1(n)
