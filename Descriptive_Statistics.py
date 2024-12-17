import pandas as pd

# Loading  the fact table
def load_fact_table(filepath):
    return pd.read_excel(filepath)

# Performing descriptive statistics
def descriptive_statistics(df):
    print("Descriptive Statistics Summary:\n")
    # Showing the numerical summary
    print(df.describe())
    # Extra statistics
    print("\nAdditional Statistics:")
    print("Variance:\n", df.var())
    print("Skewness:\n", df.skew())
    print("Kurtosis:\n", df.kurt())
    print("Range:\n", df.max() - df.min())
    # Correlation matrix
    print("Correlation Matrix:\n", df.corr())

# Primary method for running the analysis
def main():
    # Path to the fact table
    fact_table_path = r'C:\Users\Vladimir Merdzhanov\Desktop\Data_Mining\fact_table.xlsx'

    # Opening fact table
    fact_table = load_fact_table(fact_table_path)

    # Conducting  descriptive statistics
    descriptive_statistics(fact_table)

if __name__ == "__main__":
    main()
