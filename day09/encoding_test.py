import pytest
from encoding import solve

_test_solve = (
        ("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n'), 62),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n, length=5)
