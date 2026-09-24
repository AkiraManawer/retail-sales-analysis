# ============================================================
# RETAIL SALES ANALYSIS
# ============================================================

from helpers import (
    load_and_clean_data,
    calculate_category_revenue,
    calculate_store_revenue,
    calculate_product_quantity,
    calculate_product_revenue,
    calculate_monthly_revenue,
    calculate_payment_counts,
    calculate_category_quantity,
    calculate_category_average_price,
    save_bar_chart,
    save_line_chart
)


# ============================================================
# 1. LOAD AND CLEAN DATA
# ============================================================

file_path = "data/sales_data.csv"

df, quality_report = load_and_clean_data(file_path)


# ============================================================
# 2. DATA QUALITY REPORT
# ============================================================

print("\n" + "=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)

for key, value in quality_report.items():
    print(f"{key}: {value}")

print("=" * 60)


# ============================================================
# 3. CALCULATE RESULTS
# ============================================================

# Total revenue
total_revenue = df["revenue"].sum()

# Revenue by category
category_revenue = calculate_category_revenue(df)

# Revenue by store
store_revenue = calculate_store_revenue(df)

# Product quantity
product_quantity = calculate_product_quantity(df)

# Product revenue
product_revenue = calculate_product_revenue(df)

# Monthly revenue
monthly_revenue = calculate_monthly_revenue(df)

# Payment methods
payment_counts = calculate_payment_counts(df)

# Quantity by category
category_quantity = calculate_category_quantity(df)

# Average price by category
category_average_price = calculate_category_average_price(df)

# Average transaction value
average_transaction_value = df["revenue"].mean()


# ============================================================
# 4. PRINT DESCRIPTIVE RESULTS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE ANALYSIS")
print("=" * 60)


# ------------------------------------------------------------
# TOTAL REVENUE
# ------------------------------------------------------------

print("\n1. TOTAL REVENUE")
print("-" * 60)

print(f"Total revenue: R{total_revenue:,.2f}")

print(
    "Interpretation: The retailer generated "
    f"R{total_revenue:,.2f} in revenue across all cleaned transactions."
)


# ------------------------------------------------------------
# REVENUE BY CATEGORY
# ------------------------------------------------------------

print("\n2. REVENUE BY CATEGORY")
print("-" * 60)

print(category_revenue)

highest_category = category_revenue.idxmax()
highest_category_revenue = category_revenue.max()

print(
    f"\nInterpretation: {highest_category} generated the most revenue "
    f"at R{highest_category_revenue:,.2f}."
)


# ------------------------------------------------------------
# REVENUE BY STORE
# ------------------------------------------------------------

print("\n3. REVENUE BY STORE")
print("-" * 60)

print(store_revenue)

highest_store = store_revenue.idxmax()
highest_store_revenue = store_revenue.max()

lowest_store = store_revenue.idxmin()
lowest_store_revenue = store_revenue.min()

print(
    f"\nHighest-revenue store: {highest_store} "
    f"(R{highest_store_revenue:,.2f})"
)

print(
    f"Lowest-revenue store: {lowest_store} "
    f"(R{lowest_store_revenue:,.2f})"
)

print(
    f"Interpretation: {highest_store} generated the highest total revenue, "
    f"while {lowest_store} generated the lowest."
)


# ------------------------------------------------------------
# BEST-SELLING PRODUCT BY QUANTITY
# ------------------------------------------------------------

print("\n4. BEST-SELLING PRODUCT BY QUANTITY")
print("-" * 60)

best_quantity_product = product_quantity.idxmax()
best_quantity = product_quantity.max()

print(
    f"Product: {best_quantity_product}"
)

print(
    f"Quantity sold: {best_quantity:,.0f} units"
)

print(
    f"Interpretation: {best_quantity_product} had the highest sales "
    f"volume, with {best_quantity:,.0f} units sold."
)


# ------------------------------------------------------------
# HIGHEST-EARNING PRODUCT
# ------------------------------------------------------------

print("\n5. HIGHEST-EARNING PRODUCT BY REVENUE")
print("-" * 60)

highest_revenue_product = product_revenue.idxmax()
highest_product_revenue = product_revenue.max()

print(
    f"Product: {highest_revenue_product}"
)

print(
    f"Revenue: R{highest_product_revenue:,.2f}"
)

print(
    f"Interpretation: {highest_revenue_product} generated the most "
    f"revenue at R{highest_product_revenue:,.2f}."
)


# ------------------------------------------------------------
# MONTHLY REVENUE
# ------------------------------------------------------------

print("\n6. MONTHLY REVENUE")
print("-" * 60)

print(monthly_revenue)

highest_month = monthly_revenue.idxmax()
highest_month_revenue = monthly_revenue.max()

lowest_month = monthly_revenue.idxmin()
lowest_month_revenue = monthly_revenue.min()

print(
    f"\nHighest-revenue month: {highest_month} "
    f"(R{highest_month_revenue:,.2f})"
)

print(
    f"Lowest-revenue month: {lowest_month} "
    f"(R{lowest_month_revenue:,.2f})"
)

print(
    "Interpretation: Monthly revenue changes considerably across "
    "the period rather than following a constant pattern."
)


# ------------------------------------------------------------
# AVERAGE TRANSACTION VALUE
# ------------------------------------------------------------

print("\n7. AVERAGE TRANSACTION VALUE")
print("-" * 60)

print(
    f"Average transaction value: R{average_transaction_value:,.2f}"
)

print(
    f"Interpretation: The average cleaned transaction generated "
    f"approximately R{average_transaction_value:,.2f} in revenue."
)


# ------------------------------------------------------------
# PAYMENT METHODS
# ------------------------------------------------------------

print("\n8. PAYMENT METHODS")
print("-" * 60)

print(payment_counts)

most_common_payment = payment_counts.idxmax()
most_common_payment_count = payment_counts.max()

print(
    f"\nMost common payment method: {most_common_payment}"
)

print(
    f"Number of transactions: {most_common_payment_count}"
)

print(
    f"Interpretation: {most_common_payment} was used in the greatest "
    f"number of transactions."
)


# ============================================================
# 5. CHARTS
# ============================================================

print("\n" + "=" * 60)
print("CREATING CHARTS")
print("=" * 60)


# ------------------------------------------------------------
# CHART 1: REVENUE BY CATEGORY
# ------------------------------------------------------------

save_bar_chart(
    category_revenue,
    "Revenue by Category",
    "Category",
    "Revenue (R)",
    "charts/revenue_by_category.png"
)


# ------------------------------------------------------------
# CHART 2: REVENUE BY STORE
# ------------------------------------------------------------

save_bar_chart(
    store_revenue,
    "Revenue by Store",
    "Store",
    "Revenue (R)",
    "charts/revenue_by_store.png"
)


# ------------------------------------------------------------
# CHART 3: MONTHLY REVENUE
# ------------------------------------------------------------

save_line_chart(
    monthly_revenue,
    "Monthly Revenue Trend",
    "Month",
    "Revenue (R)",
    "charts/monthly_revenue.png"
)


# ------------------------------------------------------------
# BONUS CHART: PAYMENT METHODS
# ------------------------------------------------------------

save_bar_chart(
    payment_counts,
    "Transactions by Payment Method",
    "Payment Method",
    "Number of Transactions",
    "charts/payment_methods.png"
)


# ============================================================
# 6. CRITICAL THINKING
# ============================================================

print("\n" + "=" * 60)
print("CRITICAL THINKING AND BUSINESS INSIGHTS")
print("=" * 60)


# ------------------------------------------------------------
# QUESTION 1
# ------------------------------------------------------------

print("\nQUESTION 1")
print("-" * 60)

print(
    "Why can the best-selling product by quantity differ from "
    "the highest-earning product?"
)

print(
    f"\nTop product by quantity: {best_quantity_product}"
)

print(
    f"Quantity sold: {best_quantity:,.0f}"
)

print(
    f"\nTop product by revenue: {highest_revenue_product}"
)

print(
    f"Revenue: R{highest_product_revenue:,.2f}"
)

print(
    "\nAnswer:"
)

print(
    "The two products can be different because sales volume and "
    "selling price affect revenue in different ways. A product can "
    "sell many units but have a relatively low price, while another "
    "product can sell fewer units but generate more revenue because "
    "its price is higher."
)

print(
    f"In this dataset, {best_quantity_product} has the highest sales "
    f"volume, while {highest_revenue_product} generates the highest "
    f"revenue. This shows that the product sold in the largest "
    f"quantity is not necessarily the product generating the most money."
)


# ------------------------------------------------------------
# QUESTION 2
# ------------------------------------------------------------

print("\nQUESTION 2")
print("-" * 60)

print(
    "Is the highest-revenue category leading because it sells the "
    "most units or because its products cost more?"
)

highest_quantity_category = category_quantity.idxmax()
highest_quantity = category_quantity.max()

highest_price_category = category_average_price.idxmax()
highest_average_price = category_average_price.max()

print(
    "\nQuantity sold by category:"
)

print(category_quantity)

print(
    "\nAverage unit price by category:"
)

print(category_average_price)

print(
    "\nAnswer:"
)

print(
    f"{highest_category} is the highest-revenue category, with "
    f"R{highest_category_revenue:,.2f} in revenue."
)

print(
    f"The category with the highest quantity sold is "
    f"{highest_quantity_category}, with {highest_quantity:,.0f} units."
)

print(
    f"The category with the highest average unit price is "
    f"{highest_price_category}, at approximately "
    f"R{highest_average_price:,.2f} per unit."
)

if highest_category == highest_quantity_category:
    print(
        f"The results suggest that {highest_category}'s strong revenue "
        f"is partly supported by high sales volume because it also has "
        f"the highest quantity sold."
    )
else:
    print(
        f"The results suggest that {highest_category}'s strong revenue "
        f"is not simply because it sells the most units. "
        f"{highest_quantity_category} has the highest quantity sold, "
        f"so price differences also contribute to the revenue difference."
    )


# ------------------------------------------------------------
# QUESTION 3
# ------------------------------------------------------------

print("\nQUESTION 3")
print("-" * 60)

print(
    "What does the monthly revenue trend suggest, and what should "
    "the business investigate?"
)

first_month = monthly_revenue.index[0]
first_month_revenue = monthly_revenue.iloc[0]

last_month = monthly_revenue.index[-1]
last_month_revenue = monthly_revenue.iloc[-1]

print(
    f"\nFirst month: {first_month} "
    f"(R{first_month_revenue:,.2f})"
)

print(
    f"Last month: {last_month} "
    f"(R{last_month_revenue:,.2f})"
)

print(
    f"\nHighest month: {highest_month} "
    f"(R{highest_month_revenue:,.2f})"
)

print(
    f"Lowest month: {lowest_month} "
    f"(R{lowest_month_revenue:,.2f})"
)

print(
    "\nAnswer:"
)

print(
    "The monthly revenue trend is uneven. Revenue changes from "
    "month to month, with a particularly high month and a much "
    "lower final month."
)

print(
    "The business should investigate whether the changes are related "
    "to seasonality, promotions, stock availability, changes in "
    "customer demand, pricing, store activity, or incomplete data."
)

print(
    "The first and last months should also be checked carefully "
    "because a partial month or unusual trading conditions could "
    "make direct comparisons misleading."
)


# ------------------------------------------------------------
# QUESTION 4
# ------------------------------------------------------------

print("\nQUESTION 4")
print("-" * 60)

print(
    "Which store could be considered for investment, and what "
    "additional information would be needed?"
)

print(
    "\nStore revenue:"
)

print(store_revenue)

print(
    "\nAnswer:"
)

print(
    f"{highest_store} generated the highest revenue in this dataset, "
    f"with R{highest_store_revenue:,.2f}."
)

print(
    f"{lowest_store} generated the lowest revenue, with "
    f"R{lowest_store_revenue:,.2f}."
)

print(
    f"Revenue alone shows that {highest_store} currently generates "
    f"the most sales revenue, but revenue by itself is not enough "
    f"to determine whether an investment will produce the best return."
)

print(
    "\nBefore making an investment decision, the business should "
    "also consider:"
)

print("- Profit margins")
print("- Operating costs")
print("- Number of customers")
print("- Customer growth")
print("- Store size and capacity")
print("- Stock availability")
print("- Local competition")
print("- Historical sales trends")
print("- Marketing expenditure")


# ------------------------------------------------------------
# QUESTION 5
# ------------------------------------------------------------

print("\nQUESTION 5")
print("-" * 60)

print(
    "State one limitation of the analysis."
)

print(
    "\nAnswer:"
)

print(
    "One limitation is that the dataset mainly contains transaction "
    "information. It does not provide enough information about "
    "profit margins, operating costs, customer demographics, "
    "inventory levels, promotions, or external factors."
)

print(
    "Therefore, the analysis can describe sales revenue and sales "
    "patterns, but it cannot determine overall business profitability "
    "or the exact reasons why sales changed."
)


# ============================================================
# 7. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print(
    f"\nTotal revenue: R{total_revenue:,.2f}"
)

print(
    f"Highest-revenue category: {highest_category} "
    f"(R{highest_category_revenue:,.2f})"
)

print(
    f"Highest-revenue store: {highest_store} "
    f"(R{highest_store_revenue:,.2f})"
)

print(
    f"Best-selling product by quantity: {best_quantity_product} "
    f"({best_quantity:,.0f} units)"
)

print(
    f"Highest-earning product: {highest_revenue_product} "
    f"(R{highest_product_revenue:,.2f})"
)

print(
    f"Average transaction value: R{average_transaction_value:,.2f}"
)

print(
    f"Most common payment method: {most_common_payment}"
)

print(
    f"Highest-revenue month: {highest_month} "
    f"(R{highest_month_revenue:,.2f})"
)

print("=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60)
