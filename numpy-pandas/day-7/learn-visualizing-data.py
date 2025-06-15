# ✅ Visualizing Data Using matplotlib and seaborn

# Visualization helps in understanding trends, patterns, and anomalies in data — and both Matplotlib and Seaborn are essential for this in the Python ecosystem.

# 📊 Why use them?
# | Tool         | Strengths                                    |
# | ------------ | -------------------------------------------- |
# | `matplotlib` | Low-level control, customizable plots        |
# | `seaborn`    | High-level API, attractive statistical plots |

# 🔧 Setup
# pip install matplotlib seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 🧪 Example 1: Matplotlib – Basic Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

plt.plot(x, y)
plt.title("Line Chart Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# 🧪 Example 2: Pandas Integration with Matplotlib
df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'sales': [250, 300, 280, 500]
})

df.plot(x='month', y='sales', kind='bar', title="Monthly Sales")
plt.ylabel("Sales Amount")
plt.show()

# 🧪 Example 3: Seaborn – Histogram & Countplot
tips = sns.load_dataset("tips")

# Distribution plot (histogram + KDE)
sns.histplot(tips['total_bill'], kde=True)
plt.title("Total Bill Distribution")
plt.show()

# Countplot (like bar chart for categorical data)
sns.countplot(x="day", data=tips)
plt.title("Count of Tips by Day")
plt.show()

# 🧪 Example 4: Seaborn – Boxplot & Heatmap
# Boxplot showing bill by gender
sns.boxplot(x='sex', y='total_bill', data=tips)
plt.title("Boxplot: Total Bill by Sex")
plt.show()

# Correlation heatmap
sns.heatmap(tips.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 🧠 Best Practices
# Use seaborn for quick and pretty plots.
# Use matplotlib when you need more customization and control.
# Use .plot() directly on Pandas DataFrames for simple visualizations.

