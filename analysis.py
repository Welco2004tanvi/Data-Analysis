import pandas as pd

def clean_data(data):
    data = data.dropna()  # remove nulls
    data = data[data['Rating'] > 0]  # remove zero/negative ratings
    return data

if __name__ == "__main__":
    df = pd.read_csv('data/movies.csv')
    cleaned_df = clean_data(df)
    print(cleaned_df)
