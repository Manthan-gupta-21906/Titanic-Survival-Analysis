# Generated from: Titanic_Survival_Analysis.ipynb
# Converted at: 2026-04-21T16:17:50.675Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Titanic Survival Analysis


# ## 1. Problem Statement
# 
# 
# This project analyzes survival patterns of Titanic passengers using data analysis techniques. The goal is to identify key factors influencing survival such as gender, class, and age.


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# ## 2. Data Understanding


print("DATASET OVERVIEW")
print(f"Dataset Shape: {df.shape}")
print(f"Total Rows: {df.shape[0]}") #0 means row
print(f"Total Columns: {df.shape[1]}") #1 means column

print("FIRST 5 ROWS OF DATA")
df.head()

print("DATA TYPES")
print(df.dtypes)

print("BASIC INFO OF DATASET")
df.info()

print("MISSING VALUES ANALYSIS")

missing_count = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': missing_count.values,
    'Missing_Percentage': missing_percent.values
})
print(missing_df)

print("COLUMN NAMES")
for i,col in enumerate (df.columns):
    print(f"{i+1}. {col}")

print("STATISTICAL SUMMARY (NUMERICAL COLUMNS)")
print(df.describe())

# * Missing columns: Age(177), Cabin(687), Embarked(2)
# * Important Columns:
#                   Sex (VERY important)
# 
#                   Pclass (rich vs poor)
# 
#                   Age (young vs old)
# 
#                   Fare (wealth indicator)
# 
#                   Embarked (boarding location)
# 
# * Observations :
#          Dataset has mix of categorical and numerical features
# 
#          Survived is target variable (0 = died, 1 = survived)
# 
#          Cabin has too many missing values
# 
#          Age has moderate missing - needs fixing
#          


# ## 3. Data Preprocessing and Cleaning


# to check weather it is useful or null 
#how it can help me 
print("DATA PREPROCESSING & CLEANING")
print("\nHandling Missing Values...")

#fill age with median 
df['Age']=df['Age'].fillna(df['Age'].median())
print("Filled missing age with median")

#drop cabin 
df=df.drop('Cabin',axis=1) #axis = 1 means column not row 
print("Cabin column is dropped")

#fill embarked with mode 
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0]) #0 means pick first value 
print("Filled missing embarked with mode")

#drop unnecessary columns 
df=df.drop(['Name','Ticket'],axis=1)
print("Unnecessary columns dropped")

print("Again checking for null values")
df.isnull().sum()

print("DATA PREPROCESSING & CLEANING DONE")

# ## 4. Analysis


# ### Q1: What is survival rate?


print("ANALYSING SURVIVAL RATES.....")
df['Survived'].value_counts()  # 0 ---> dead & 1 ---> survived

died     = df[df['Survived'] == 0]
survived = df[df['Survived'] == 1]

print(f"Total Died     : {len(died)}")
print(f"Total Survived : {len(survived)}")

df['Survival_Status'] = df['Survived'].map({0: 'Died', 1: 'Survived'}) #add new column easy for visualization

print(df['Survival_Status'].value_counts())

x=df['Survived'].value_counts(normalize=True)*100
print("Require survival and death percentage will be : ")
print(x.round(2))

# Only 38.38% of passengers survived, while 61.62% did not survive, indicating that the majority of people on board the Titanic lost their lives.
# 
# This suggests survival was difficult and likely influenced by factors such as gender, class, and age rather than being random.


# ### Q2: Gender Vs Survival?


print("ANALYSING GENDER VS SURVIVAL.....")
y=df.groupby('Sex')['Survived'].mean()*100
print("Gender vs Survival analysis is as follows: ")
print(y.round(2))

# Females had a much higher survival rate (74.20%) compared to males (18.89%), showing a significant difference in survival outcomes based on gender.
# 
# This suggests that women were given priority during rescue operations, reflecting the “women and children first” policy followed during the Titanic evacuation.


# ### Q3: Class Vs Survival?


print("ANALYSING CLASS VS SURVIVAL.....")
z=df.groupby('Pclass')['Survived'].mean()*100
print("Pclass vs Survival analysis is as follows: ")
print(z.round(2))

# Passengers in 1st class had the highest survival rate, while those in 3rd class had the lowest survival rate
# 
# This likely occurred because higher-class passengers had better access to lifeboats, were closer to upper decks, and received priority during evacuation, whereas lower-class passengers faced more barriers and delays.


# ### Q4: Gender VS Class?


print("Gender and Class.....")
x1=df.groupby(['Pclass','Sex'])['Survived'].mean()*100
print("require analysis is ")
print(x1.round(2))

# 1st class females had the highest survival rate (~96.8%), while 3rd class males had the lowest (~13.5%), showing a huge survival gap based on both gender and class.
# 
# Survival was strongly influenced by both gender and class together. Women, especially in higher classes, were given the highest priority, while lower-class men were the least prioritized during evacuation.


# ### Q5: Age Impact?


print("ANALYSING AGE IMPACT.....")
df.groupby('Survived')['Age'].mean()

# The average age of survivors (~28 years) is slightly lower than those who did not survive (~30 years), indicating that younger passengers had a marginally higher chance of survival.
# 
# The small difference suggests that age alone was not a major factor in survival, and other variables like gender and class had a much stronger influence


df['Age_Group'] = pd.cut(
    df['Age'],
    bins   = [0, 12, 20, 40, 60, 100],
    labels = ['Child', 'Teen', 'Adult', 'Middle Age', 'Senior']
)

print(df.groupby('Age_Group')['Survived'].value_counts())

# #### Overall Insight
# 
# Survival was not random. It followed a clear priority pattern:
# - Females > Males
# - Higher class > Lower class
# - Children > Adults > Seniors
# 
# The strongest factors influencing survival were gender and class, while age had a secondary effect.


# ## 5. Visualization


print("SURVIVAL COUNT")
df['Survived'].value_counts().plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("0 -> DIED, 1-> Survived")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout() 
plt.savefig(r"C:\Users\hp\Desktop\Titanic-Survival-Analysis\Images\survival.png")
plt.show()

print("GENDER VS SURVIVAL")
df.groupby('Sex')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout() 
plt.savefig(r"C:\Users\hp\Desktop\Titanic-Survival-Analysis\Images\gender_survival.png")
plt.show()

# Female have significantly higher survival rate compared to males, supporting the "women first" evacuation method


print("CLASS VS SURVIVAL")
df.groupby('Pclass')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(r"C:\Users\hp\Desktop\Titanic-Survival-Analysis\Images\survival_by_class.png")
plt.show()

# First-class passengers had higher survival rates likely due to better access to lifeboats and proximity to upper decks during evacuation.


print("AGE GROUP")
df.groupby('Age_Group')['Survived'].mean().plot(kind='bar')
plt.title("Survival Rate by Age Group")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(r"C:\Users\hp\Desktop\Titanic-Survival-Analysis\Images\survival_by_age_group.png")
plt.show()

# child has more survival all becaus of child and women first policy


df.groupby(['Pclass','Sex'])['Survived'].mean().unstack().plot(kind='bar')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(r"C:\Users\hp\Desktop\Titanic-Survival-Analysis\Images\pclass_and_gender_survival.png")
plt.show()

# ## 6. Final Insights
# 
# 1. Only 38% passengers survived, indicating survival was difficult and not random.
# 
# 2. Females had a much higher survival rate (~74%) compared to males (~19%), showing strong gender-based priority.
# 
# 3. 1st class passengers had the highest survival rate, while 3rd class had the lowest, indicating class-based inequality in survival.
# 
# 4. Combining gender and class shows that 1st class females had the highest survival, while 3rd class males had the lowest.
# 
# 5. Children had a relatively higher survival rate compared to adults and seniors, but age was less influential than gender and class.
# 
# ### Conclusion
# 
# Survival on the Titanic was heavily influenced by social factors such as gender and class rather than being random. Women and higher-class passengers had significantly better chances of survival.


#