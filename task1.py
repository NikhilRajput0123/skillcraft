import pandas as pd
import matplotlib.pyplot as plt

file_total_pop = 'API_SP.POP.TOTL_DS2_en_csv_v2_23043.csv'
file_pop_0_14 = 'API_SP.POP.0014.TO.ZS_DS2_en_csv_v2_22704.csv'
file_pop_15_64 = 'API_SP.POP.1564.TO.ZS_DS2_en_csv_v2_154.csv'
file_pop_65_plus = 'API_SP.POP.65UP.TO.ZS_DS2_en_csv_v2_8582.csv'

try:
    df_total_pop = pd.read_csv(file_total_pop, skiprows=4)
    df_pop_0_14 = pd.read_csv(file_pop_0_14, skiprows=4)
    df_pop_15_64 = pd.read_csv(file_pop_15_64, skiprows=4)
    df_pop_65_plus = pd.read_csv(file_pop_65_plus, skiprows=4)
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    exit()

country_name = 'India'
year = '2022'
try:
    total_pop = df_total_pop.loc[df_total_pop['Country Name'] == country_name, year].values[0]
    p_0_14 = df_pop_0_14.loc[df_pop_0_14['Country Name'] == country_name, year].values[0]
    p_15_64 = df_pop_15_64.loc[df_pop_15_64['Country Name'] == country_name, year].values[0]
    p_65_plus = df_pop_65_plus.loc[df_pop_65_plus['Country Name'] == country_name, year].values[0]
except (KeyError, IndexError):
    print(f"Error: Could not find data for '{country_name}' in the year '{year}'.")
    exit()

pop_0_14_mil = (total_pop * p_0_14 / 100) / 1000000
pop_15_64_mil = (total_pop * p_15_64 / 100) / 1000000
pop_65_plus_mil = (total_pop * p_65_plus / 100) / 1000000

age_groups_labels = [f'Ages 0-14 ({p_0_14:.1f}%)', f'Ages 15-64 ({p_15_64:.1f}%)', f'Ages 65+ ({p_65_plus:.1f}%)']
populations = [round(pop_0_14_mil), round(pop_15_64_mil), round(pop_65_plus_mil)]
colors = ['#FFD700', '#1E90FF', '#FF69B4']
x_positions = [0, 1, 2]

fig, ax = plt.subplots(figsize=(10, 7))

ax.bar(x_positions, populations, color=colors)
ax.set_xticks(x_positions)
ax.set_xticklabels(age_groups_labels)

for i, pop in enumerate(populations):
    ax.text(i, pop, f'{pop} Mn', ha='center', va='bottom', fontsize=11)

ax.set_title(f"{country_name}'s Population Distribution by Age in {year}", fontsize=16)
ax.set_ylabel("Population (in Millions)", fontsize=12)
ax.set_xlabel("Age Groups", fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_ylim(0, max(populations) * 1.1)

plt.tight_layout()
plt.savefig('final_working_chart.png')
plt.show()