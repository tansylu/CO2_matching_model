from model_class import string_embedder
import pandas as pd
from pickle_processor import init_processing

##run this once to obtain the pickle-excel convesion, otherwise skip
##init_processing()

# Read the codex Excel file
df1 = pd.read_excel('codex.xlsx')

# Access the columns in the first dataframe
code_column = df1['Code']
indented_tree_column = df1['Product'].str.strip()

# Read the second Excel file
df2 = pd.read_excel('output_ex_to_ei.xlsx')

# Access the columns in the second dataframe
subcategory_column = df2['Subcategory']
parent_category_column = df2['Parent Category']

# Initialize the string_embedder model
model = string_embedder('paraphrase-MiniLM-L6-v2')
# Embed the product string and get the closest match
model.embed_list_of_strings(subcategory_column.tolist())
#!!do this once here instead of repeating th eprocess every time in the loop

# Create a new dataframe to store the results
result_df = pd.DataFrame(columns=['Code', 'Product', 'Matched Subcategory', 'Parent Category'])

print("Running main.py...")

count = 0
# Loop through each item in the "Product" column
for product in indented_tree_column:
    if count == 50:
        break
    else:
        count+=1
    print("Processing {}".format(product))
 
    match = model.get_closest_from_list_of_strings(product)
    
    # Find the index of the matched subcategory
    match_index = subcategory_column[subcategory_column == match].index[0]
    
    # Get the parent category based on the match index
    parent_category = parent_category_column[match_index]
    
    # Append the result to the result dataframe
    result_df = pd.concat([result_df, pd.DataFrame({
        'Code': [code_column[match_index]],
        'Product': [product],
        'Matched Subcategory': [match],
        'Parent Category': [parent_category]
    })], ignore_index=True)

print("Prediction complete.")
print(result_df)

# Save the result dataframe to an Excel file
result_df.to_excel('result.xlsx', index=False)