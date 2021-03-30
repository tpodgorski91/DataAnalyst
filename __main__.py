import pandas as pd

sales = pd.read_csv(r'.\data\sales_data.csv')['Customer_Age'].mean()
print(sales)