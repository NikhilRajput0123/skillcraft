import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

data_string = """
age;job;marital;education;default;balance;housing;loan;contact;day;month;duration;campaign;pdays;previous;poutcome;y
58;"management";"married";"tertiary";"no";2143;"yes";"no";"unknown";5;"may";261;1;-1;0;"unknown";"no"
44;"technician";"single";"secondary";"no";29;"yes";"no";"unknown";5;"may";151;1;-1;0;"unknown";"no"
33;"entrepreneur";"married";"secondary";"no";2;"yes";"yes";"unknown";5;"may";76;1;-1;0;"unknown";"no"
47;"blue-collar";"married";"unknown";"no";1506;"yes";"no";"unknown";5;"may";92;1;-1;0;"unknown";"no"
33;"unknown";"single";"unknown";"no";1;"no";"no";"unknown";5;"may";198;1;-1;0;"unknown";"no"
35;"management";"married";"tertiary";"no";231;"yes";"no";"unknown";5;"may";139;1;-1;0;"unknown";"no"
28;"management";"single";"tertiary";"no";447;"yes";"yes";"unknown";5;"may";217;1;-1;0;"unknown";"no"
42;"entrepreneur";"divorced";"tertiary";"yes";2;"yes";"no";"unknown";5;"may";380;1;-1;0;"unknown";"no"
58;"retired";"married";"primary";"no";121;"yes";"no";"unknown";5;"may";50;1;-1;0;"unknown";"no"
44;"technician";"single";"secondary";"no";593;"yes";"no";"unknown";5;"may";55;1;-1;0;"unknown";"no"
41;"admin.";"divorced";"secondary";"no";270;"yes";"no";"unknown";5;"may";222;1;-1;0;"unknown";"no"
29;"admin.";"single";"secondary";"no";390;"yes";"no";"unknown";5;"may";137;1;-1;0;"unknown";"no"
53;"technician";"married";"secondary";"no";6;"yes";"no";"unknown";5;"may";517;1;-1;0;"unknown";"no"
58;"technician";"married";"unknown";"no";71;"yes";"no";"unknown";5;"may";71;1;-1;0;"unknown";"no"
57;"services";"married";"secondary";"no";162;"yes";"no";"unknown";5;"may";174;1;-1;0;"unknown";"no"
51;"retired";"married";"primary";"no";229;"yes";"no";"unknown";5;"may";353;1;-1;0;"unknown";"no"
4ș;"admin.";"single";"unknown";"no";13;"yes";"no";"unknown";5;"may";98;1;-1;0;"unknown";"no"
57;"blue-collar";"married";"primary";"no";52;"yes";"no";"unknown";5;"may";38;1;-1;0;"unknown";"no"
60;"retired";"married";"primary";"no";60;"yes";"no";"unknown";5;"may";219;1;-1;0;"unknown";"no"
35;"services";"married";"secondary";"no";0;"yes";"no";"unknown";5;"may";185;1;-1;0;"unknown";"no"
28;"blue-collar";"married";"secondary";"no";723;"yes";"yes";"unknown";5;"may";262;1;-1;0;"unknown";"no"
56;"management";"married";"tertiary";"no";779;"yes";"no";"unknown";5;"may";164;1;-1;0;"unknown";"no"
32;"blue-collar";"single";"primary";"no";23;"yes";"yes";"unknown";5;"may";160;1;-1;0;"unknown";"no"
25;"services";"married";"secondary";"no";502;"yes";"no";"unknown";5;"may";341;2;-1;0;"unknown";"yes"
42;"admin.";"married";"secondary";"no";0;"yes";"yes";"unknown";5;"may";181;2;-1;0;"unknown";"no"
"""

df = pd.read_csv(io.StringIO(data_string), sep=';')

print("--- Bank Marketing Data Loaded Successfully ---")
print("First 5 rows of the dataset:")
print(df.head())

sns.set_style("whitegrid")
print("\n--- Generating and Saving Visualizations for Task-3 ---")

plt.figure(figsize=(7, 5))
sns.countplot(x='y', data=df, palette='viridis')
plt.title('Distribution of Term Deposit Subscription', fontsize=14)
plt.xlabel('Subscribed to Term Deposit? (y)')
plt.ylabel('Count of Clients')
plt.savefig('1_subscription_distribution.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='job', data=df, palette='plasma', order = df['job'].value_counts().index)
plt.title('Distribution of Client Job Types', fontsize=14)
plt.xlabel('Job Type')
plt.ylabel('Count of Clients')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('2_job_distribution.png')
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='marital', data=df, palette='magma')
plt.title('Distribution of Marital Status', fontsize=14)
plt.xlabel('Marital Status')
plt.ylabel('Count of Clients')
plt.savefig('3_marital_status_distribution.png')
plt.show()

plt.figure(figsize=(9, 5))
sns.countplot(x='education', data=df, palette='cividis', order = df['education'].value_counts().index)
plt.title('Distribution of Education Level', fontsize=14)
plt.xlabel('Education Level')
plt.ylabel('Count of Clients')
plt.savefig('4_education_level_distribution.png')
plt.show()

numerical_cols = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(14, 10))
sns.heatmap(numerical_cols.corr(), cmap='coolwarm', annot=True, fmt='.2f')
plt.title('Correlation Heatmap of Numerical Features', fontsize=16)
plt.savefig('5_correlation_heatmap.png')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='y', y='age', data=df, palette='pastel')
plt.title('Age Distribution by Subscription Status', fontsize=14)
plt.xlabel('Subscribed to Term Deposit? (y)')
plt.ylabel('Age of Client')
plt.savefig('6_age_vs_subscription_boxplot.png')
plt.show()

print("\n--- All visualizations for Task-3 have been saved successfully! ---")