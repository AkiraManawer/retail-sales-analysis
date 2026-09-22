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

# Initial data inspection

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nBasic information:")
print(df.info())

original_rows = len(df)

# Clean column names

df.columns = df.columns.str.strip().str.lower()

print("\nClean column names:")
print(df.columns.tolist())

# Clean text values

text_columns = [
    "transaction_id",
    "product_id",
    "product_name",
    "category",
    "store",
    "payment_method"
]

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()

df["product_name"] = df["product_name"].str.title()
df["category"] = df["category"].str.title()
df["store"] = df["store"].str.title()
df["payment_method"] = df["payment_method"].str.title()

print("\nText values cleaned.")

# Clean dates

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

print("\nDate column cleaned.")
print(df["date"].head())

# Clean quantity

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

missing_quantity = df["quantity"].isna().sum()

print("\nMissing quantity values:", missing_quantity)

# Clean unit price

df["unit_price"] = pd.to_numeric(
    df["unit_price"],
    errors="coerce"
)

missing_price = df["unit_price"].isna().sum()

print("Invalid/missing prices:", missing_price)

# Remove missing quantity

rows_before_quantity = len(df)

df = df.dropna(subset=["quantity"])

rows_after_quantity = len(df)

removed_quantity = (
    rows_before_quantity - rows_after_quantity
)

print(
    "Rows removed because quantity was missing:",
    removed_quantity
)

# Remove invalid prices

rows_before_price = len(df)

df = df.dropna(subset=["unit_price"])

rows_after_price = len(df)

removed_price = (
    rows_before_price - rows_after_price
)

print(
    "Rows removed because price was invalid:",
    removed_price
)

# Remove negative quantity

negative_quantity_count = (
    (df["quantity"] < 0).sum()
)

df = df[df["quantity"] >= 0]

print(
    "Rows removed because quantity was negative:",
    negative_quantity_count
)

# Remove duplicate transactions

duplicate_count = df.duplicated().sum()

df = df.drop_duplicates()

print(
    "Duplicate rows removed:",
    duplicate_count
)

# Check for invalid dates and correct

invalid_dates = df["date"].isna().sum()

print(
    "Invalid dates:",
    invalid_dates
)

rows_before_dates = len(df)

df = df.dropna(subset=["date"])

rows_after_dates = len(df)

removed_dates = rows_before_dates - rows_after_dates

print(
    "Rows removed because date was invalid:",
    removed_dates
)

# Caluclate revenue

df["revenue"] = df["quantity"] * df["unit_price"]

print("\nRevenue calculated.")
print(df[["quantity", "unit_price", "revenue"]].head())

# Data quality repor

original_rows = 600

clean_rows = len(df)

total_removed = original_rows - clean_rows

print("\n" + "=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

print("Rows originally loaded:", original_rows)
print("Rows removed - missing quantity:", removed_quantity)
print("Rows removed - invalid price:", removed_price)
print("Rows removed - negative quantity:", negative_quantity_count)
print("Rows removed - duplicates:", duplicate_count)
print("Rows removed - invalid dates:",
      removed_dates if "removed_dates" in locals() else 0)
print("Total rows removed:", total_removed)
print("Clean rows remaining:", clean_rows)

print("=" * 50)

# FInal data check

print("\nFinal data shape:")
print(df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nRemaining negative quantities:")
print((df["quantity"] < 0).sum())

print("\nFinal data preview:")
print(df.head())
