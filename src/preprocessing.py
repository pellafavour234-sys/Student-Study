import pandas as pd

def load_data():

    data = pd.read_csv(
        "data/students.csv"
    )

    return data


def clean_data(data):

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Remove rows with missing values
    data = data.dropna()

    return data