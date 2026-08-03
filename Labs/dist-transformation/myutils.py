import pandas as pd
import numpy as np


def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    rows = []
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        n_unique = df[col].nunique()
        if n_unique <= 2 or n_unique == len(df):
            continue

        skewness = df[col].skew()

        if skewness < -1:
            degree, direction = 'Highly Skewed', 'Left'
        elif skewness < -0.5:
            degree, direction = 'Moderately Skewed', 'Left'
        elif skewness <= 0.5:
            degree, direction = 'Normal', 'Symmetrical'
        elif skewness <= 1:
            degree, direction = 'Moderately Skewed', 'Right'
        else:
            degree, direction = 'Highly Skewed', 'Right'

        min_val = df[col].min()


        if degree == 'Normal':
            transformation = 'None'
        elif direction == 'Right' and min_val == 0:
            transformation = 'Log Plus One'
        elif min_val < 0:
            transformation = 'Yeo-Johnson'
        else:
            transformation = 'Box-Cox'

        rows.append({
            'Feature': col,
            'Skewness': skewness,
            'Degree': degree,
            'Direction': direction,
            'Recommended Transformation': transformation
        })

    return pd.DataFrame(rows)
