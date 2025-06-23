import pytest
from stream_adapter import StreamAdapter


@pytest.fixture
def sa():
    return StreamAdapter()


def test_exact_12(sa):
    result = sa.split_massages([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
    assert result == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]


def test_short_fill(sa):
    result = sa.split_massages([[1, 2, 3]])
    assert result == [[1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1]]


def test_long_split_fill(sa):
    result = sa.split_massages([[1] * 25])
    assert result == [
        [1] * 12,
        [1] * 12,
        [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    ]


def test_partial_fill_across_messages(sa):
    result = sa.split_massages([[1, 2, 3], [4, 5]])
    assert result == [
        [1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [4, 5, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    ]


def test_mixed_sequence(sa):
    result = sa.split_massages([
        [4, 5, 8, 8, 6, 6, 8, 8, 6, 10, 11, 12],
        [2, 2, 1, 3],
        [4, 5, 8, 8, 8, 8, 8, 8, 8, 10, 11, 12, 15, 2, 1, 1],
        [1, 2, 3],
        [6, 6],
    ])
    assert result == [
        [4, 5, 8, 8, 6, 6, 8, 8, 6, 10, 11, 12],
        [2, 2, 1, 3, 1, 2, 1, 2, 1, 2, 1, 2],
        [4, 5, 8, 8, 8, 8, 8, 8, 8, 10, 11, 12],
        [15, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [6, 6, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    ]

def test_replace_555_with_666(sa):
    input_messages = [
        [1, 5, 5, 5, 2, 3],
        [5, 5, 5],
        [4, 5, 5, 5, 5, 5, 6],
        [5, 5],
        [1, 2, 3]
    ]
    expected_chunks = [
        [1, 6, 6, 6, 2, 3, 1, 2, 1, 2, 1, 2],
        [6, 6, 6, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [4, 6, 6, 6, 6, 6, 6, 2, 1, 2, 1, 2],
        [5, 5, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
        [1, 2, 3, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    ]
    result = sa.split_massages(input_messages)
    assert result == expected_chunks




