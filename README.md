# 🍽️ Mealytics — AI-Powered Analytics Suite for Food Businesses

## 🧠 Overview
**Mealytics** is an end-to-end analytics platform designed to help food services, college messes, and restaurant chains make **data-driven decisions**.  
From monitoring daily sales to predicting future demand, Mealytics brings together **interactive dashboards**, **predictive insights**, and **smart visual analytics** — all powered by Python and modern visualization tools.

Mealytics turns raw operational data into **actionable intelligence** using intuitive, interactive dashboards built with Streamlit, Plotly, and Pandas.

---

## 🎯 Project Goals
- 📊 Provide deep insights into sales, customer behavior, and operational performance  
- 🔮 Enable predictive analysis to forecast future revenue, demand, and growth  
- 💰 Optimize resources, reduce waste, and improve profitability  
- 🧾 Automate reporting for management and administration  
- ⚙️ Offer modular dashboards for different business functions  

---

## 🧩 Core Modules (7 Dashboards)
Mealytics is divided into **7 interactive dashboards**, each serving a distinct business goal.

| # | Dashboard | Goal | Key Insights |
|:-:|------------|------|--------------|
| 1️⃣ | **Sales & Revenue Dashboard** | Track daily income, profit, and discounts | Revenue trends, top-selling items, location-wise profit |
| 2️⃣ | **Customer Segmentation Dashboard** | Understand customer demographics and preferences | Age, gender, lifestyle, repeat patterns |
| 3️⃣ | **Operational Efficiency Dashboard** | Evaluate performance and cost efficiency | Preparation time, delivery performance, resource optimization |
| 4️⃣ | **Feedback Sentiment Dashboard** | Analyze customer feedback automatically | Sentiment classification, rating distribution |
| 5️⃣ | **Funnel Analysis Dashboard** | Measure order flow and conversion rates | Drop-off points, payment success ratio |
| 6️⃣ | **Market Expansion Dashboard** | Identify opportunities for new regions | Regional demand, demographic mapping |
| 7️⃣ | **Financial Forecasting Dashboard** | Predict future sales and profits | Time-series forecasts, seasonality trends |

---

## 🧮 Dataset Schema
Mealytics uses a comprehensive dataset simulating real-world mess and food service operations.

| Column | Description |
|--------|-------------|
| `Order_ID` | Unique order identifier |
| `Date` | Date of transaction |
| `Time_of_Day` | Morning, Afternoon, Evening |
| `Day_of_Week` | Weekday indicator |
| `Meal_Type` | Breakfast, Lunch, Dinner |
| `Consumer_Type` | Student, Staff, Guest |
| `Item_Name` | Food item name |
| `Quantity` | Items sold |
| `Unit_Price` | Price per item |
| `Total_Amount` | Before discount |
| `Discount_%` | Discount offered |
| `Discount_Amount` | Discount in currency |
| `Final_Amount` | Net bill after discount |
| `Cost_of_Preparation` | Ingredient and labor cost |
| `Profit` | Final profit |
| `Calories`, `Protein_g`, `Carbs_g`, `Fats_g`, `Fiber_g` | Nutritional metrics |
| `Age`, `Gender`, `BMI`, `Lifestyle` | Customer data |
| `Location`, `Payment_Mode` | Transaction data |
| `Rating`, `Feedback_Text`, `Sentiment_Label` | Feedback data |
| `Delivery_Mode`, `Delivery_Time_min`, `Packaging_Rating`, `Delivery_Rating` | Delivery details |
| `Repeat_Customer` | Boolean flag |

---

## ⚙️ Tech Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | Streamlit / Dash (Python) |
| **Backend** | Python (Pandas, NumPy) |
| **Visualization** | Plotly / Matplotlib / Seaborn |
| **Database** | CSV / SQLite (for predictive modules) |
| **Machine Learning (Predictive Dashboards)** | Scikit-Learn, Prophet, XGBoost |
| **Data Processing** | Pandas, Numpy |
| **Deployment** | Streamlit Cloud / Localhost |
| **Version Control** | Git & GitHub |

---

## 🧱 Project Structure
mealytics/
│
├── data/
│ └── mealytics_data.csv
│
├── dashboards/
│ ├── 1_sales_revenue.py
│ ├── 2_customer_segmentation.py
│ ├── 3_operational_efficiency.py
│ ├── 4_feedback_sentiment.py
│ ├── 5_funnel_analysis.py
│ ├── 6_market_expansion.py
│ └── 7_financial_forecasting.py
│
├── utils/
│ ├── preprocessing.py
│ ├── predictive_models.py
│ └── helpers.py
│
├── app.py
├── requirements.txt
└── README.md


---

## 🧮 Key Features
- 📊 **Interactive KPIs** (Revenue, Profit, Quantity Sold, Average Rating)  
- 📈 **Real-Time Graphs** (Sales trends, product performance, location insights)  
- 🧾 **Download Section** (Export filtered datasets as CSV)  
- 🔮 **Predictive Analysis Tabs** (Forecasting & what-if simulations)  
- 🔍 **Advanced Filters** (Date, Location, Meal Type, Payment Mode)  
- 🌍 **Modular Design** (Each dashboard can run independently or as part of suite)

---

## 🔮 Predictive Analysis (Future Outcome Tab)
Each dashboard includes or will include a **Predictive Analysis section** accessible via a tab:
- **Sales Forecasting:** Predict future sales & profit using time-series modeling  
- **Customer Retention Prediction:** Classify likely repeat customers  
- **Operational Forecasting:** Predict stock or resource needs  
- **Sentiment Trends:** Anticipate feedback changes over time  

---

## 🧠 How It Works
1. **Data Ingestion:** Read and clean dataset using Pandas  
2. **Data Transformation:** Calculate metrics (profit, discounts, KPIs)  
3. **Visualization:** Render charts dynamically with Plotly  
4. **Download Section:** Export processed insights  
5. **Predictive Module (Optional):** Load trained ML models to forecast results  

---

## 💻 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/mealytics.git
cd mealytics
