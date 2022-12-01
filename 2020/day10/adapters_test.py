import pytest
from adapters import solve

_test_solve = (
        ("""16
10
15
5
1
11
7
19
6
12
4""".split('\n'), 8),

        ("""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n'), 19208),
)

@pytest.mark.parametrize('n,expect', _test_solve)
def test_solve(n, expect):
    assert expect == solve(n)
