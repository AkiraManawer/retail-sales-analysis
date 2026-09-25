import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean_data(file_path):
    """
    Load the sales CSV file and clean the data.
    """

    df = pd.read_csv(file_path)

    original_rows = len(df)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Track cleaning counts
    removed_missing_quantity = 0
    removed_invalid_price = 0
    removed_negative_quantity = 0
    removed_duplicates = 0
    removed_invalid_dates = 0

    # Clean text columns
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

    # Clean dates
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    invalid_dates_before = df["date"].isna().sum()

    df = df.dropna(subset=["date"])

    removed_invalid_dates = invalid_dates_before

    # Clean quantity
    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    missing_quantity = df["quantity"].isna().sum()

    df = df.dropna(subset=["quantity"])

    removed_missing_quantity = missing_quantity

    # Clean price
    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    invalid_price = df["unit_price"].isna().sum()

    df = df.dropna(subset=["unit_price"])

    removed_invalid_price = invalid_price

    # Remove negative quantities
    negative_quantity = (
        df["quantity"] < 0
    ).sum()

    df = df[df["quantity"] >= 0]

    removed_negative_quantity = negative_quantity

    # Remove duplicates
    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    removed_duplicates = duplicates

    # Calculate revenue
    df["revenue"] = (
        df["quantity"] *
        df["unit_price"]
    )

    # Create month
    df["month"] = df["date"].dt.to_period("M")

    clean_rows = len(df)

    quality_report = {
        "original_rows": original_rows,
        "removed_missing_quantity": removed_missing_quantity,
        "removed_invalid_price": removed_invalid_price,
        "removed_negative_quantity": removed_negative_quantity,
        "removed_duplicates": removed_duplicates,
        "removed_invalid_dates": removed_invalid_dates,
        "clean_rows": clean_rows
    }

    return df, quality_report


def load_and_clean_data(file_path):
    """
    Load the sales CSV file and clean the data.
    """

    df = pd.read_csv(file_path)

    original_rows = len(df)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Track cleaning counts
    removed_missing_quantity = 0
    removed_invalid_price = 0
    removed_negative_quantity = 0
    removed_duplicates = 0
    removed_invalid_dates = 0

    # Clean text columns
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

    # Clean dates
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    invalid_dates_before = df["date"].isna().sum()

    df = df.dropna(subset=["date"])

    removed_invalid_dates = invalid_dates_before

    # Clean quantity
    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    missing_quantity = df["quantity"].isna().sum()

    df = df.dropna(subset=["quantity"])

    removed_missing_quantity = missing_quantity

    # Clean price
    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    invalid_price = df["unit_price"].isna().sum()

    df = df.dropna(subset=["unit_price"])

    removed_invalid_price = invalid_price

    # Remove negative quantities
    negative_quantity = (
        df["quantity"] < 0
    ).sum()

    df = df[df["quantity"] >= 0]

    removed_negative_quantity = negative_quantity

    # Remove duplicates
    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    removed_duplicates = duplicates

    # Calculate revenue
    df["revenue"] = (
        df["quantity"] *
        df["unit_price"]
    )

    # Create month
    df["month"] = df["date"].dt.to_period("M")

    clean_rows = len(df)

    quality_report = {
        "original_rows": original_rows,
        "removed_missing_quantity": removed_missing_quantity,
        "removed_invalid_price": removed_invalid_price,
        "removed_negative_quantity": removed_negative_quantity,
        "removed_duplicates": removed_duplicates,
        "removed_invalid_dates": removed_invalid_dates,
        "clean_rows": clean_rows
    }

    return df, quality_report


def save_bar_chart(
    data,
    title,
    xlabel,
    ylabel,
    filename
):
    """
    Create and save a bar chart.
    """

    plt.figure(figsize=(10, 6))

    data.plot(kind="bar")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(filename)

    plt.show()
    plt.close()

    def save_line_chart(
        data,
        title,
        xlabel,
        ylabel,
        filename
    ):
        """
        Create and save a line chart.
        """

    plt.figure(figsize=(10, 6))

    data.plot(
        kind="line",
        marker="o"
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(filename)

    plt.show()
    plt.close()

# 3
# ============================================
# 1. LOAD AND CLEAN DATA
# ============================================


file_path = "data/sales_data.csv"

df, quality_report = load_and_clean_data(
    file_path
)
print("\n" + "=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

for key, value in quality_report.items():
    print(f"{key}: {value}")

print("=" * 50)
print("\n" + "=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

for key, value in quality_report.items():
    print(f"{key}: {value}")

print("=" * 50)
# ============================================
# 2. CALCULATE RESULTS
# ============================================

total_revenue = df["revenue"].sum()

category_revenue = calculate_category_revenue(df)

store_revenue = calculate_store_revenue(df)

product_quantity = calculate_product_quantity(df)

product_revenue = calculate_product_revenue(df)

monthly_revenue = calculate_monthly_revenue(df)

payment_counts = calculate_payment_counts(df)
# ============================================
# 3. PRINT RESULTS
# ============================================

print("\nTOTAL REVENUE")
print(f"R{total_revenue:,.2f}")

print("\nREVENUE BY CATEGORY")
print(category_revenue)

print("\nREVENUE BY STORE")
print(store_revenue)

print("\nBEST-SELLING PRODUCT BY QUANTITY")
print(product_quantity.head(1))

print("\nHIGHEST-EARNING PRODUCT")
print(product_revenue.head(1))

print("\nMONTHLY REVENUE")
print(monthly_revenue)

average_transaction_value = df["revenue"].mean()

print("\nAVERAGE TRANSACTION VALUE")
print(f"R{average_transaction_value:,.2f}")

print("\nPAYMENT METHODS")
print(payment_counts)

print(
    "\nMOST COMMON PAYMENT METHOD:",
    payment_counts.idxmax()
)
# ============================================
# 4. CRITICAL THINKING DATA
# ============================================

category_quantity = (
    df.groupby("category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

category_average_price = (
    df.groupby("category")["unit_price"]
    .mean()
    .sort_values(ascending=False)
)

store_quantity = (
    df.groupby("store")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

store_average_transaction = (
    df.groupby("store")["revenue"]
    .mean()
    .sort_values(ascending=False)
)

print("\nCATEGORY QUANTITY")
print(category_quantity)

print("\nCATEGORY AVERAGE PRICE")
print(category_average_price)

print("\nSTORE QUANTITY")
print(store_quantity)

print("\nSTORE AVERAGE TRANSACTION VALUE")
print(store_average_transaction)
# ============================================
# 5. CHARTS
# ============================================

save_bar_chart(
    category_revenue,
    "Revenue by Category",
    "Category",
    "Revenue (R)",
    "charts/revenue_by_category.png"
)

save_bar_chart(
    store_revenue,
    "Revenue by Store",
    "Store",
    "Revenue (R)",
    "charts/revenue_by_store.png"
)

save_line_chart(
    monthly_revenue,
    "Monthly Revenue Trend",
    "Month",
    "Revenue (R)",
    "charts/monthly_revenue.png"
)

save_bar_chart(
    payment_counts,
    "Transactions by Payment Method",
    "Payment Method",
    "Number of Transactions",
    "charts/revenue_by_payment_method.png"
)
# ============================================
# 6. CRITICAL THINKING RESULTS
# ============================================

print("\n" + "=" * 60)
print("CRITICAL THINKING RESULTS")
print("=" * 60)

print(
    "\nTop product by quantity:",
    product_quantity.idxmax()
)

print(
    "Top product by revenue:",
    product_revenue.idxmax()
)

print(
    "\nHighest-revenue category:",
    category_revenue.idxmax()
)

print(
    "Highest-quantity category:",
    category_quantity.idxmax()
)

print(
    "\nFirst month:",
    monthly_revenue.index[0],
    f"R{monthly_revenue.iloc[0]:,.2f}"
)

print(
    "Last month:",
    monthly_revenue.index[-1],
    f"R{monthly_revenue.iloc[-1]:,.2f}"
)

print(
    "\nHighest-revenue store:",
    store_revenue.idxmax()
)

print(
    "Lowest-revenue store:",
    store_revenue.idxmin()
)

print("=" * 60)
