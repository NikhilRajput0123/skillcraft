import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('train.csv')
except FileNotFoundError:
    print("ERROR: 'train.csv' file not found. Please place the file in the correct directory.")
    exit()

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Has_Cabin'] = df['Cabin'].notna().astype(int)
df.drop('Cabin', axis=1, inplace=True)
df.drop(['Name', 'Ticket'], axis=1, inplace=True)
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

print("--- Data after Cleaning ---")
print(df.head())
print("\n--- Missing values check ---")
print(df.isnull().sum())

sns.set_style("whitegrid")

plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Features', fontsize=16)
plt.savefig('correlation_heatmap.png')
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x='Sex', y='Survived', data=df, palette='plasma')
plt.title('Survival Rate by Gender', fontsize=14)
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])
plt.savefig('survival_by_gender.png')
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x='Pclass', y='Survived', data=df, palette='viridis')
plt.title('Survival Rate by Passenger Class (Pclass)', fontsize=14)
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.savefig('survival_by_pclass.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df[df['Survived']==1]['Age'], bins=30, kde=True, color='green', label='Survived', alpha=0.7)
sns.histplot(df[df['Survived']==0]['Age'], bins=30, kde=True, color='red', label='Did Not Survive', alpha=0.7)
plt.title('Age Distribution by Survival Status', fontsize=14)
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.legend()
plt.savefig('age_distribution.png')
plt.show()

plt.figure(figsize=(7, 5))
sns.barplot(x='Has_Cabin', y='Survived', data=df, palette='magma')
plt.title('Survival Rate by Having a Cabin', fontsize=14)
plt.ylabel('Survival Rate')
plt.xlabel('Had a Cabin')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.savefig('survival_by_cabin.png')
plt.show()

print("\n--- Key EDA Findings ---")
overall_survival = df['Survived'].mean() * 100
print(f"Overall Survival Rate: {overall_survival:.2f}%")
print("\nSurvival Rate by Sex:")
print(df.groupby('Sex')['Survived'].mean().map('{:.2%}'.format).rename({0: 'Male', 1: 'Female'}))
print("\nSurvival Rate by Pclass:")
print(df.groupby('Pclass')['Survived'].mean().map('{:.2%}'.format))
print("\nSurvival Rate based on Having a Cabin:")
print(df.groupby('Has_Cabin')['Survived'].mean().map('{:.2%}'.format).rename({0: 'No Cabin', 1: 'Has Cabin'}))