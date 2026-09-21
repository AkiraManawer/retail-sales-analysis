import pandas as pd

# Load the data

file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)
print("Original data:")
print(df.head())

print("\nOriginal shape:")
print(df.shape)

print("\nCOlumn names:")
print(df.columns.tolist())
