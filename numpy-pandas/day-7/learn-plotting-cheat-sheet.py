# 📊 Plotting Cheat Sheet: Matplotlib, Seaborn, Pandas

# 🔹 1. Line Plot
# Trend over time or sequence
# plt.plot(x, y)
# sns.lineplot(x=x, y=y)
# df.plot(kind='line')

# 🔹 2. Bar Chart
# Category vs Value
# plt.bar(x, height)
# sns.barplot(x='category', y='value', data=df)
# df.plot(kind='bar')

# 🔹 3. Horizontal Bar Chart
# plt.barh(x, width)
# df.plot(kind='barh')

# 🔹 4. Histogram
# Distribution of numeric data
# plt.hist(df['column'])
# sns.histplot(df['column'], bins=20, kde=True)
# df['column'].plot(kind='hist')


# 🔹 5. Box Plot
# Spread and outliers
# sns.boxplot(x='category', y='value', data=df)

# 🔹 6. Scatter Plot
# Relationship between two numeric variables
# plt.scatter(x, y)
# sns.scatterplot(x='col1', y='col2', data=df)
# df.plot(kind='scatter', x='col1', y='col2')

# 🔹 7. Count Plot
# Frequency of categorical values
# sns.countplot(x='category', data=df)

# 🔹 8. Pair Plot
# All pairwise scatter plots + histograms
# sns.pairplot(df)

# 🔹 9. Heatmap
# Matrix of values (correlation, confusion matrix)
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# 🔹 10. Pie Chart (Pandas only, not preferred for analysis)
# df['column'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# 🧠 Pro Tips:
# Use plt.tight_layout() to fix overlapping labels
# Combine Pandas .plot() with matplotlib.pyplot for full control
# Use sns.set(style="whitegrid") for clean Seaborn visuals