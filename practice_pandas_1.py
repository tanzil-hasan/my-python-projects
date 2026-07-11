import pandas as pd

data = {
    "Name": [
        "Rahim", "Karim", "Nabila", "Sadia",
        "Hasan", "Mim", "Rafi", "Jannat"
    ],
    "Age": [22, 25, 21, 23, 24, 22, 26, 20],
    "Dept": [
        "CSE", "EEE", "CSE", "BBA",
        "EEE", "CSE", "BBA", "CSE"
    ],
    "Math": [88, 75, 95, 81, 81, 90, 73, 85],
    "English": [79, 85, 91, 70, 76, 88, 80, 92],
    "CGPA": [3.75, 2.45, 3.95, 3.45, 2.60, 3.88, 2.30, 3.82]
}

df = pd.DataFrame(data)
#print(df)




#print(df.head(5), "\n ",  df.tail(3))
#df.set_index('CGPA', inplace= True)
#print(df.columns ,  '\n'  ,  df.index )
#print(df.shape ,  '\n' ,   df.info())

#print(df.describe(include= 'all'))
#print('\n' , df.transpose().head(4))



# print(df.sort_values(by=['Age']  , ascending=True) )
# print(df.sort_values(by='Age CGPA'.split() , ascending=False)) 


# print(df.sort_values(by=['Math'] , ascending=False))
# print(df.sort_values(by=['Math','CGPA'] , ascending=False ))


# sdf = pd.Series(data)
# print(sdf['Name'])



# df.index = '4 6 9 2 1 5 3 0'.split()
# df.sort_index(axis=0 , ascending=False,inplace=True)
# print(df.sort_values(by=['Dept' , 'CGPA'], ascending=False))

#print(df.loc[ [1,4,5,6,7] , ['Name' , 'Age'] ])

#print((df.sort_values(by=["Math" , "CGPA"] , ascending=False)).loc[ [2,5,0], :])

#print((df.sort_values(by=["Math" , "CGPA"] , ascending=False)))
#print((df.sort_values(by=["Math" , "CGPA"] , ascending=False))[0:3])

# ndf=df.sort_values(by=["CGPA"])
# print(ndf)
# print(ndf[len(ndf)-2 : ])

# print((df.T).index)
# print((df.T).columns)

#print(((df['Name Age Dept CGPA'.split()]).sort_values(by=['CGPA'] , ascending=False ))[:5])
#print(df[['Name','Age','Dept','CGPA']].sort_values(by='CGPA', ascending=False).head(5))

# the functions I learned proprtly : head() , tail() , transpose() , index , columns , shape , info() , describe() , sort_index() , sort_values()


















