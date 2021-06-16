""" These are some simple betters
"""
import abc
from typing import Dict
import pandas as pd
from euroguesser.utils import query_from_df, points


class GuesserBase(abc.ABC):

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def bet(self, **kwargs) -> [int, int]:
        pass


class RankGuesserBase(GuesserBase):

    def __init__(self, fifa_ranking: pd.DataFrame):
        super().__init__()
        self.fifa_ranking = fifa_ranking

    def get_scores(self, team_1, team_2):
        score_1 = query_from_df(self.fifa_ranking, "Team", team_1, "total_points")
        score_2 = query_from_df(self.fifa_ranking, "Team", team_2, "total_points")
        return score_1, score_2

    def bet(self, **kwargs):
        pass


class RankGuesser_1_0(RankGuesserBase):

    def __init__(self, fifa_ranking: pd.DataFrame):
        super().__init__(fifa_ranking)

    def bet(self, team_1, team_2) -> [int, int]:

        score_1, score_2 = self.get_scores(team_1, team_2)
        if score_1 > score_2:
            return (1, 0)
        elif score_1 < score_2:
            return (0, 1)
        else:
            return (1, 1)


class RankGuesser_2_1(RankGuesserBase):

    def __init__(self, fifa_ranking: pd.DataFrame):
        super().__init__(fifa_ranking)

    def bet(self, team_1, team_2) -> [int, int]:

        score_1, score_2 = self.get_scores(team_1, team_2)
        if score_1 > score_2:
            return (2, 1)
        elif score_1 < score_2:
            return (1, 2)
        else:
            return (1, 1)


class AgeGuesserBase(GuesserBase):

    def __init__(self, ages: pd.DataFrame):
        super().__init__()
        self.ages = ages

    def get_scores(self, team_1, team_2):
        score_1 = query_from_df(self.ages, "Team", team_1, "Age")
        score_2 = query_from_df(self.ages, "Team", team_2, "Age")
        return score_1, score_2

    def bet(self, **kwargs):
        pass


class AgeGuesser_1_0(AgeGuesserBase):

    def __init__(self, age: pd.DataFrame):
        super().__init__(age)

    def bet(self, team_1, team_2) -> [int, int]:

        score_1, score_2 = self.get_scores(team_1, team_2)
        if score_1 > score_2:
            return (1, 0)
        elif score_1 < score_2:
            return (0, 1)
        else:
            return (1, 1)


class AgeGuesser_2_1(AgeGuesserBase):

    def __init__(self, age: pd.DataFrame):
        super().__init__(age)

    def bet(self, team_1, team_2) -> [int, int]:

        score_1, score_2 = self.get_scores(team_1, team_2)
        if score_1 > score_2:
            return (2, 1)
        elif score_1 < score_2:
            return (1, 2)
        else:
            return (1, 1)


def evaluate(matches: pd.DataFrame,
             betters: Dict[str, GuesserBase],
             predict_only: bool = False) -> [pd.DataFrame, pd.DataFrame]:

    """ Evaluate already played matches and given betters.
    """

    # Only take already played matches into account
    if not predict_only:
        matches = matches.loc[~matches["Goals Team 1"].isnull()]

    guesser_performances = {}

    for guesser_name, guesser in betters.items():

        # Bet
        matches[f"{guesser_name} Bet Goals 1"] = matches.apply(
            lambda row: guesser.bet(row["Team 1"], row["Team 2"])[0], axis=1)
        matches[f"{guesser_name} Bet Goals 2"] = matches.apply(
            lambda row: guesser.bet(row["Team 1"], row["Team 2"])[1], axis=1)

        if not predict_only:

            # Get Points
            matches[f"{guesser_name} Points"] = matches.apply(
                lambda row: points(row["Goals Team 1"],
                                   row["Goals Team 2"],
                                   row[f"{guesser_name} Bet Goals 1"],
                                   row[f"{guesser_name} Bet Goals 2"]), axis=1
            )

            # Save in dict
            guesser_performances[guesser_name] = matches[f"{guesser_name} Points"].sum()

    # Format results
    results = pd.DataFrame(guesser_performances.items())
    if not predict_only:
        results.columns = ["Guesser", "Points"]
        results = results.sort_values(by=["Points"], ascending=False)

    return matches, results