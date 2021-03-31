import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import pandas as pd
import sys

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

# Create a numpy matrix of 2*2 integers, filled with ones
# print(np.ones([2,3], dtype=int))

# print(np.ones([3, 2], dtype=np.float16))
# print(np.zeros([3, 2], dtype=np.float16))

# Create a numpy matrix of 4*4 integers, filled with fives.
# print(
#
#     np.array([5]*16, dtype=int).reshape(4, 4)
# )

# a = np.array([10, 2, 100])
# print(np.ones_like(a) * 5)

# convert numpy array from the list
# copy array
# append to the array

# l = [1, 2, 3, 4]
#
# a = np.array(l)
# y = np.copy(a)
# y = np.append(y, [50])
#
# print(
#     a,
#     y
# )
# Comparing size of list

a = np.random.randint(0,8,9,)
l = [1,2,3,4,5,6,7,8]
print(
a,
sys.getsizeof(1),
sys.getsizeof(int),
np.dtype(int).itemsize
)