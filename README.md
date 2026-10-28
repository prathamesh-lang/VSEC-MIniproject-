# VSEC-MIniproject-

# 🌙 Sleep Patterns & Screen Time Analysis Using Python

<p align="center">
  <strong>Turning everyday digital habits into data-driven insights.</strong>
</p>

<p align="center">
  A Data Analysis & Visualization Mini Project
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge" alt="Seaborn">
</p>

---

## 📌 Project Overview

**Sleep Patterns & Screen Time Analysis Using Python** is a mini project that demonstrates how data analysis can be used to explore relationships between screen time, sleep duration, study hours, physical activity, and concentration scores.

The project follows a complete data-analysis workflow: importing a dataset, cleaning inconsistent or incomplete records, calculating statistical summaries, examining correlations, and visualizing the results through meaningful graphs.

The goal is to transform raw data into understandable insights using Python's data analysis and visualization libraries.

> **Project focus:** Data Cleaning • Numerical Analysis • Correlation • Data Visualization

## 🎯 Objectives

- Clean and prepare a dataset using **Pandas**.
- Calculate statistical measures using **NumPy**.
- Explore relationships between screen time, sleep duration, and concentration.
- Create clear and informative visualizations using **Matplotlib** and **Seaborn**.
- Interpret the results and understand the limitations of data-driven conclusions.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, inspection, cleaning, and manipulation |
| NumPy | Numerical operations and statistical calculations |
| Matplotlib | Creating and customizing plots |
| Seaborn | Statistical visualizations and correlation heatmaps |
| Google Colab / Jupyter Notebook | Interactive development and execution |
| Git & GitHub | Version control and project hosting |

## 📂 Dataset Description

The project uses a **simulated educational dataset** designed to demonstrate data analysis techniques. It is not a real survey of students.

After cleaning, the dataset contains **100 records and 6 columns**.

| Column | Description |
|---|---|
| `Student_ID` | Identifier for each record |
| `Study_Hours` | Study duration recorded in hours |
| `Screen_Time_Hours` | Daily screen time in hours |
| `Sleep_Hours` | Sleep duration in hours |
| `Concentration_Score` | Numerical concentration score |
| `Physical_Activity_Minutes` | Physical activity duration in minutes |

### 🧹 Data Cleaning

The original dataset contained 101 rows, including one duplicate record. Some values were also missing.

The cleaning process involved:

1. Inspecting the dataset structure and data types.
2. Identifying missing values.
3. Removing the duplicate record.
4. Filling missing numerical values using the median of the corresponding column.
5. Preparing the cleaned data for statistical analysis and visualization.

The cleaned dataset contains 100 records.

## 📊 Key Results

The analysis of the simulated dataset produced the following approximate results:

| Metric | Result |
|---|---:|
| Average sleep duration | 6.75 hours |
| Average daily screen time | 4.79 hours |
| Screen time vs. sleep correlation | −0.52 |
| Sleep vs. concentration correlation | +0.59 |

### 🔍 What Do These Results Suggest?

- **Screen time and sleep:** The negative correlation suggests that higher screen time tends to be associated with less sleep in this dataset.
- **Sleep and concentration:** The positive correlation suggests that higher sleep duration tends to be associated with higher concentration scores in these records.
- **Data quality matters:** Removing duplicates and handling missing values helps prepare the dataset for more consistent analysis.

**Important:** These are patterns in simulated data. Correlation does not establish causation, and the findings should not be generalized to real students.

## 📈 Data Visualizations

The project generates five visualizations to help interpret the dataset.

### 1. 📱 Screen Time vs. Sleep Duration
A scatter plot used to explore the relationship between daily screen time and sleep duration.

### 2. 😴 Sleep Duration Distribution
A histogram showing how sleep-duration values are distributed across the dataset.

### 3. 📊 Average Activity Hours
A bar chart comparing the average values of the activities represented in the visualization.

### 4. 🧠 Sleep Duration vs. Concentration
A scatter plot used to examine the association between sleep duration and concentration scores.

### 5. 🔥 Correlation Heatmap
A heatmap displaying correlations between numerical variables, making positive and negative relationships easier to identify.

Run the notebook to generate and inspect the graphs and their outputs.

## 🚀 Getting Started

### Option 1: Run in Google Colab

1. Download or open `Sleep_ScreenTime_Analysis.ipynb`.
2. Upload the notebook to [Google Colab](https://colab.research.google.com/).
3. Upload `sleep_screen_time_data.csv` using the Colab Files panel or the notebook's CSV upload cell.
4. Run the code cells in order.
5. Review the cleaning results, statistical summaries, correlation values, and five visualizations.

Make sure the CSV is available before running any cell that reads the file.

### Option 2: Run Locally

**Step 1 — Clone the repository**

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your actual GitHub details.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

**Step 2 — Install the required libraries**

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

**Step 3 — Run the Python script**

```bash
python colab_code.py
```

Alternatively, launch Jupyter Notebook:

```bash
jupyter notebook
```

Then open `Sleep_ScreenTime_Analysis.ipynb` and execute the cells in order.

> The notebook, script, and CSV should remain in the appropriate project directory so the code can locate the dataset.

## 🗂️ Project Structure

```text
Sleep-ScreenTime-Analysis/
│
├── Sleep_ScreenTime_Analysis.ipynb
├── sleep_screen_time_data.csv
├── colab_code.py
├── README.md
└── .gitignore
```

## 💡 Findings & Observations

1. Data cleaning is an important first step because duplicate records and missing values can affect an analysis.
2. Correlation analysis helps identify patterns among numerical variables.
3. Visualizations make statistical results easier to interpret.
4. Screen time and sleep duration show a negative association in this simulated dataset.
5. Sleep duration and concentration scores show a positive association in this simulated dataset.
6. More data and real-world observations would be required to evaluate whether similar patterns occur among actual students.

## ⚠️ Limitations

- The dataset is simulated for educational purposes.
- The analysis contains only 100 cleaned records.
- Correlation does not prove cause and effect.
- The findings depend on the data values and preprocessing choices.
- The results are not medical advice and should not be used to make health-related conclusions.

## 🔮 Future Scope

Potential improvements include:

- Analyzing a larger, anonymized real-world dataset with appropriate permission.
- Comparing patterns across different days or groups, when suitable data is available.
- Adding more detailed statistical analysis.
- Developing an interactive dashboard with Streamlit or Plotly.
- Adding automated data-quality checks and exporting the generated plots.

## 🎓 Learning Outcomes

Through this project, we practised:

- Loading and exploring data with Pandas.
- Detecting and handling missing values and duplicates.
- Performing numerical and statistical analysis.
- Understanding correlation matrices.
- Creating and interpreting visualizations.
- Documenting a reproducible Python data-analysis workflow.

## 👥 Project Team

**Project Title:** Sleep Patterns & Screen Time Analysis Using Python

| Team Member | Roll Number |
|---|---:|
| Prathamesh Patil | 48 |
| Pranay Patil | 44 |

**Faculty Guide:** Prof. Kavyashree HN

**Department:** Computer Engineering  
**Institute:** Nutan Maharashtra Institute of Engineering & Technology, Pune

**Academic Year:** 2026–2027

## 📚 References

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Google Colab](https://colab.research.google.com/)

---

<p align="center">
  <strong>Built with Python. Driven by Data. Visualized with Purpose. 🌙📊</strong>
</p>

<p align="center">
  <sub>Educational mini project — Data Analysis & Visualization</sub>
</p>
