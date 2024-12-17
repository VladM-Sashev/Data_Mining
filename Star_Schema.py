import pandas as pd

#displaying options to ensure that all columns and rows are shown when printed
pd.set_option(‘display.max_columns’, None)
pd.set_option(‘display.max_rows’, None)

# Defining the path to the file
file_path = r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\Cleaned_Dataset.xlsx’

#Reading  the excel file
df = pd.read_excel(file_path)

# Printing  the DataFrame
print(df.head())
# Creating Dimension Tables
## Date Dimension
date_new = df[[‘Date’]].drop_duplicates().reset_index(drop=True)
date_new[‘date_id’] = date_new.index + 1

## Country Dimension
country_new = df[[‘Country(UK)’]].drop_duplicates().reset_index(drop=True)
country_new[‘country_id’] = country_new.index + 1

## Product Dimension
product_new = df[[‘Confectionary’]].drop_duplicates().reset_index(drop=True)
product_new[‘product_id’] = product_new.index + 1

# Creating Fact Table

## Getting IDs
df = df.merge(date_new, on=’Date’, how=’left’)
df = df.merge(country_new, on=’Country(UK)’, how=’left’)
df = df.merge(product_new, on=’Confectionary’, how=’left’)

## Selecting  and renaming the  columns for the fact table
fact_table = df[[‘date_id’, ‘country_id’, ‘product_id’, ‘Units Sold’, ‘Revenue(£)’, ‘Cost(£)’, ‘Profit(£)’]]
fact_table.rename(columns={‘Revenue(£)’: ‘revenue’, ‘Cost(£)’: ‘cost’, ‘Profit(£)’: ‘profit’}, inplace=True)

# Saving the Dimension Tables and Fact Table to new Excel files
date_new.to_excel(r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\date_dimension.xlsx’, index=False)
country_new.to_excel(r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\country_dimension.xlsx’, index=False)
product_new.to_excel(r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\product_dimension.xlsx’, index=False)
fact_table.to_excel(r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\fact_table.xlsx’, index=False)

print(“Star schema created and saved.”)
