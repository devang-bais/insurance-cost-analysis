# 🩺 Insurance Cost Analysis

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) on a medical insurance dataset to understand the factors associated with insurance charges. Using Python and data visualization techniques, it explores patterns and relationships between personal attributes and medical costs.

## 🎯 Objectives
- Explore and understand the insurance dataset.
- Analyze numerical and categorical features.
- Identify missing values and duplicate records.
- Visualize relationships between different variables and insurance charges.
- Perform categorical encoding and numerical feature scaling where required.
- Prepare data for further analysis and machine learning.

## 📂 Repository Structure

```text
insurance-cost-analysis/
├── insurance.csv
├── insurance_eda_colab.ipynb
├── insurance_eda.py
└── README.md
```

## 📊 Dataset Description

The dataset contains information about individuals and their medical insurance charges.

| Feature | Description |
|---|---|
| `age` | Age of the individual |
| `sex` | Sex of the individual |
| `bmi` | Body Mass Index |
| `children` | Number of dependents |
| `smoker` | Smoking status |
| `region` | Residential region |
| `charges` | Medical insurance charges |

## 🛠️ Technologies Used
- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Scikit-learn** — Data preprocessing, where used
- **Google Colab / Jupyter Notebook** — Development environment

## 🔍 Project Workflow
1. Import required Python libraries.
2. Load and inspect the dataset.
3. Perform exploratory data analysis.
4. Generate statistical summaries and visualizations.
5. Analyze relationships between insurance charges and other features.
6. Encode categorical variables where required.
7. Scale numerical features where appropriate.

## 🚀 How to Run the Project

### Using Google Colab
1. Open `insurance_eda_colab.ipynb` in Google Colab.
2. Run the first cell to upload `insurance.csv`.
3. Select the dataset from your computer.
4. Run all notebook cells using **Runtime → Run all**.
5. Explore the analysis, charts, and results.

### Running Locally
Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Keep `insurance.csv` in the same directory as `insurance_eda.py` and execute:

```bash
python insurance_eda.py
```

## 💡 Key Insights
The notebook explores how factors such as age, BMI, smoking status, number of children, and region relate to medical insurance charges. Refer to the notebook outputs and visualizations for the actual findings.

## 📌 Project Purpose
This project was created for learning and practicing Exploratory Data Analysis, data visualization, and data preprocessing using Python.

**Note:** Observed relationships do not necessarily imply causation. This project is for educational purposes and is not intended for real-world insurance decisions.

## 👨‍💻 Author
**Devang Bais**

If you find this project useful, feel free to explore the notebook and its visualizations!
