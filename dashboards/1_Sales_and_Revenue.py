import pandas as pd
import streamlit as st
import numpy as np 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

@st.cache_data
# Load data
def load_data(path="data/mess_food_insights.xlsx"):
    # Read Excel file (openpyxl must be installed)
    try:
        df = pd.read_excel(path, engine="openpyxl")
    except Exception as e:
        st.error(f"Could not read data file at `{path}`. Error: {e}")
        return pd.DataFrame()
# clean column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

# Convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # make sure numeric columns are numeric
    for col in ["final_amount", "profit", "quantity", "unit_price", "total_amount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors = "coerce")
    return df


def check_required_columns(df):
    required = [ "order_id", "date", "item_name", "final_amount", "profit", "quantity"]
    missing = [c for c in required if c not in df.columns]
    return missing

st.markdown("## 📈 Sales & Revenue — Static Dashboard")
st.write("This dashboard shows revenue, profit, top items, and sales patterns. Use filters in the sidebarn to slice the data. ")

df = load_data()

if df.empty:
    st.stop()

missing = check_required_columns(df)
if missing:
    st.warning(f"The dataset is missing columns needed for this dashboard: {missing}. Displaying available data for inspeciton")
    st.dataframe(df.head())
    st.stop()
# Sidebar filters
st.sidebar.header("🔍 Filters")

#data range
min_date = df["date"].min()
max_date = df["date"].max()
date_range = st.sidebar.date_input("Date range", [min_date.date(), max_date.date()], min_value=min_date.date(), max_value=max_date.date() )

#meal type filter (if available)
meal_type_values = df["meal_type"].dropna().unique() if "meal_type" in df.columns else []
meal_types = st.sidebar.multiselect("Meal Type", options = np.sort(meal_type_values), default = list(meal_type_values))

# Consumer Type filter
consumer_values = df["consumer_type"].dropna().unique() if "consumer_type" in df.columns else []
consumers = st.sidebar.multiselect("Consumer Type", options=np.sort(consumer_values), default=list(consumer_values))

# Location filter
location_values = df["location"].dropna().unique() if "location" in df.columns else []
locations = st.sidebar.multiselect("Location", options=np.sort(location_values), default=list(location_values))

# Payment Mode filter
payment_values = df["payment_mode"].dropna().unique() if "payment_mode" in df.columns else []
payments = st.sidebar.multiselect("Payment Mode", options=np.sort(payment_values), default=list(payment_values))

# Apply filters
start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
filtered = df[(df["date"] >= start) & (df["date"] <= end)]

if "meal_type" in filtered.columns and meal_types:
    filtered = filtered[filtered["meal_type"].isin(meal_types)]
if "consumer_type" in filtered.columns and consumers:
    filtered = filtered[filtered["consumer_type"].isin(consumers)]
if "location" in filtered.columns and locations:
    filtered = filtered[filtered["location"].isin(locations)]
if "payment_mode" in filtered.columns and payments:
    filtered = filtered[filtered["payment_mode"].isin(payments)]

# -------------------------
# KPIs
# -------------------------
st.markdown("### 🔢 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

total_revenue = filtered["final_amount"].sum()
total_profit = filtered["profit"].sum() if "profit" in filtered.columns else np.nan
total_orders = filtered["order_id"].nunique()
avg_rating = filtered["rating"].mean() if "rating" in filtered.columns else np.nan
repeat_customers = None
if "repeat_customer" in filtered.columns:
    repeat_customers = (filtered["repeat_customer"].astype(str).str.lower() == "yes").sum()

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("💹 Total Profit", f"₹{total_profit:,.0f}")
col3.metric("🛒 Total Orders", f"{total_orders:,}")
if not np.isnan(avg_rating):
    col4.metric("⭐ Avg Rating", f"{avg_rating:.2f}")
else:
    col4.metric("⭐ Avg Rating", "N/A")

# optional repeat customers card (small)
if repeat_customers is not None:
    st.write(f"Repeat orders (Yes): **{repeat_customers}**")

st.markdown("---")

# -------------------------
# Chart 1: Daily revenue trend (line)
# -------------------------
st.markdown("#### 📅 Daily Revenue Trend")
daily = filtered.groupby("date", as_index=False)["final_amount"].sum().sort_values("date")
fig_line = px.line(daily, x="date", y="final_amount", markers=True, title="Daily Revenue", labels={"final_amount":"Revenue (₹)","date":"Date"})
fig_line.update_layout(margin=dict(t=40,b=10))
st.plotly_chart(fig_line, use_container_width=True)

# -------------------------
# Chart 2: Top selling items (horizontal bar)
# -------------------------
st.markdown("#### 🧾 Top Selling Items")
top_items = filtered.groupby("item_name", as_index=False)["quantity"].sum().sort_values("quantity", ascending=False).head(10)
if top_items.empty:
    st.info("No item sales in selected filters.")
else:
    fig_bar = px.bar(top_items.sort_values("quantity"), x="quantity", y="item_name", orientation="h", title="Top 10 Items by Quantity", labels={"quantity":"Quantity","item_name":"Item"})
    st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------
# Chart 3: Profit by meal type
# -------------------------
st.markdown("#### 🥗 Profit by Meal Type")
if "meal_type" in filtered.columns and "profit" in filtered.columns:
    profit_by_meal = filtered.groupby("meal_type", as_index=False)["profit"].sum().sort_values("profit", ascending=False)
    fig_profit = px.bar(profit_by_meal, x="meal_type", y="profit", title="Profit by Meal Type", labels={"profit":"Profit (₹)","meal_type":"Meal Type"})
    st.plotly_chart(fig_profit, use_container_width=True)
else:
    st.info("Profit by meal type requires 'meal_type' and 'profit' columns.")

# -------------------------
# Chart 4: Weekday heatmap (day_of_week vs meal_type) - quantity
# -------------------------
st.markdown("#### 📈 Sales Heatmap — Weekday × Meal Type")
if "day_of_week" in filtered.columns and "meal_type" in filtered.columns:
    pivot = filtered.pivot_table(index="day_of_week", columns="meal_type", values="quantity", aggfunc="sum", fill_value=0)
    # ensure weekday order:
    weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    pivot = pivot.reindex([d for d in weekday_order if d in pivot.index])
    plt.figure(figsize=(10, 4))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title("Quantity sold — Day of Week vs Meal Type")
    st.pyplot(plt.gcf())
    plt.clf()
else:
    st.info("Heatmap requires 'day_of_week', 'meal_type', and 'quantity' columns.")

# -------------------------
# Chart 5: Payment mode share (pie)
# -------------------------
st.markdown("#### 💳 Payment Mode Share")
if "payment_mode" in filtered.columns:
    pay = filtered["payment_mode"].value_counts().reset_index()
    pay.columns = ["payment_mode", "count"]
    fig_pie = px.pie(pay, names="payment_mode", values="count", title="Payment Mode Distribution", hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)
else:
    st.info("Payment mode column not found.")

# -------------------------
# Download filtered data
# -------------------------
st.markdown("---")
st.write("⬇️ Download the filtered dataset for offline reporting or further analysis.")
csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button(label="Download filtered data (CSV)", data=csv, file_name="mealytics_filtered_sales.csv", mime="text/csv")

# End of dashboard