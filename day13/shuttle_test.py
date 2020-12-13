import pytest
from shuttle import solve

_test_solve = (
        ("""939
7,13,x,x,59,x,31,19""".split('\n'), 295),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
