import pandas as pd 

#Load the Excel files into pandas dataframes
model1 = pd.read_excel('result_modelPara.xlsx')
model2 = pd.read_excel('result_modelAll.xlsx')


# Compare the dataframes and identify the rows that do not match
differences = model1.compare(model2)

# Filter out the rows that match and keep only the differing rows
#differing_rows = differences[differences['self'].notna()] this gives error, need to check

# Save the differing rows to a new Excel file
differences.to_excel('differences.xlsx', index=True)