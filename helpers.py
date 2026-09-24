import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD AND CLEAN DATA
# ============================================================

def load_and_clean_data(file_path):
    """
    Load the sales CSV file, clean the data, calculate revenue,
    and return the cleaned DataFrame and a data-quality report.
    """

    # Load the CSV file
    df = pd.read_csv(file_path)

    # Record original number of rows
    original_rows = len(df)

    # --------------------------------------------------------
    # Standardise column names
    # --------------------------------------------------------

    df.columns = df.columns.str.strip().str.lower()

    # --------------------------------------------------------
    # Clean text columns
    # --------------------------------------------------------

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

    # Standardise capitalisation
    df["product_name"] = df["product_name"].str.title()
    df["category"] = df["category"].str.title()
    df["store"] = df["store"].str.title()
    df["payment_method"] = df["payment_method"].str.title()

    # --------------------------------------------------------
    # Convert quantity to numeric
    # --------------------------------------------------------

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    # Count missing quantities
    removed_missing_quantity = df["quantity"].isna().sum()

    # Remove rows with missing quantity
    df = df.dropna(subset=["quantity"])

    # --------------------------------------------------------
    # Convert unit price to numeric
    # --------------------------------------------------------

    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    # Count invalid/missing prices
    removed_invalid_price = df["unit_price"].isna().sum()

    # Remove rows with invalid/missing prices
    df = df.dropna(subset=["unit_price"])

    # --------------------------------------------------------
    # Remove negative quantities
    # --------------------------------------------------------

    negative_quantity_mask = df["quantity"] < 0

    removed_negative_quantity = negative_quantity_mask.sum()

    df = df[~negative_quantity_mask]

    # --------------------------------------------------------
    # Convert dates
    # --------------------------------------------------------

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Count invalid dates
    removed_invalid_dates = df["date"].isna().sum()

    # Remove rows with invalid dates
    df = df.dropna(subset=["date"])

    # --------------------------------------------------------
    # Remove duplicate transactions
    # --------------------------------------------------------

    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    removed_duplicates = duplicates

    # --------------------------------------------------------
    # Calculate revenue
    # --------------------------------------------------------

    df["revenue"] = (
        df["quantity"] *
        df["unit_price"]
    )

    # --------------------------------------------------------
    # Create month column
    # --------------------------------------------------------

    df["month"] = df["date"].dt.to_period("M")

    # --------------------------------------------------------
    # Final row count
    # --------------------------------------------------------

    clean_rows = len(df)

    # --------------------------------------------------------
    # Data-quality report
    # --------------------------------------------------------

    quality_report = {
        "original_rows": original_rows,
        "removed_missing_quantity": int(removed_missing_quantity),
        "removed_invalid_price": int(removed_invalid_price),
        "removed_negative_quantity": int(removed_negative_quantity),
        "removed_duplicates": int(removed_duplicates),
        "removed_invalid_dates": int(removed_invalid_dates),
        "clean_rows": clean_rows
    }

    return df, quality_report


# ============================================================
# 2. REVENUE BY CATEGORY
# ============================================================

def calculate_category_revenue(df):
    """
    Calculate total revenue for each category,
    ranked from highest to lowest.
    """

    category_revenue = (
        df.groupby("category")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_revenue


# ============================================================
# 3. REVENUE BY STORE
# ============================================================

def calculate_store_revenue(df):
    """
    Calculate total revenue for each store,
    ranked from highest to lowest.
    """

    store_revenue = (
        df.groupby("store")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return store_revenue


# ============================================================
# 4. PRODUCT QUANTITY
# ============================================================

def calculate_product_quantity(df):
    """
    Calculate total quantity sold for each product,
    ranked from highest to lowest.
    """

    product_quantity = (
        df.groupby("product_name")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    return product_quantity


# ============================================================
# 5. PRODUCT REVENUE
# ============================================================

def calculate_product_revenue(df):
    """
    Calculate total revenue for each product,
    ranked from highest to lowest.
    """

    product_revenue = (
        df.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return product_revenue


# ============================================================
# 6. MONTHLY REVENUE
# ============================================================

def calculate_monthly_revenue(df):
    """
    Calculate total revenue for each month,
    in chronological order.
    """

    monthly_revenue = (
        df.groupby("month")["revenue"]
        .sum()
        .sort_index()
    )

    return monthly_revenue


# ============================================================
# 7. PAYMENT METHOD COUNTS
# ============================================================

def calculate_payment_counts(df):
    """
    Calculate the number of transactions
    for each payment method.
    """

    payment_counts = (
        df["payment_method"]
        .value_counts()
    )

    return payment_counts


# ============================================================
# 8. QUANTITY BY CATEGORY
# ============================================================

def calculate_category_quantity(df):
    """
    Calculate total quantity sold for each category,
    ranked from highest to lowest.
    """

    category_quantity = (
        df.groupby("category")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_quantity


# ============================================================
# 9. AVERAGE UNIT PRICE BY CATEGORY
# ============================================================

def calculate_category_average_price(df):
    """
    Calculate the average unit price for each category.
    """

    category_average_price = (
        df.groupby("category")["unit_price"]
        .mean()
        .sort_values(ascending=False)
    )

    return category_average_price


# ============================================================
# 10. SAVE BAR CHART
# ============================================================

def save_bar_chart(
    data,
    title,
    xlabel,
    ylabel,
    filename
):
    """
    Create, display and save a bar chart.
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


# ============================================================
# 11. SAVE LINE CHART
# ============================================================

def save_line_chart(
    data,
    title,
    xlabel,
    ylabel,
    filename
):
    """
    Create, display and save a line chart.
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
