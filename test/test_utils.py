import pytest
from utils import points


@pytest.mark.parametrize("goals_1, goals_2, bet_goals_1, bet_goals_2, expected_points",
                         [(3, 2, 3, 2, 4),
                          (1, 1, 1, 1, 4),
                          (1, 1, 2, 2, 3),
                          (3, 2, 1, 0, 3),
                          (0, 1, 0, 2, 2),
                          (0, 1, 1, 0, 0),
                          (1, 1, 1, 0, 0),
                          (1, 1, 0, 1, 0)])
def test_points(goals_1, goals_2, bet_goals_1, bet_goals_2, expected_points):

    assert points(goals_1, goals_2, bet_goals_1, bet_goals_2) == expected_points
