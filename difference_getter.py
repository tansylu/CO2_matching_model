import pandas as pd 

#Load the Excel files into pandas dataframes
model1 = pd.read_excel('result_modelPara.xlsx')
model2 = pd.read_excel('result_modelAll.xlsx')


merged = model1.merge(model2, indicator=True, how='outer')
differing_rows = merged[merged['_merge'] != 'both'].drop(columns=['_merge'])

# Save the differing rows to a new Excel file
differing_rows.to_excel('differences_new.xlsx', index=False) #Need to filter in alphabetical order to be able to see the 2 models' output together