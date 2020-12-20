import pytest
from rules import *


_test_solve = (
        ("""0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split('\n'), 2),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
