# SLEEP PATTERNS AND SCREEN TIME ANALYSIS USING PYTHON
# Simulated teaching data for demonstration; NOT a real student survey.

from pathlib import Path
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

start_time = time.time()

# 1. Load the dataset. In Colab, upload sleep_screen_time_data.csv via the Files panel first.
candidates = [Path('/content/sleep_screen_time_data.csv'), Path.cwd() / 'sleep_screen_time_data.csv']
# For a local .py run, also look beside this script.
try:
    candidates.append(Path(__file__).resolve().parent / 'sleep_screen_time_data.csv')
except NameError:
    pass
file_path = next((p for p in candidates if p.exists()), None)
if file_path is None:
    raise FileNotFoundError(
        'Cannot find sleep_screen_time_data.csv. In Google Colab, open the Files panel '
        'on the left and upload that CSV, then rerun this cell. For local Python, keep the '
        'CSV in the same folder as this script/notebook.'
    )

print(f'Loading dataset from: {file_path}')
df = pd.read_csv(file_path)
print('\nRAW DATA PREVIEW')
display(df.head())
print('Original shape (rows, columns):', df.shape)

# 2. Inspect and clean the data
print('\nMissing values before cleaning:')
print(df.isnull().sum())
print('\nDuplicate rows before cleaning:', df.duplicated().sum())

df = df.drop_duplicates().copy()

numeric_cols = [
    'Study_Hours',
    'Screen_Time_Hours',
    'Sleep_Hours',
    'Concentration_Score',
    'Physical_Activity_Minutes',
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    if df[col].notna().any():
        df[col] = df[col].fillna(df[col].median())

print('\nCleaned shape (rows, columns):', df.shape)
print('Missing values after cleaning:')
print(df.isnull().sum())

# 3. Numerical analysis using NumPy
sleep = df['Sleep_Hours'].to_numpy(dtype=float)
screen = df['Screen_Time_Hours'].to_numpy(dtype=float)
focus = df['Concentration_Score'].to_numpy(dtype=float)

print('\nNUMERICAL SUMMARY')
print(f'Average sleep: {np.mean(sleep):.2f} hours')
print(f'Minimum sleep: {np.min(sleep):.2f} hours')
print(f'Maximum sleep: {np.max(sleep):.2f} hours')
print(f'Sleep standard deviation: {np.std(sleep):.2f} hours')
print(f'Average screen time: {np.mean(screen):.2f} hours/day')
print(f'Average concentration score: {np.mean(focus):.2f}/100')
print(f'Total physical activity: {np.sum(df["Physical_Activity_Minutes"].to_numpy(dtype=float)):.0f} minutes')

correlation = df[numeric_cols].corr(numeric_only=True)
print('\nCORRELATION MATRIX')
display(correlation.round(2))

# 4. Visualizations. Each figure is closed after display to keep memory usage low.
sns.set_theme(style='whitegrid')

plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='Screen_Time_Hours', y='Sleep_Hours',
            scatter_kws={'alpha': 0.7}, line_kws={'color': 'red'}, ci=None)
plt.title('Screen Time vs Sleep Duration')
plt.xlabel('Screen Time (hours per day)')
plt.ylabel('Sleep Duration (hours per night)')
plt.tight_layout()
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(df['Sleep_Hours'], bins=12, edgecolor='black')
plt.title('Distribution of Sleep Duration')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Number of Records')
plt.tight_layout()
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
means = [df['Sleep_Hours'].mean(), df['Screen_Time_Hours'].mean(), df['Study_Hours'].mean()]
plt.bar(['Sleep', 'Screen time', 'Study'], means)
plt.title('Average Daily Hours by Activity')
plt.ylabel('Average hours')
plt.tight_layout()
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Sleep_Hours', y='Concentration_Score')
plt.title('Sleep Duration vs Concentration Score')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Concentration Score (out of 100)')
plt.tight_layout()
plt.show()
plt.close()

plt.figure(figsize=(9, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Between Student Lifestyle Variables')
plt.tight_layout()
plt.show()
plt.close()

print(f'\nProject complete! Five graphs were displayed in {time.time() - start_time:.1f} seconds.')
print('Reminder: These are simulated teaching data, not a real student survey.')
