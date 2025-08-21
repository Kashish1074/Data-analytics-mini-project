# students_data_analysis.py

# ------------------------------
# Mini-Project: Students' Performance Data Analysis
# ------------------------------

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: make plots look nicer
sns.set(style="whitegrid")

# Step 2: Load Dataset
# Make sure the CSV file is in the same folder as this script
df = pd.read_csv("Student_data.csv")

# Step 3: Clean Column Names (remove spaces)
df.columns = df.columns.str.strip()

# Step 4: Explore Dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Step 5: Count of Students by Gender
print("\nCount of students by gender:")
print(df['sex'].value_counts())

# Step 6: Average Scores by Gender
avg_scores = df.groupby('sex')[['studytime','traveltime','freetime']].mean()
print("\nAverage scores by gender:")
print(avg_scores)

# Step 7: Visualizations and Saving Plots

# 7a: Distribution of Math Scores
plt.figure(figsize=(8,5))
sns.histplot(df['studytime'], bins=10, kde=True)
plt.title('Distribution of study time')
plt.xlabel('study time')
plt.ylabel('Count')
plt.savefig('hist_math_score.png')  # saves the plot as an image
plt.show() # closes the plot

# 7b: Boxplot of Math Scores by Gender
plt.figure(figsize=(8,5))
sns.boxplot(x='sex', y='studytime', data=df)
plt.title('studytime by Gender')
plt.xlabel('Gender')
plt.ylabel('study time')
plt.savefig('boxplot_math_score_gender.png')  # saves the plot
plt.show()

# 7c: Correlation Heatmap of Scores
plt.figure(figsize=(6,5))
sns.heatmap(df[['studytime','traveltime','freetime']].corr(), annot=True, cmap='coolwarm')
plt.title('Score Correlation')
plt.savefig('correlation_heatmap.png')  # saves the plot
plt.show()

print("\nAll plots have been saved as image files.")

# Step 8: Save Summary Report
summary = df.groupby('sex')[['studytime','traveltime','freetime']].mean()
summary.to_csv('summary_scores.csv')
print("\nSummary report saved as 'summary_scores.csv'")

# ------------------------------
# End of Script
# ------------------------------
