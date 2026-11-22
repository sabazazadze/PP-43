import pytest
from grades import get_grade


@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"),
        (91, "A"),


        (90, "B"),
        (81, "B"),


        (80, "C"),
        (71, "C"),


        (70, "D"),
        (61, "D"),


        (60, "E"),
        (51, "E"),


        (50, "F"),
        (0, "F"),
    ],
)
def test_get_grade(score, expected):
    assert get_grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101, 250])
def test_get_grade_invalid(score):
    with pytest.raises(ValueError):
        get_grade(score)