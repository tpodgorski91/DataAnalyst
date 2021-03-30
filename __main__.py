import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import pandas as pd


sales = pd.read_csv(r'.\data\sales_data.csv', parse_dates=['Date'])
# sales = pd.read_csv(r'.\data\sales_data.csv')
# df = pd.DataFrame(sales)
print(sales.describe())
# sales['Customer_Age'].mean()
df = pd.DataFrame(sales.describe())
df.to_excel('test.xlsx')
