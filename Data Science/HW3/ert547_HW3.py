#Download the file ert547_hw3.py; Open the file in Spyder; Run the code by clicking the “Run” button

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

print("Done by: Maahir Kalban (ert547)\n")
#%% Q1 Matrix multiplication 
print("Question 1 **************************************\n")

arr = np.array([[14,  9, 12],        
                [14,  3, 10],
                [13, 13,  2],
                [17,  3, 17],
                [13, 18, 19],
                [ 0, 15, 10]])

print(arr[:4, :2])


A = np.array ([[2, 8, 4],
               [5, 4, 2]])

B = np.array ([[4, 1],
               [6, 4],
               [5, 3]])

C = np.array ([[4, 1, 2],
               [6, 4, 3],
               [5, 3, 4]])

D = np.array ([[4, 1, 2],
               [6, 4, 3]])

print("A dot B equals\n")
print (A.dot(B))

print("\nA dot C equals\n")
print (A.dot(C))

print("\nA dot D equals\n")
#print (A.dot(D))

print("Error: shapes (2,3) and (2,3) not aligned. The resulting matrix has to have the same number of rows in A and the same number of columns in D.\n")


#%% Q2
print("Question 2 **************************************\n")
#def zscore(arr):
 
# x=
# y=

x = np.array([50, 68, 74, 70, 65, 61, 63, 74, 62])
y = np.array([170, 193, 209, 185, 195, 188, 188, 202, 183]) 
plt.scatter(x, y) 
plt.show()

def zscore(numArray):
    return (numArray - np.mean(numArray))/np.std(numArray)

zx = zscore(x)
zy = zscore(y)
    
plt.scatter(zx, zy)
plt.show()

#zx.dot(zy) / len(x)
print("Pearson correlation coefficient using my own methods\n",zx.dot(zy) / len(x) )
print("Pearson correlation coefficient from the corrcoef function\n",np.corrcoef(x, y)[0,1])
print("Thus they are they the same\n")



#%% Q3
print("Question 3 **************************************\n")
# x=
# y=
x = np.array([50, 68, 74, 70, 65, 61, 63, 74, 62, 80])
y = np.array([170, 193, 209, 185, 195, 188, 188, 202, 183, 1000]) 
plt.scatter(x, y) 
plt.show()

print("Pearson correlation coefficient from the corrcoef function\n",np.corrcoef(x, y)[0,1])

x_rank = np.argsort(np.argsort(x))
y_rank = np.argsort(np.argsort(y))
print("Spearman correlation coefficient from the corrcoef function\n",np.corrcoef(x_rank, y_rank)[0,1])
print("Thus they are not the same.Spearman correlation coefficient is better\n")
print("The values (-1, 0, and 1) of the coefficient indicate correlation measures of the linear relationship\n")

#%% Q4
print("Question 4 **************************************\n")
# print("norm.cdf(0.5) ... ... \n")
from scipy.stats import norm
print("norm.cdf(0.5) = ",norm.cdf(0.5)-norm.cdf(-0.5))
print("2*(0.5-norm.cdf(-0.5)) = ",2*(0.5-norm.cdf(-0.5)))

#%% Q5
print("\nQuestion 5 **************************************\n")
# print("5a. X' ~ ... ...")
print("5a. X' ~ N(a\u03BC + b, a\u00b2\u03BC\u00B2)\n")
print("5b. Z = (X - \u03BC)/\u03C3 ~ N(0,1)\n")
print("5c.\n")
print ("Given P(2<= X <=7) where X ~ N(5,9)\n")
import math
print("Standard Deviation = sqrt(variance) =",math.sqrt(9),"\n")   
print("probability = norm.cdf(7,5,3.0)-norm.cdf(2, 5, 3.0) =",norm.cdf(7,5,3.0)-norm.cdf(2, 5, 3.0),"\n")
print("5d.\n")
print ("Given P(-1.5<= X <=1.5) where X ~ N(0,1)\n")
print("probability = norm.cdf(1.5) - norm.cdf(-1.5) =",norm.cdf(1.5) - norm.cdf(-1.5),"\n")
#%% Q6
print("Question 6 **************************************\n")
# print("P(A U B U C) = P(A) + ... + ...")
print("a.) P(A \u222A B) = P(A) + P(B) - P(AB)\n")
print("b.) P(A|B) = P(A \u2229 B)/P(B)\n")
print("c.) P(A \u2229 B) = P(B)*P(A|B)\n")
print("d.) If A and B are independent, P(A \u2229 B) = P(A)*P(B)\n")

#%% Q7
print("Question 7 **************************************\n")
print("Are P(d = even) and P(d < 5) independent?\n")
print("A, B are independent iff\n")
print("-> P(A ∩ B) = P(A) * P(B)\n")
print("P(d = even and d < 5) = 2/8 = 1/4\n")
print("P(d = even) * P(d < 5) = (4/8)*(4/8) = 1/8\n")
print("Therefore P(A ∩ B) \u2260 P(A) * P(B)\n")
print("Thus P(d = even) and P(d < 5) are not independent\n")
#%% Q8
print("Question 8 **************************************\n")
print("P( 6 | fair ) = 1/6\n")
print("P( 6 | loaded ) = 0.5\n")
print("P( fair ) = 0.95 and P( loaded ) = 0.05\n")
print("Therefore using law of total probability , we get here:\n")
print("P( 6666) = P(6666 | fair)P(fair) + P(6666 | loaded )P(loaded )\n")
print("P( 6666) = (1/6)\u2074*0.95 + 0.5\u2074*0.05 = 0.003858\n")
print("Using Bayes theorem, we get now:\n")
print("P( loaded | 6666 ) = P(6666 | loaded )P(loaded ) / P( 6666)\n")
print("P( loaded | 6666 ) = 0.5\u2074*0.05 / 0.003858\n")
print("P( loaded | 6666 ) = 0.81\n")
#%% Q9
print("Question 9 **************************************\n")

print("Let F represents the event 'Has a disease', E represents the event 'Tests positive', F' represents 'Doesn't have the disease', and E' represents 'Test negative.\n'The probability of people with the disease test positive is P( E | F) = 99.9% = 0.999\n")
print("The probability of people with the disease test negative is\n P( E' | F) = 1 - 0.999 = ",1 - 0.999,"\n")
print("The probability of people who do not have the disease test positive is:\n")
print("P( E | F' ) = 0.02% = 0.0002.\n")
print("The probability of people who do not have the disease test negative is:\n")
print("P( E' | F' ) = 1 - 0.0002 = ",1 - 0.0002,"\n")
print("The probability of people having rare genetic desease is:\n")
print("P(F) = 1/1000 = ",1/1000,"\n")
print("And the probability of people who do not have disease is P( F' ) = 1 - 0.0001 =",1 - 0.0001,"\n")
print("a.)\n")
print("Determine the probability that someone who tests positive has the disease.\n")
print("Use Bayes' theorem P( F | E) = P(E | F)P( F ) /(P ( E | F ) P( F ) + P ( E | F' ) P ( F' )).\n")
print("P( F |E ) = 0.999 x 0.0001/(0.999 X 0.0001 + 0.0002 X 0.9999) = ",(0.999 * 0.0001)/(0.999 * 0.0001 + 0.0002 * 0.9999),"\n")
print("Therefore, there is approximately 0.333 chance of having the disease even if tests positive, as the disease is so rare.\n")
print("b.)\n")
print("Determine the probability that someone who tests negative has the disease.\n")
print("Use Bayes' theorem P( F' | E') = P(E' | F')P( F' ) /(P ( E' | F'' ) P( F' ) + P ( E' | F ) P ( F ))\n")
print("P( F' | E') = 0.9998 * 0.9999 /(0.9998 * 0.9999 + 0.001 * 0.0001) = ",(0.9998 * 0.9999) /(0.9998 * 0.9999 + 0.001 * 0.0001),"\n")
print("Therefore, there is approximately 0.999 chance of not having the disease even if tests positive.\n")


# close all existing floating figures
plt.close('all')

print("Question 10 **************************************\n")
#%% load data
import pandas as pd 
import functools as ft
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

# a. plot annual total measles cases in each year
plt.figure()
plt.title('a. NYC measles cases')

# 1. Your code is here
#%%  Total number of measles cases in each year
measlesData = np.array(measles) # Convert to numpy array

# get years from measles data
years = measlesData[:,0] # All rows x 0th column
# create array for X-axis data
totalMeaslesCases = np.array(years[:]) 

# For each year add all columns from index 1 to 12; add Sum to a numpy array
for year in range(len(years)): 
    totalMeaslesCases[year] = ft.reduce(lambda x,y: x+y, measlesData[year, 1:12]) 

# Plot Measles data
#plt.figure()
#plt.title('a: NYC measles cases')
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.plot(years, totalMeaslesCases, 'b*-') 

plt.show()

#%% b. bar plot average mumps cases for each month of the year
plt.figure()
plt.title('b. Average monthly mumps cases')

# 2. Your code is here
mumpsData = np.array(mumps) # Convert to numpy array
#%% Average number of mumps cases for each month of the year
sums = np.sum(mumpsData[:, 1:] , axis=0) # sum each column (month) along 0th axis
sums = sums / 41 # calculate average of each month

#plt.figure()
#plt.title('b: Average monthly mumps cases')
plt.xlabel('Months')
plt.ylabel('Average number of cases')
plt.bar(range(1,13), sums)
plt.show()


#%% c. scatter plot monthly mumps cases against measles cases
mumpsCases = mumps[:, 1:].reshape(41*12)
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('c. Monthly mumps vs measles cases')

# 3. Your code is here
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measles cases')
plt.scatter(mumpsData[:, 1:], measlesData[:, 1: ])
plt.show()


#%% d. plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('d. Monthly mumps vs measles cases (log scale)')

# 4. Your code is here
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measles cases')
plt.xscale('log')
plt.yscale('log')
plt.scatter(mumpsData[:, 1:], measlesData[:, 1:])
plt.axis([10**1.5, 10**3.5, 1, 10**5])
plt.show()


#%% Answer to e

# 5. Your code is here
answer = 'There are two main reasons to use logarithmic scales in charts and graphs. The first is to respond to skewness towards large values; i.e., cases in which one or a few points are much larger than the bulk of the data. The second is to show percent change or multiplicative factors'

print('\nAnswer to e: ' + answer)
