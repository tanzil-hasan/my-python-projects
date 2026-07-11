import pandas as pd

data = {
    "Employee_ID": [
        1001,1002,1003,1004,1005,
        1006,1007,1008,1009,1010,
        1011,1012,1013,1014,1015,
        1016,1017,1018,1019,1020
    ],

    "Name": [
        "Rahim","Karim","Sadia","Nabila","Hasan",
        "Mim","Rafi","Jannat","Sakib","Nusrat",
        "Tanvir","Sumaiya","Arif","Tania","Fahim",
        "Shanto","Rima","Rakib","Farzana","Imran"
    ],

    "Gender": [
        "Male","Male","Female","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Male","Female","Male","Female","Male"
    ],

    "Age": [
        22,25,21,23,24,
        22,26,20,23,21,
        29,27,30,26,28,
        24,25,27,22,31
    ],

    "Dept": [
        "Sales","EEE","HR","Finance","Marketing",
        "CSE","EEE","HR","Finance","Marketing",
        "CSE","Marketing","HR","Finance","IT",
        "Sales","Sales","IT","IT","Management"
    ],

    "Position": [
        "Junior Dev","Engineer","HR Officer","Accountant","Marketing Officer",
        "Data Analyst","Senior Engineer","HR Executive","Finance Officer","Sales Executive",
        "Software Engineer","Electrical Engineer","HR Manager","Senior Accountant","Marketing Manager",
        "Sales Officer","Sales Manager","System Admin","Network Engineer","General Manager"
    ],

    "Experience": [
        1,3,2,4,5,
        2,6,3,5,2,
        7,8,9,6,10,
        4,8,5,7,12
    ],

    "Salary": [
        35000,42000,35000,45000,50000,
        39000,65000,32000,47000,41000,
        70000,72000,80000,68000,85000,
        48000,76000,60000,62000,100000
    ],

    "Working_Hour": [
        8,9,6,8,9,
        8,10,7,8,8,
        9,9,6,7,10,
        8,7,8,9,10
    ],

    "Score": [
        85,78,74,91,88,
        90,95,72,84,80,
        96,89,93,87,98,
        82,94,88,91,99
    ],

    "City": [
        "Dhaka","Chattogram","Khulna","Dhaka","Rajshahi",
        "Dhaka","Sylhet","Khulna","Barishal","Dhaka",
        "Chattogram","Sylhet","Rajshahi","Dhaka","Khulna",
        "Cumilla","Dhaka","Sylhet","Rajshahi","Dhaka"
    ],

    "Status": [
        "Active","Active","Inactive","Active","Active",
        "Active","Inactive","Active","Active","Inactive",
        "Active","Active","Active","Inactive","Active",
        "Active","Active","Inactive","Active","Active"
    ]
}

df = pd.DataFrame(data)
df.set_index('Employee_ID' , inplace=True )
#print(df)

#=======================================================================================
#Find the top 5 employees based on Salary.

#salary_df = df.sort_values(by=['Salary' , 'Score'] , ascending=False)
#top_5_salary = salary_df.loc[salary_df.index[0:6] , : ]
#top_5_salary = salary_df.loc[(salary_df['Salary'] <= 100000 ) & (salary_df['Salary'] >= 72000) , : ]
#top_5_salary = salary_df.loc[salary_df['Salary'].between(72000,100000), : ]
#print(top_5_salary)
#=======================================================================================
#Display only the Name and Salary of employees whose Score is greater than 85.

# name_salary_df = df.loc[df["Score"] > 85 , ["Name" , "Salary"]]
# print(name_salary_df)

#======================================================================================
#Show all employees except those from the HR department.

# without_hr = df.loc[ ~(df['Dept'] == "HR") , : ]
# print(without_hr)

#=====================================================================================
#Display employees whose age is between 21 and 24

# specific_employee = df.loc[ df["Age"].between(21,24) , : ]
# print(specific_employee)

#====================================================================================
#Find employees who work exactly 8 hours.
#print(df.loc[ df['Working_Hour'].isin([8]) , : ])
#=====================================================================================

#Display the first three employees after sorting by Score in descending order and st four employees after sorting by Salary in ascending order..
#print(df.sort_values(by=["Score","Working_Hour"], ascending= False).head(3))
#print(df.sort_values(by=['Salary' , 'Score'] , ascending=True).tail(4))

#=====================================================================================
#Find all employees whose department is either CSE or IT.

# print(df.loc[ df['Dept'].isin(['CSE' , 'IT']) , : ])
# print(df.loc[ (df['Dept']=="CSE")|(df['Dept']=='IT') , : ])

#=====================================================================================
#Show only Name, Department and Score after sorting by Department.

#print(df.sort_values(by=['Dept' , 'Salary'] , ascending=[True,False]).loc[ : , ['Name' , 'Dept' , 'Score']])

#=====================================================================================
#Find employees whose Salary is greater than 55000 and Score is greater than 80.

#print(df.loc[ (df['Salary']>55000)  & (df['Score']>80), : ])

#=====================================================================================
#Display the row having the highest Score & the row having the lowest Salary.
# print(df.loc[df['Score'].isin([df['Score'].max()]), : ])
#print(df.sort_values(by=['Salary','Score']  , ascending=[True,False]).tail(1))

#==================================================================================

#sort the dataset by Age and then Salary.
#print( df.sort_values(  by='Age Salary'.split() , ascending=[True,True]  ) )

#==================================================================================
#Display only the first four columns of the DataFrame.
# print(df.columns[0:4]) #---> ['Name', 'Gender', 'Age', 'Dept']
# print(df.loc[: , df.columns[0:4]])

#======================================================================================

#Display only the last three columns.
# print(len(df.columns))
# print(  df.columns[ len(df.columns)-4 : len(df.columns)-1 ]  )

# print(df.loc[ : ,['Working_Hour', 'Score', 'City'] ])

# print(df.loc[ : , df.columns[ len(df.columns)-4 : len(df.columns)-1 ] ])

#=======================================================================================

#Find employees whose Salary is above the average Salary.
# print(df['Salary'].mean())
# print(df.loc[ df['Salary'] > df['Salary'].mean() , :])


#=======================================================================================
#Show employees whose Department is not CSE and whose Salary is above 35000.
#print(df.loc[ (df['Dept']=='CSE') & (df['Salary']>35000) , : ])

#================================================================================
#print(df.loc[df["Age"] % 2 == 0 , :])
# print(df[df["Age"] % 2 == 0 ] )

# even_age = [age for age in df['Age'] if age%2==0  ]
# print(even_age)
# print(df[df['Age'].isin(even_age)])

#==========================================================================================

#Display employees whose Salary is divisible by 5000.
#a_salary = [ salary for salary in df['Salary'] if salary%5000==0 ]
# print(df[df['Salary'].isin(a_salary)])
# print(df.loc[ df["Salary"].isin(a_salary) , : ])
# print(df.loc[ df["Salary"] % 5000 == 0 , : ])

#===========================================================================================

#Sort by Department, then Salary (descending), then Age (ascending).
#print(df.sort_values(by='dept salary age'.title().split() , ascending=[True , False , True]))

#===========================================================================================
#Display only Name, Salary and Score of the top five highest paid employees.
newdf = df.sort_values(by=["Salary","Score"] , ascending=[False , False])
#print(newdf.loc[ newdf['Salary'].isin([]) , ['Name' , 'Salary' , 'Score']])










