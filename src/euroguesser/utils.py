""" Just some utils
"""
from typing import Any
import pandas as pd
import numpy as np


def query_from_df(df: pd.DataFrame,
                  col: str,
                  search: Any,
                  select: Any) -> Any:

    result = df.loc[df[col] == search].reset_index()
    if len(result) > 1:
        raise Exception("query not unique.")
    if len(result) == 0:
        raise Exception(f"Didnt found {search} for {col}")
    result = result.at[0, select]
    return result


def points(g1, g2, b1, b2) -> int:

    if (g1 - g2) == (b1 - b2):
        if g1 == b1 and g2 == b2:
            return 4  # correct bet
        else:
            return 3 # correct difference
    elif np.sign(g1 - g2) == np.sign(b1 - b2):
        return 2  # correct tendency
    else:
        return 0


