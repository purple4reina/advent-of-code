import pytest
from cycles import solve, cycle, active

_test_solve = (
        (('.#.', '..#', '###'), 848),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
