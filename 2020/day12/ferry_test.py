import pytest
from ferry import solve

_test_solve = (
        ("""F10
N3
F7
R90
F11""".split('\n'), 286),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
