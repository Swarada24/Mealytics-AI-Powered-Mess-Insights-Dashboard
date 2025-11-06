import streamlit as st
import os

# Set page config
st.set_page_config(page_title="🍽️ Mealytics Dashboard", layout="wide")

# Title and intro
st.title("🍽️ Mealytics – AI-Powered Mess Insights Dashboard")
st.markdown("Analyze daily meal performance, trends, and feedback in one place.")

# Sidebar navigation
st.sidebar.title("📊 Dashboard Navigation")
option = st.sidebar.selectbox(
    "Select a Dashboard:",
    [
        "1️⃣ Sales & Revenue",
        "2️⃣ Meal Preferences",
        "3️⃣ Feedback & Sentiment",
        "4️⃣ Insights & Recommendations"
    ]
)

# Load the selected dashboard
dashboard_dir = "dashboards"

if option == "1️⃣ Sales & Revenue":
    file_path = os.path.join(dashboard_dir, "1_Sales_and_Revenue.py")


# Run the selected dashboard
if file_path and os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()
        exec(code, globals())
else:
    st.warning("⚠️ Dashboard file not found. Please check your folder structure.")

# Footer
st.markdown("---")
st.caption("© 2025 Mealytics | Designed by Swarada Deshpande")
