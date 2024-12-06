import pandas as pd

df = pd.read_csv('example.csv')

print("Original Dataframe")
print(df)

df['NewColumn'] = df['Age'] * 2

print("\nDataFrame with NewColumn:")
print(df)

df.to_csv('example_with_new_column.csv', index=False)