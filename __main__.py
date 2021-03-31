import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import pandas as pd

file = r'.\data\sales_data.csv'
# sales = pd.read_csv(r'.\data\sales_data.csv', parse_dates=['Date'])

# print(sales.describe())
# sales['Customer_Age'].mean()
# df = pd.DataFrame(sales.describe())
# df.to_excel('test.xlsx')

# E: Create a numpy array with values ranging from 10 to 49

# my solution
# a = np.array([10])
# b = []
# for i in range(11, 50):
#     b.append(i)
# newArray = np.append(a, b)
# print(newArray)

# easier solution
# print(np.arange(10, 50))
