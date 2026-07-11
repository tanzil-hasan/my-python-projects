import pandas as pd
import openpyxl as xl
#things that i have  used ---->  head(), tail(), set_index(),  rename() ,  rename_axis(),  duplicated() , drop_duplicates(), isna() ,dropona() , shape , info() ,loc[] , describe() , dtypes .



#pd.set_option('display.max_columns' , None)
#pd.set_option('display.max_rows' , None)

df = pd.read_csv(r"C:\Users\User\Downloads\heart_attack_dataset (1).csv")
df.set_index('patient_id',inplace=True)
#print(df.head(5))
#df.drop(columns=['']) 
print(df[df['age'].notna()])

newdf = df.loc[: ,  'age':'cholesterol']
newdf = newdf.rename_axis('ID')

newdf.rename(columns={'chest_pain_type':'pain_type' , 'resting_bp':'bp'},inplace=True)
#print(newdf.shape)
###################################
#print(newdf[newdf.duplicated()],'\n')

newdf.drop_duplicates(inplace= True)
#print('\n',newdf.shape)
#print(newdf.info())


#print(newdf.isna().sum())
#print ( newdf[newdf.isna().any(axis=1)] )
newdf.dropna(inplace=True)
#print(newdf['age bp cholesterol'.split()].max())

high_bp = newdf[(newdf['bp']>80) & (newdf['bp']<250) ]
#print(high_bp.info())
#print(high_bp.describe())
#print(high_bp)

#print(newdf.describe())


#print(newdf.dtypes)



#newdf.to_excel(r'C:\Users\User\Downloads\heart_attack_summary.xlsx' , sheet_name = 'patients' , index = False)
