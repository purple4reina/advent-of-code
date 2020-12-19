import pytest
from cycles import solve, cycle, active

_test_solve = (
        (('.#.', '..#', '###'), 112),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)

_test_cycle = (
    ({
        (0, 0, 0): False, (0, 1, 0): True, (0, 2, 0): False, (1, 0, 0): False,
        (1, 1, 0): False, (1, 2, 0): True, (2, 0, 0): True, (2, 1, 0): True,
        (2, 2, 0): True,
    }, 11),
)

@pytest.mark.parametrize('n,expect', _test_cycle)
def test_cycle(n, expect):
    assert expect == sum(cycle(n).values())

_test_active = (
        (0, 0, 0, {}, 0),
        (0, 0, 0, {(0, 0, 0): True}, 0),
        (0, 0, 0, {(0, 0, 0): False}, 0),
        (0, 0, 0, {(1, 0, 0): False}, 0),
        (0, 0, 0, {(1, 0, 0): True}, 1),
        (0, 0, 0, {(1, 0, 0): True, (0, -1, 0): True}, 2),
        (0, 0, 0, {(5, 0, 0): True}, 0),
)

@pytest.mark.parametrize('x,y,z,c,expect', _test_active)
def test_active(x,y,z,c, expect):
    assert expect == active(x,y,z,c)
