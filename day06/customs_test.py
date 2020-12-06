import pytest
from customs import solve

_test_solve = (
        ("""abc

a
b
c

ab
ac

a
a
a
a

b""".split('\n'), 11),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
