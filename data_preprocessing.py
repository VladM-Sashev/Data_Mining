import pandas as pd

#displaying options to ensure that all columns and rows are shown when printed
pd.set_option(‘display.max_columns’, None)
pd.set_option(‘display.max_rows’, None)

# Defining the path to the file
file_path = r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\Correct_Assignment_data_set_Feb_24_SCC.xlsx’

#Using pandas to read the excel file
df = pd.read_excel(file_path)

# Print the DataFrame
print(df.head())

# Checking  for missing values in the DataFrame
missing_values_count = df.isnull().sum()
print(“\nInitial missing values count for each column:”)
print(missing_values_count)

# ‘Units Sold’ with  median
units_sold_median = df[‘Units Sold’].median()
df[‘Units Sold’] = df[‘Units Sold’].fillna(units_sold_median)

# ‘Revenue’ and ‘Cost’ with their medians
if ‘Revenue(£)’ in df.columns and ‘Cost(£)’ in df.columns:
    revenue_median = df[‘Revenue(£)’].median()
    cost_median = df[‘Cost(£)’].median()
    df[‘Revenue(£)’] = df[‘Revenue(£)’].fillna(revenue_median)
    df[‘Cost(£)’] = df[‘Cost(£)’].fillna(cost_median)

    # Calculating missing ‘Profit’ values if both ‘Revenue’ and ‘Cost’ are available
    df.loc[df[‘Profit(£)’].isnull() & df[‘Revenue(£)’].notnull() & df[‘Cost(£)’].notnull(), ‘Profit(£)’] = df[‘Revenue(£)’] – df[‘Cost(£)’]

# Imputing remaining missing ‘Profit’ values with its median
profit_median = df[‘Profit(£)’].median()
df[‘Profit(£)’] = df[‘Profit(£)’].fillna(profit_median)

#checking for any remaining missing values
final_missing_values_count = df.isnull().sum()
print(“\nMissing values count after treatment for each column:”)
print(final_missing_values_count)

# Checking for exact duplicates
duplicates = df.duplicated(subset=[‘Date’, ‘Country(UK)’, ‘Confectionary’, ‘Units Sold’, ‘Revenue(£)’, ‘Cost(£)’, ‘Profit(£)’], keep=False)
duplicate_df = df[duplicates]

# Displaying  the duplicate rows if there are any
if not duplicate_df.empty:
    print(“Duplicate records in the dataset:”)
    print(duplicate_df)
else:
    print(“No duplicate records found.”)

# Function to identify the  outliers and calculating the IQR
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 – Q1
    lower_bound = Q1 – 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (df[column] < lower_bound) | (df[column] > upper_bound)

# Applying the function to each column and check for outliers
numeric_columns = [‘Units Sold’, ‘Revenue(£)’, ‘Cost(£)’, ‘Profit(£)’]
for column in numeric_columns:
    if column in df.columns:
        outliers = detect_outliers(df, column)
        if not outliers.any():
            print(f”No outliers found in {column}.”)
        else:
            print(f”Outliers in {column}:”)
            print(df[outliers])

# Function to calculate IQR and cap outliers
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 – Q1
    lower_bound = Q1 – 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)

# Applying the capping function to each numeric column
numeric_columns = df.select_dtypes(include=[‘number’]).columns
for column in numeric_columns:
    cap_outliers(df, column)
    print(f”Outliers in {column} have been capped.”)

# Specifying  the file path where I  want to save the cleaned data
output_file_path = r’C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\Cleaned_Dataset.xlsx’

# Saving the DataFrame to an Excel file
df.to_excel(output_file_path, index=False)

print(“The cleaned dataset has been saved to:”, output_file_path)
