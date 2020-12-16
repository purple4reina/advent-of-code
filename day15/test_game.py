import pytest
from game import solve

_test_solve = (
        ((0,3,6), 436),
        ((1,3,2), 1),
        ((2,1,3), 10),
        ((1,2,3), 27),
        ((2,3,1), 78),
        ((3,2,1), 438),
        ((3,1,2), 1836),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
