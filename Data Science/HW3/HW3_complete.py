# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm




#%% Q1 Matrix multiplication
print("Question 1 **************************************")
A = np.array([
     [2, 8, 4],
     [5, 4, 2]])
B = np.array([
     [4, 1],
     [6, 4],
     [5, 3]])
C = np.array([
     [4, 1, 2],
     [6, 4, 3],
     [5, 3, 4]])
D = np.array([
     [4, 1, 2],
     [6, 4, 3]])

try:
  AB = A.dot(B)
  print("AB=", AB)
except ValueError:
  print("A can not multiplicate with B.")

try:
  AC = A.dot(C)
  print("AC=", AC)
except ValueError:
  print("A can not multiplicate with C.")

try:
  AD = A.dot(D)
except ValueError:
  print("A can not multiplicate with D.")

print("The multiplication requires the columns of first matrix is equal to the rows of second matrix.")

#%% Q2
print("Question 2 **************************************")

def zscore(arr):
  return (arr - np.mean(arr))/np.std(arr)
  
x = np.array([ 50, 68, 74, 70, 65, 61, 63, 74, 62])
y = np.array([170, 193, 209, 185, 195, 188, 188, 202, 183])

plt.scatter(x, y)

plt.show()

xScores = zscore(x)
yScores = zscore(y)

plt.scatter(xScores, yScores)

plt.show()

coeff = (xScores.dot(yScores))/len(xScores)
print("Pearsons Corr Coefficient: ", coeff)

print("Coefficient calculated by NumPy: ", np.corrcoef(x, y)[0,1])

print("The results are the same.")


#%% Q3

print("Question 3 **************************************")
x = np.array([ 50, 68, 74, 70, 65, 61, 63, 74, 62, 80])
y = np.array([170, 193, 209, 185, 195, 188, 188, 202, 183, 1000])

plt.scatter(x, y)

plt.show()

print("3b. Coefficient calculated by NumPy: ", np.corrcoef(x, y)[0,1])

xRank = np.argsort(np.argsort(x))
yRank = np.argsort(np.argsort(y))
spearmanCoeff = np.corrcoef(xRank, yRank)
print("3c. Spearman rank correlation coefficient: ", spearmanCoeff[0, 1])

print("3d. They are not the same. Comparing to the x and y in Question 2, there is an outlier (80, 1000). We expect the correlation coefficient is much closer to the coefficient in Question 2. Therefore, the Spearman correlation coefficient is better. The Spearman rank correlation works better with outliers.")

print("3e. 1: incidates a positive linear relationship between data points")
print("0: no or non-linear correlation")
print("-1: indicates a negative/inverse relationship")

#%% Q4
print("Question 4 **************************************")
print("norm.cdf(0.5) - norm.cdf(-0.5)\n")
print("2*(norm.cdf(0) - norm.cdf(-0.5)) or 2*(norm.cdf(0.5) - norm.cdf(0))\n")

#%% Q5
print("Question 5 **************************************")
print("5a. X' ~ ( aμ+b, (aσ)^2)\n")
print("5b. Z = (X- \u03BC)/σ\n")
print("5c. P(2<=X<=7) = norm.cdf(7, 5, 3) - norm.cdf(2, 5, 3) = ", norm.cdf(7, 5, 3) - norm.cdf(2, 5, 3))

print("5d. P(-1.5 <= X <= 1.5) = norm.cdf(1.5) - norm.cdf(-1.5) = ", norm.cdf(1.5) - norm.cdf(-1.5))

#%% Q6
print("Question 6 **************************************")

print("a: P(A ∪ B)   = P(A) + P(B) – P(A ∩ B)")
print("b: P(A | B)   = P(A ∩ B) / P(B)")
print("c: P(A ∩ B)   = P(B) * P(A | B)")
print("d: If A and B are independent, P(A ∩ B) = P(A) * P(B)")



#%% Q7
print("Question 7 **************************************")
print("P(d = even) = 1/2")
print("P(d < 5) = 1/2")
print("P(d = even) * P(d < 5) = 1/4")

print("P(d = even ∩ d < 5) = 2/8 = 1/4")

print("P(d = even) * P(d < 5) = P(d = even ∩ d < 5)")

print("Therefore, P(d = even) and P(d < 5) are independent.")

#%% Q8
print("Question 8 **************************************")
print("P( loaded | 6666) = P(6666 | loaded)*P(loaded)/P(6666)")
print("= P(6666 | loaded)*P(loaded)/(P(6666 | loaded)*P(loaded) + P(6666 | fair)*P(fiar))" )
print("= (0.5**4) * 0.05 / ((0.5**4) * 0.05 + ((1/6)**4)*0.95)")
print("=0.81")



#%% Q9
print("Question 9 **************************************")
print("A: have the disease, P(A) = 0.0001;")
print("B: test positive;")
print("P(A)+P(neg(A)) =1")
print("P(B)+P(neg(B)) =1")

print("9a")
print("P(B | A) = 0.999; P(B | neg(A)) = 0.0002;")
print("By Bayes Theorem, P(A | B) = P(B | A) * P(A) / P(B)")
print("=P(B|A)*P(A)/(P(B|A)*P(A) + P(B|neg(A))*P(neg(A)))")
print("= 33.3%")

print("9b")

print("P(neg(A)| neg(B)) = P(neg(B)|neg(A))*P(neg(A))/P(neg(B))")
print("= (1-P(B|neg(A)))*(1-P(A))/(1-P(B))")
print("=0.99999")


# close all figures
plt.close('all')

print("Question 10 **************************************")
#%% load data
import pandas as pd 
measles=pd.read_csv('Measles.csv',header=None).values
mumps=pd.read_csv('Mumps.csv',header=None).values
chickenPox=pd.read_csv('chickenPox.csv',header=None).values

#a. plot annual total measles cases in each year
plt.figure()
plt.title('a. NYC measles cases')
plt.plot(measles[:,0], measles[:, 1:].sum(1), '-*')
plt.xlabel('Year')
plt.ylabel('Number of cases')
plt.show()

#%% b. bar plot average mumps cases for each month of the year

plt.figure()
plt.title('b. Average monthly mumps cases')
plt.bar(range(1,13), mumps[:, 1:].mean(0))
plt.xlabel('Month')
plt.ylabel('Average number of cases')
plt.show()


#%% c. scatter plot monthly mumps cases against measles cases
mumpsCases = mumps[:, 1:].reshape(41*12)
measlesCases = measles[:, 1:].reshape(41*12)

plt.figure()
plt.title('c. Monthly mumps vs measles cases')
plt.scatter(mumpsCases, measlesCases)
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measels cases')
plt.show()


#%% d. plot monthly mumps cases against measles cases in log scale
plt.figure()
plt.title('d. Monthly mumps vs measles cases (log scale)')
plt.loglog(mumpsCases, measlesCases, '.')
plt.xlabel('Number of Mumps cases')
plt.ylabel('Number of Measels cases')
plt.show()



#%% Answer to Q10.e

answer = 'If plotted in linear space, the relationship between two variables is difficulty to see.'

print('\n\nAnswer to e: ' + answer)
