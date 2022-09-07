import pandas as pd



data_df = pd.read_csv("simple_data.csv")
print(data_df)

data_df.to_json(r'simple_data.json',orient='columns')
