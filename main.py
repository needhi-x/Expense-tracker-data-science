import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("🚀 Expense Tracker Started...")

# -----------------------------
# CREATE SYNTHETIC DATA
# -----------------------------
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=100)

categories = ['Food', 'Travel', 'Rent', 'Shopping', 'Bills', 'Entertainment']
payment_methods = ['Cash', 'UPI', 'Card']

data = {
    "Date": np.random.choice(dates, 200),
    "Category": np.random.choice(categories, 200),
    "Amount": np.random.randint(100, 5000, 200),
    "Payment_Method": np.random.choice(payment_methods, 200)
}

# ✅ THIS LINE CREATES df
df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/expenses.csv", index=False)

# -----------------------------
# CLEANING
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
df['Month'] = df['Date'].dt.to_period('M')

# -----------------------------
# ANALYSIS
# -----------------------------
total_spend = df['Amount'].sum()
category_spend = df.groupby('Category')['Amount'].sum()
monthly_spend = df.groupby('Month')['Amount'].sum()

# -----------------------------
# OUTPUT
# -----------------------------
print("\n========== EXPENSE ANALYSIS ==========")
print("💰 Total Spending:", total_spend)


print("\n📊 Category-wise Spending:")
print("\nCategory         Spending")

for category, amount in category_spend.items():
    print(f"{category:<15} ₹{amount}")
top_category = category_spend.idxmax()
print("\n🏆 Top Spending Category:", top_category)

if category_spend.max() > 10000:
    print("⚠️ Overspending detected in:", top_category)

print("=====================================")

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure()
category_spend.plot(kind='bar')
plt.title("Category-wise Spending")
plt.tight_layout()
plt.savefig("outputs/category_spending.png")

plt.figure()
category_spend.plot(kind='pie', autopct='%1.1f%%')
plt.title("Spending Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/pie_chart.png")

plt.figure()
monthly_spend.plot()
plt.title("Monthly Spending Trend")
plt.tight_layout()
plt.savefig("outputs/monthly_trend.png")

print("\n📊 Charts saved in 'outputs' folder")
print("✅ Project executed successfully!")