import pandas as pd
import matplotlib.pyplot as plt


def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    original_rows = len(df)

    df.columns = df.columns.str.strip().str.lower()

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

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    removed_missing_quantity = df["quantity"].isna().sum()
    df = df.dropna(subset=["quantity"])

    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    removed_invalid_price = df["unit_price"].isna().sum()
    df = df.dropna(subset=["unit_price"])

    negative_quantity_mask = df["quantity"] < 0
    removed_negative_quantity = negative_quantity_mask.sum()
    df = df[~negative_quantity_mask]

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    removed_invalid_dates = df["date"].isna().sum()
    df = df.dropna(subset=["date"])

    removed_duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M")

    clean_rows = len(df)

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


def calculate_category_revenue(df):
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)


def calculate_store_revenue(df):
    return df.groupby("store")["revenue"].sum().sort_values(ascending=False)


def calculate_product_quantity(df):
    return df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)


def calculate_product_revenue(df):
    return df.groupby("product_name")["revenue"].sum().sort_values(ascending=False)


def calculate_monthly_revenue(df):
    return df.groupby("month")["revenue"].sum().sort_index()


def calculate_payment_counts(df):
    return df["payment_method"].value_counts()


def calculate_category_quantity(df):
    return df.groupby("category")["quantity"].sum().sort_values(ascending=False)


def calculate_category_average_price(df):
    return df.groupby("category")["unit_price"].mean().sort_values(ascending=False)


def save_bar_chart(data, title, xlabel, ylabel, filename):
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


def save_line_chart(data, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    data.plot(kind="line", marker="o")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    plt.close()
