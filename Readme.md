# 🚢 Titanic Survival Analysis

A beginner data science project that analyzes survival patterns of Titanic passengers to identify key factors that influenced survival — such as **gender**, **passenger class**, and **age**.

---

## 📁 Project Structure

```
TITANIC-SURVIVAL-ANALYSIS/
│
├── Data/
│   ├── Images/
│   │   ├── survival.png
│   │   ├── gender_survival.png
│   │   ├── survival_by_class.png
│   │   ├── survival_by_age_group.png
│   │   └── pclass_and_gender_survival.png
│   │
│   └── Notebook/
│       └── Titanic_Survival_Analysis.ipynb
│
├── README.md
└── requirement.txt
```

---

## 🎯 Problem Statement

Organizations and researchers often collect historical data but lack a clear understanding of the patterns within it. This project focuses on the Titanic dataset to answer:

> **Who was more likely to survive the Titanic — and why?**

---

## 📊 Dataset

- **Source** — [Titanic Dataset on GitHub](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
- **Total Rows** — 891 passengers
- **Total Columns** — 12 features

| Column | Description |
|---|---|
| `Survived` | Target variable — 0 = Died, 1 = Survived |
| `Pclass` | Passenger class — 1st, 2nd, 3rd |
| `Sex` | Gender of passenger |
| `Age` | Age of passenger |
| `Fare` | Ticket fare paid |
| `Embarked` | Port of boarding |

---

## 🛠️ Libraries Used

```python
pandas       # Data loading, cleaning, analysis
matplotlib   # Data visualization
```

Install all dependencies:

```bash
pip install -r requirement.txt
```

---

## 🔄 Project Workflow

```
1. Load Data  →  2. Understand Data  →  3. Clean Data  →  4. Analyse  →  5. Visualize  →  6. Insights
```

---

## 🧹 Data Cleaning

| Issue | Fix Applied |
|---|---|
| Age — 177 missing values | Filled with **median** age |
| Cabin — 687 missing values | **Dropped** the column |
| Embarked — 2 missing values | Filled with **mode** |
| Name, Ticket columns | **Dropped** — not useful for analysis |

---

## 🔍 Analysis & Key Findings

### Q1 — What is the overall survival rate?

- **61.62%** of passengers died
- **38.38%** of passengers survived

> Survival was not random — it was strongly influenced by social factors.

---

### Q2 — Does Gender affect survival?

| Gender | Survival Rate |
|---|---|
| Female | **74.20%** |
| Male | **18.89%** |

> Females had a much higher survival rate due to the **"women and children first"** evacuation policy.

![Gender vs Survival](./Data/Images/gender_survival.png)

---

### Q3 — Does Passenger Class affect survival?

| Class | Survival Rate |
|---|---|
| 1st Class | **62.96%** |
| 2nd Class | **47.28%** |
| 3rd Class | **24.24%** |

> Higher-class passengers had better access to lifeboats and upper decks.

![Survival by Class](Data/Images/survival_by_class.png)

---

### Q4 — Gender combined with Class?

| Class + Gender | Survival Rate |
|---|---|
| 1st Class Female | **~96.8%** (Highest) |
| 3rd Class Male | **~13.5%** (Lowest) |

> The combination of being female AND in 1st class gave the highest chance of survival.

![Class and Gender Survival](Data/Images/pclass_and_gender_survival.png)

---

### Q5 — Does Age affect survival?

| Age Group | Survival Rate |
|---|---|
| Child (0–12) | **~58%** |
| Teen (12–20) | **~38%** |
| Adult (20–40) | **~37%** |
| Middle Age (40–60) | **~39%** |
| Senior (60–100) | **~23%** |

> Children had the highest survival rate. Age had a secondary effect compared to gender and class.

![Survival by Age Group](Data/Images/survival_by_age_group.png)

---

## 📈 Visualizations

| Chart | What it shows |
|---|---|
| `survival.png` | Overall count of died vs survived |
| `gender_survival.png` | Survival rate by gender |
| `survival_by_class.png` | Survival rate by passenger class |
| `survival_by_age_group.png` | Survival rate by age group |
| `pclass_and_gender_survival.png` | Combined gender and class survival |

![Survival Count](Data/Images/survival.png)

---

## 💡 Final Conclusion

Survival on the Titanic was **heavily influenced by social factors** — not random chance.

The priority order during evacuation was clear:

```
Females  >  Males
1st Class  >  2nd Class  >  3rd Class
Children  >  Adults  >  Seniors
```

The **strongest factors** were **gender** and **passenger class**.  
**Age** had a smaller but noticeable effect.

---

## 🚀 How to Run

1. Clone or download this project
2. Install dependencies
   ```bash
   pip install -r requirement.txt
   ```
3. Open the notebook
   ```bash
   jupyter notebook Data/Notebook/Titanic_Survival_Analysis.ipynb
   ```
4. Run all cells from top to bottom

---

## 👨‍💻 Author

**Learning Data Science** — This is a beginner project built while learning data analysis with Python, pandas, and matplotlib.

---

## 📌 Skills Demonstrated

- ✅ Data Loading with `pandas`
- ✅ Data Understanding — `shape`, `info`, `describe`, `dtypes`
- ✅ Missing Value Analysis and Handling
- ✅ Feature Engineering — `Age_Group` using `pd.cut()`
- ✅ Group-wise Analysis using `groupby()`
- ✅ Data Visualization using `matplotlib`
- ✅ Drawing insights from data
