import pytest


from recite import recite


@pytest.mark.parametrize(
    ("numbers", "last", "expected"),
    [
        ([0, 3, 6], 2020, 436),
        ([1, 3, 2], 2020, 1),
        ([2, 1, 3], 2020, 10),
        ([1, 2, 3], 2020, 27),
        ([2, 3, 1], 2020, 78),
        ([3, 2, 1], 2020, 438),
        ([3, 1, 2], 2020, 1836),
        ([16, 11, 15, 0, 1, 7], 2020, 662),
        ([0, 3, 6], 30000000, 175594),
        ([16, 11, 15, 0, 1, 7], 30000000, 37312),
    ],
)
def test_recite(numbers, last, expected):
    assert recite(numbers, last) == expected
