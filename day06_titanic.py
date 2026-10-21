import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

# Task 1 — Explore the data

print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())

print("\nColumn names:")
print(df.columns)

print("\nData types and non-null values:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nmissing-value percentages:")
missing_percent = df.isna().mean() * 100
print(missing_percent[missing_percent > 0].round(2))


# Task 2 — Clean the data
print("\nMissing values before cleaning:")
print(df[["Age", "Fare", "Embarked", "Cabin"]].isna().sum())

clean_df = df.copy()

# Fill missing ages using the median age
clean_df["Age"] = df.Age.fillna(df["Age"].median())
print(clean_df[["Age", "Fare", "Embarked", "Cabin"]].isna().sum())

# Fill missing embarkation ports using the most frequent value
clean_df["Embarked"] = clean_df.Embarked.fillna(clean_df["Embarked"].mode()[0])

# Cabin has many missing entries; drop it for this beginner analysis
clean_df = clean_df.drop(columns=["Cabin"])

print("Missing values after cleaning:")
print(clean_df.isna().sum())

print("Original shape:", df.shape)
print("Cleaned shape:", clean_df.shape)

# Your code goes here
# clean_df.to_csv("clean_df.csv")

# Task 3 — Answer three questions with code and plots

# Question 1: What was the survival rate by gender?
survival_by_gender = (clean_df.groupby('Sex')["Survived"].mean())
print((survival_by_gender * 100).round(2))
print(clean_df.Sex.value_counts()) # it just showing no of males and females in the dataset

survival_by_gender.plot(
    kind="bar",
    color=["steelblue", "salmon"],
    rot=0
)

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("my_plot.png")

# Question 2: What does the age distribution look like?

age_distribution = clean_df.Age.value_counts()
print(age_distribution)

plt.figure(figsize=(8, 5))

sns.histplot(
    data=clean_df,
    x="Age",
    bins=25,
    kde=True
)

plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("Age_plot.png")

# Question 3: Is passenger age related to the fare paid?
print(clean_df.head())
# age_related_to_fare = clean_df.groupby('Age')["Fare"].agg(['max','min', 'count'])
age_related_to_fare = print(clean_df[["Age", "Fare"]].corr())
print(age_related_to_fare)

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=clean_df,
    x="Age",
    y="Fare",
    hue="Survived",
    alpha=0.65
)

plt.title("Passenger Age vs Fare")
plt.tight_layout()
plt.savefig("age_fare.png")

# Passenger class: Which passenger class had the highest survival rate? Use groupby() and a bar plot.

survival_rate = clean_df.groupby('Pclass')["Survived"].mean()
print(survival_rate* 100)

# Age comparison: What was the average age of survivors compared with non-survivors?
survivors_age = clean_df.groupby('Survived')["Age"].mean()
print(survivors_age)

# Fare outliers: Which passengers paid unusually high fares? Use a box plot and describe what you observe.
plt.figure(figsize=(8, 5))

sns.boxplot(data=clean_df, x="Pclass", y="Fare")

plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("fare_distribution.png")
# passengers_paid = clean_df.groupby(['Pclass', 'Sex'])["Fare"].agg(['max'])
# print(passengers_paid)