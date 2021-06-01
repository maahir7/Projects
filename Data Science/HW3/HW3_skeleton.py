# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#%% Q1 Matrix multiplication 
print("Question 1 **************************************")



#%% Q2
print("Question 2 **************************************")
#def zscore(arr):
 
# x=
# y=


#%% Q3
print("Question 3 **************************************")
# x=
# y=




#%% Q4
print("Question 4 **************************************")
# print("norm.cdf(0.5) ... ... \n")




#%% Q5
print("Question 5 **************************************")
# print("5a. X' ~ ... ...")



#%% Q6
print("Question 6 **************************************")
# print("P(A U B U C) = P(A) + ... + ...")





#%% Q7
print("Question 7 **************************************")




#%% Q8
print("Question 8 **************************************")






#%% Q9
print("Question 9 **************************************")



# close all existing floating figures
plt.close('all')

print("Question 10 **************************************")
#%% load data
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

# a. plot annual total measles cases in each year
plt.figure()
plt.title('a. NYC measles cases')

# 1. Your code is here


plt.show()

#%% b. bar plot average mumps cases for each month of the year
plt.figure()
plt.title('b. Average monthly mumps cases')

# 2. Your code is here

plt.show()


#%% c. scatter plot monthly mumps cases against measles cases
mumpsCases = mumps[:, 1:].reshape(41*12)
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('c. Monthly mumps vs measles cases')

# 3. Your code is here

plt.show()


#%% d. plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('d. Monthly mumps vs measles cases (log scale)')

# 4. Your code is here

plt.show()


#%% Answer to e

# 5. Your code is here
answer = ''

print('\n\nAnswer to e: ' + answer)
