# Step 1: Upload insurance.csv from your computer
from google.colab import files
uploaded = files.upload()

# Make sure the uploaded file is named insurance.csv.
# If your file has a different name, change the filename in pd.read_csv below.

import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings 

warnings.filterwarnings('ignore')

df = pd.read_csv('insurance.csv')

df

# # EDA

df.shape

df.head()

df.info()

df.describe()

df.isnull().sum()

df.columns

numeric_columns = ['age', 'bmi', 'children','charges']
for col in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col],kde = True,bins = 20)

sns.countplot(x = df['children'])

sns.countplot(x = df['sex'])

sns.countplot(x = df['smoker'])

for col in numeric_columns:
    plt.figure(figsize= (6,4))
    sns.boxplot(x = df[col])

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True),annot=True)

# # Data Cleaning and preprocessing

df_cleaned = df.copy()

df_cleaned.head()

df_cleaned.shape

df_cleaned.drop_duplicates(inplace = True)

df_cleaned.shape

df_cleaned.isnull().sum()

df_cleaned.dtypes

df_cleaned['sex'].value_counts()

df_cleaned['sex'] = df_cleaned['sex'].map({"male" : 0,"female" : 1})

df_cleaned.head()

df_cleaned['smoker'].value_counts()

df_cleaned['smoker'] = df_cleaned['smoker'].map({"no" : 0,"yes" : 1})

df_cleaned

df_cleaned.rename(columns={
    'sex' :'is_female',
    'smoker': 'is_smoker'
                          },inplace = True)

df_cleaned.head()

df['region'].value_counts()

df_cleaned = pd.get_dummies(df_cleaned,columns = ['region'],drop_first=True)

df_cleaned.head()

df_cleaned = df_cleaned.astype(int)

df_cleaned

# # Feature Engineering and Extraction

sns.histplot(df['bmi'])

df_cleaned['bmi_category'] = pd.cut(
    df_cleaned['bmi'],
    bins=[0, 18.5, 24.9, 29.9, float('inf')],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)

df_cleaned

df_cleaned = pd.get_dummies(df_cleaned,columns = ['bmi_category'],drop_first=True)

df_cleaned = df_cleaned.astype(int)

df_cleaned.head()

df_cleaned.columns

from sklearn.preprocessing import StandardScaler
cols = ['age','bmi','children']
scaler = StandardScaler()

df_cleaned[cols] = scaler.fit_transform(df_cleaned[cols])

df_cleaned.head()

from scipy.stats import pearsonr

# ----------------------------------
# Pearson Correlation Calculation
# ----------------------------------

# List of features to check against target
selected_features = [
    'age', 'bmi', 'children', 'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]

correlations = {
    feature: pearsonr(df_cleaned[feature], df_cleaned['charges'])[0]
    for feature in selected_features
}
correlation_df = pd.DataFrame(list(correlations.items()), columns=['Feature', 'Pearson Correlation'])
correlation_df.sort_values(by='Pearson Correlation', ascending=False)

cat_features = [
    'is_female', 'is_smoker',
    'region_northwest', 'region_southeast', 'region_southwest',
    'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese'
]

from scipy.stats import chi2_contingency
import pandas as pd

alpha = 0.05

df_cleaned['charges_bin'] = pd.qcut(df_cleaned['charges'], q=4, labels=False)
chi2_results = {}

for col in cat_features:
    contingency = pd.crosstab(df_cleaned[col], df_cleaned['charges_bin'])
    chi2_stat, p_val, _, _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else 'Accept Null (Drop Feature)'
    chi2_results[col] = {
        'chi2_statistic': chi2_stat,
        'p_value': p_val,
        'Decision': decision
    }

chi2_df = pd.DataFrame(chi2_results).T
chi2_df = chi2_df.sort_values(by='p_value')
chi2_df

final_df = df_cleaned[['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges','region_southeast','bmi_category_Obese']]

final_df

df

