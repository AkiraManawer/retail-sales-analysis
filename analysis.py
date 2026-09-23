import pandas as pd
import matplotlib.pyplot as plt

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

# Clen unit price
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

###########
# Descriptive analysis
###########

# Total Revnue
total_revenue = df["revenue"].sum()
print("\nTOTAL REVENUE")
print(f"R{total_revenue:,.2f}")

# Revenue by category
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nREVENUE BY CATEGORY")
print(category_revenue)

# Revenue by store
store_revenue = (
    df.groupby("store")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nREVENUE BY STORE")
print(store_revenue)

best_store = store_revenue.idxmax()
best_store_revenue = store_revenue.max()
worst_store = store_revenue.idxmin()
worst_store_revenue = store_revenue.min()

print("\nBEST STORE")
print(best_store)
print(f"Revenue: R{best_store_revenue:,.2f}")
print("\nLOWEST-REVENUE STORE")
print(worst_store)
print(f"Revenue: R{worst_store_revenue:,.2f}")

# Best-selling product by quantity
product_quantity = (
    df.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)
top_quantity_product = product_quantity.idxmax()
top_quantity_value = product_quantity.max()
print("\nBEST-SELLING PRODUCT BY QUANTITY")
print(top_quantity_product)
print(f"Units sold: {top_quantity_value}")

# Highest earning product by revenue
product_quantity = (
    df.groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)
top_quantity_product = product_quantity.idxmax()
top_quantity_value = product_quantity.max()
print("\nBEST-SELLING PRODUCT BY QUANTITY")
print(top_quantity_product)
print(f"Units sold: {top_quantity_value}")

# Highest earning product by revenue
product_revenue = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
top_revenue_product = product_revenue.idxmax()
top_revenue_value = product_revenue.max()

print("\nHIGHEST-EARNING PRODUCT BY REVENUE")
print(top_revenue_product)
print(f"Revenue: R{top_revenue_value:,.2f}")

# MOnthly revenue
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
)
print("\nMONTHLY REVENUE")
print(monthly_revenue)

# Average transaction value
average_transaction_value = df["revenue"].mean()
print("\nAVERAGE TRANSACTION VALUE")
print(f"R{average_transaction_value:,.2f}")

# Payment method
payment_counts = (
    df["payment_method"]
    .value_counts()
)
most_common_payment = payment_counts.idxmax()
most_common_payment_count = payment_counts.max()
print("\nMOST COMMON PAYMENT METHOD")
print(most_common_payment)
print(f"Transactions: {most_common_payment_count}")

# Summary
print("\n" + "=" * 60)
print("KEY RESULTS SUMMARY")
print("=" * 60)

print(f"Total revenue: R{total_revenue:,.2f}")
print(f"Highest-revenue category: {category_revenue.idxmax()}")
print(f"Best store: {best_store}")
print(f"Lowest-revenue store: {worst_store}")
print(f"Top product by quantity: {top_quantity_product}")
print(f"Top product by revenue: {top_revenue_product}")
print(f"Average transaction value: R{average_transaction_value:,.2f}")
print(f"Most common payment method: {most_common_payment}")

print("=" * 60)

# Revenue chart - catgeory
plt.figure(figsize=(10, 6))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (R)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/revenue_by_category.png"
)
plt.show()
plt.close()

# Revenue chart - store
plt.figure(figsize=(10, 6))
store_revenue.plot(kind="bar")
plt.title("Revenue by Store")
plt.xlabel("Store")
plt.ylabel("Revenue (R)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(
    "charts/revenue_by_store.png"
)
plt.show()
plt.close()

# Revenue chart - MOnthly
plt.figure(figsize=(10, 6))
monthly_revenue.plot(
    kind="line",
    marker="o"
)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (R)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(
    "charts/monthly_revenue.png"
)
plt.show()
plt.close()

# chart - payment method
plt.figure(figsize=(10, 6))
payment_counts.plot(kind="bar")
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(
    "charts/revenue_by_payment_method.png"
)
plt.show()
plt.close()


##### Question 1 #####
plt.figure(figsize=(10, 6))
payment_counts.plot(kind="bar")
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(
    "charts/revenue_by_payment_method.png"
)
plt.show()
plt.close()

##### Question 2 #####
category_quantity = (
    df.groupby("category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)
print("\nCATEGORY QUANTITY")
print(category_quantity)

category_average_price = (
    df.groupby("category")["unit_price"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVERAGE UNIT PRICE BY CATEGORY")
print(category_average_price)

##### Question 3 #####
category_average_price = (
    df.groupby("category")["unit_price"]
    .mean()
    .sort_values(ascending=False)
)
print("\nAVERAGE UNIT PRICE BY CATEGORY")
print(category_average_price)
first_month = monthly_revenue.index[0]
last_month = monthly_revenue.index[-1]

first_month_revenue = monthly_revenue.iloc[0]
last_month_revenue = monthly_revenue.iloc[-1]

print("\nFIRST MONTH")
print(first_month)
print(f"Revenue: R{first_month_revenue:,.2f}")
print("\nLAST MONTH")
print(last_month)
print(f"Revenue: R{last_month_revenue:,.2f}")

##### Question 4 #####
first_month = monthly_revenue.index[0]
last_month = monthly_revenue.index[-1]

first_month_revenue = monthly_revenue.iloc[0]
last_month_revenue = monthly_revenue.iloc[-1]

print("\nFIRST MONTH")
print(first_month)
print(f"Revenue: R{first_month_revenue:,.2f}")

print("\nLAST MONTH")
print(last_month)
print(f"Revenue: R{last_month_revenue:,.2f}")
store_quantity = (
    df.groupby("store")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUANTITY BY STORE")
print(store_quantity)
