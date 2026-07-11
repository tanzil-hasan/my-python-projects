import pandas as pd 
import numpy as np
import openpyxl as xl



import numpy as np

employees = {
    "Id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        116, 117, 118, 119, 120,
        121, 122, 123, 124, 125,
        126, 127, 128, 129, 130
    ],

    "name": [
        "Alice", "Bob", "Charlie", np.nan, "Eva",
        "Frank", "Grace", "Henry", "Isabella", "Jack",
        "Kevin", "Lily", "Mason", "Nora", np.nan,
        "Oliver", "Peter", "Queen", "Ryan", "Sophia",
        "Thomas", "Uma", "Victor", "William", "Xavier",
        "Yasmin", "Zara", "David", "Emma", "Chris"
    ],

    "age": [
        25, 30, np.nan, 28, 35,
        42, 29, 33, 26, np.nan,
        38, 27, 45, 31, 36,
        24, np.nan, 41, 39, 32,
        30, 28, 37, np.nan, 30,
        29, 42, 26, 33, 25
    ],

    "salary": [
        45000, 52000, 61000, np.nan, 70000,
        55000, 48000, 62000, np.nan , 51000,
        np.nan, 47000, 80000, 54000, 66000,
        45000, 59000, np.nan, 75000, 58000,
        np.nan, 49000, 72000, 56000, np.nan,
        61000, 82000, 50000, 69000, 45000
    ],

    "department": [
        "HR", "IT", "Finance", "Sales", np.nan,
        "IT", "Marketing", "Finance", "HR", "Sales",
        "IT", "Marketing", "Management", "Finance", "HR",
        "Sales", np.nan, "Management", "IT", "Finance",
        "Marketing", "HR", "Management", "Sales", "IT",
        "Finance", np.nan, "Marketing", "IT", "HR"
    ],

    "gender": [
        "Female", "Male", "Male", "Female", "Female",
        np.nan, "Female", "Male", "Female", "Male",
        "Male", "Female", "Male", np.nan, "Female",
        "Male", "Male", "Female", "Male", "Female",
        "Male", "Female", np.nan, "Male", "Male",
        "Female", "Female", "Male", "Female", "Male"
    ],

    "working_hour": [
        6, 9, 8, 7, np.nan,
        8, 9, 8, 8, 7,
        9, np.nan, 8, 8, 9,
        7, 8, 7, np.nan, 8,
        7, 8, 9, 8, 7,
        12 , np.nan , 9, 8, 7
    ],

    "score": [
        88, 75, np.nan, 92, 81,
        69, 95, 78, 84, 73,
        90, np.nan, 98, 85, 80,
        76, 91, 87, np.nan, 83,
        78, 94, 89, 72, 86,
        79, 97, 88 , 82, 90
    ]
}


"""
df = df.info()
print(df.describe())
df = df.set_index('Id')
df = df.rename_axis('ID NO.')
unipue = df['age'].notna()
df = df.iloc[:20 , :4]
df = df.iloc[2:7]
df = df.iloc[ : , 2:7]
df = df.loc[ : ,'salary' : 'score']
df = df.loc[ '101':'110' ,'salary' : 'score']
df = df.loc[ df.index[2:9] ,'salary' : 'score']
df = df.loc[ '101' : '125' ,'salary working_hour score'.split()]
df = df.loc[ '101' : '125' , ['age', 'score' , 'salary']]
df = df[df.duplicated()]
ddf= df['Age'].drop_duplicates()
df = df[df.duplicated('score' , keep='first')]
df = df[df.duplicated('score' , keep='last')]
df.drop_duplicates(subset='salary' , keep = 'last' , inplace = True)
df.drop_duplicates(inplace=True)
df = df[df['salary'].notna()]
df = df.rename(columns={'age' : 'Age' , 'salary' : 'Salary' , 'score' : 'Score' , 'department':'Dept' , 'name' : 'Name' , 'gender':'Sex'})
df = df[df.isna().any(axis=1)]
df = df[df.notna().all(axis=1)] 

105 and 106 ei 2 liner theke aro besi read-able =>  df = df.loc[df.notna().all(axis=1) , : ]

df = df[

    (df['Age'].between(30,df['Age'].max())) &

    (df['working_hour'].between(8,df['working_hour'].max())) &

    (df['Score'].between(85,df['Score'].max()))
]

df = df.loc[df['Salary'].between(50000,100000), 'NAME AGE SALARY DEPT SEX SCORE PROMOTED_SALARY'.title().split()] 
df =df.nunique()
df =df['Age Salary Score'.split()].nunique()
df['Promoted_Salary'] = df['Salary']
df.loc[df['Score'].between(80, 98), 'Promoted_Salary'] = df['Salary'] + 10000

value = df['Dept'].value_counts()

value = df['Dept Sex'.split()].value_counts() -----> output :        Dept        Sex   
                                                                    Finance     Female    2
                                                                    IT          Male      1
                                                                    Finance     Male      1
                                                                    Management  Male      1
                                                                    Marketing   Male      1
                                                                    HR          Female    1
                                                                    Name: count, dtype: int64

value = df.describe()
value = df['Age'].describe()
value = df.value_counts()

"""



df = pd.DataFrame(employees)

df = df.set_index('Id')
df = df.rename_axis('ID NO')
df = df.rename(columns={'age' : 'Age' , 'salary' : 'Salary' , 'score' : 'Score' , 'department':'Dept' , 'name' : 'Name' , 'gender':'Sex', 'working_hour': 'Work Time'})
 #starts from here ... 

# ndf =df[df['Age Dept'.split()].duplicated(keep = 'first')]
# print(ndf)
# print('\n\n')
# df =df[df['Age Dept'.split()].duplicated(keep = 'last')]


ddf= df.drop_duplicates(subset='Age Salary Dept'.split() , keep='last')
ndf = df['Age Salary Dept'.split()].nunique(dropna = False)
print(ndf ,'\n\n', ddf)


#value = df['Dept Sex'.split()].value_counts()
#value = df.value_counts()
#print(value)


#df.to_excel(r'C:\Users\User\Downloads\employees.xlsx' , sheet_name = 'employees' , index = False)
print('saved successfully')
