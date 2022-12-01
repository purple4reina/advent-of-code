import pytest
from boarding import get_seat_id

_test_get_seat_id = (
        ('FBFBBFFRLR', 357),
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
)

@pytest.mark.parametrize('n,expect', _test_get_seat_id)
def test_get_seat_id(n, expect):
    assert expect == get_seat_id(n)
