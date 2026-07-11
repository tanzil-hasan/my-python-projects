import pandas as pd 
import numpy as np

employees = {
    "id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        116, 117, 118, 119, 120
    ],

    "name": [
        "Alice", "Bob", "Charlie", "David", np.nan,
        "Frank", "Grace", "Henry", "Isabella", "Jack",
        "Kevin", "Lily", "Mason", "Nora", "Oliver",
        "Charlie", "Peter", np.nan , "Ryan", "Sophia"
    ],

    "sex": [
        "F", "M", "M", "M", "F",
        np.nan, "F", "M", "F", "M",
        "M", "F", "M", "F", "M",
        "M", "M", "F", np.nan, "F"
    ],

    "age": [
        25, 30, 27, np.nan, 35,
        40, 29, 31, 26, 28,
        np.nan, 24, 38, 33, 36,
        27, 41, 30, np.nan, 29
    ],

    "dept": [
        "HR", "IT", "Finance", "Sales", "HR",
        "IT", np.nan, "Finance", "Marketing", "IT",
        "Sales", "HR", "Management", np.nan , "IT",
        np.nan , "Sales", "Marketing", "HR", np.nan
    ],

    "salary": [
        45000, 55000, 60000, np.nan, 70000, np.nan , 
        49000, 62000, 51000, np.nan,
        68000, 47000, 85000, 61000, np.nan ,
        60000, np.nan, 53000, np.nan , 65000
    ],

    "join_date": [
        "2020-01-15",
        "2019-06-10",
        "2021-03-22",
        "2018-11-05",
        np.nan,
        "2020-07-18",
        "2022-01-11",
        "2019-09-30",
        "2023-02-01",
        "2021-12-12",
        "2018-05-19",
        np.nan,
        "2017-10-25",
        "2020-08-14",
        "2019-04-09",
        "2021-03-22",
        "2022-06-15",
        "2023-01-20",
        "2021-11-11",
        np.nan
    ]
}

df = pd.DataFrame(employees)
#print(df)

#====================সব IT department-এর employee বের করো।===========================================

#print(df['dept'].value_counts())
it_employee = df[df['dept'].isin(['IT'])] # isin() takes list [...]
#print(it_employee)

#========================যাদের salary NaN, শুধু তাদের দেখাও=============================================

nan_salary = df[df['salary'].isna()]
#print(nan_salary.value_counts())

#==============================যাদের age NaN, তাদের count বের করো।====================================

nan_age = df[df['age'].isna()]
#print('AGE THAT WEREN NOT GIVEN ENTRY : ', len(nan_age['age']) )

#=========================================Duplicate name remove করো।==================================

#print(df[df['name'].duplicated(keep='first')])
#print(df[df['name'].isna()])

remove_duplicate_name = df.drop_duplicates(subset='name', keep='first')
#print(remove_duplicate_name,'\n\n',df)

#=========================প্রতিটি department-এর average salary বের করো।=================================

# print(df['dept'].describe())
# print('\n', df['dept'].unique())

dept_avg_salary = df.groupby('dept').agg({
   'salary' : ['mean'],
   'age' : ['median']     })

# print(dept_avg_salary,'\n\n')

# print(df[df['dept'].isin('HR'.split())])

#=====কোন department-এ সবচেয়ে বেশি employee আছে? =======================================================

dept_employee = df['dept'].value_counts()
#print(dept_employee)
new_df = df[df['dept'].isin(['HR','IT'])]
#print(new_df)

max_employee = dept_employee['hr it'.upper().split()]
#print("most employee : \n ", max_employee)

#========================Highest salary কার And  , Lowest salary কার? (done)==============================
 
range_salary = df[df['salary'].isin([df['salary'].max() , df['salary'].min()])]
#print(range_salary)

#===============================Salary-এর mean, median, max, min বের করো।=================================

operation_salary = df['salary'].agg('mean max min median'.split())
#print(operation_salary)

#===============================Join date NaN যাদের, তাদের আলাদা DataFrame বানাও।===========================

null_joindate = df[df['join_date'].isna()]
#print(null_joindate)

#===============================Salary NaN হলে mean salary দিয়ে fill করো===================================

mean = df['salary'].mean()
df['salary'] = df['salary'].fillna(mean)
#print(df['name age dept salary'.split()])

#=================================Department NaN হলে "Unknown" দিয়ে fill করো।==============================
# print("Puro column-e total missing:", df['dept'].isna().sum())
# print(df[df['dept'].isna()])
# print("Total rows in DataFrame:", len(df))

#df['dept'] = df['dept'].replace({np.nan : 'unknown'}) ----> alternative ..
#df['dept'] = df['dept'].fillna('unknown')
#print(df)

#============================HR department-এর average age বের করো।=========================================

hr_dept = df[df['dept'].isin(['HR'])]
#print(hr_dept)
avg_age = hr_dept['age'].mean()
hr_dept['age'] = hr_dept['age'].fillna(avg_age)
#print(hr_dept)

#=======================প্রতিটি department-এর employee count বের করো।========================================
employee = df['dept'].value_counts()
#print(employee)

#=========================Age 30-এর বেশি এবং salary 60000-এর বেশি—এমন employee বের করো।===================

special_employee = df[(df['age'].between(30,df['age'].max()))  &  (df['salary'].between(60000,df['salary'].max()))]
#print(special_employee)

#==========================সব NaN থাকা row delete করো।======================================================

""" 
Duto column-ke tader nijossho mean value diye fill korar niyom:
df['age salary'.split()] = df['age salary'.split()].fillna({
    'age': df['age'].mean(),
    'salary': df['salary'].mean()
},inplace = True)

print(df)
"""

only_nan = df[df[df.columns].isna().any(axis=1)]
#print(only_nan,'\n')

fresh = df.dropna(how='any')
#print(fresh)

#============================id-কে index বানিয়ে আবার reset_index() করো।==========================================
#print(df.set_index('id'))
df.set_index('id' , inplace=True) #permanently seted
#print(df.reset_index())

#===========================Salary অনুযায়ী descending order-এ sort করো।===========================================
#print(df.sort_values(by=['salary'] , ascending=False).reset_index())
