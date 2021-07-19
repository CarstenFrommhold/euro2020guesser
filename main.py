""" Go for it
"""
import pandas as pd
from euroguesser.guesser import RankGuesser_1_0, RankGuesser_2_1, AgeGuesser_1_0, AgeGuesser_2_1, evaluate

export_match_excel: bool = True
date: str = "2021-07-11"

if __name__ == "__main__":

    # Load data
    fifa_ranking = pd.read_csv("data/fifa_ranking.csv")
    ages = pd.read_csv("data/ages.csv")
    matches = pd.read_excel("data/input/matches.xlsx")

    # Init stupid betters
    RankGuesser_10 = RankGuesser_1_0(fifa_ranking)
    RankGuesser_21 = RankGuesser_2_1(fifa_ranking)
    AgeGuesser_10 = AgeGuesser_1_0(ages)
    AgeGuesser_21 = AgeGuesser_2_1(ages)

    # evaluate
    matches, results = evaluate(matches, {
        "RankGuesser_10": RankGuesser_10,
        "RankGuesser_21": RankGuesser_21,
        "AgeGuesser_10": AgeGuesser_10,
        "AgeGuesser_21": AgeGuesser_21
    }, predict_only=False)

    print(results.to_markdown(index=False))

    if export_match_excel:
        matches.to_excel(f"data/evaluation/matches_{date}.xlsx")
