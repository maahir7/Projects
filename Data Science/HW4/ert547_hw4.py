#Download the file ert547_hw3.py; Open the file in Spyder; Run the code by clicking the “Run” button
#%% import necessary modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pdb



##Q1, 20pts
#%% Q1a, 15pts
# the plot is not required
#Your code is here
x = np.array([2005, 2006, 2007, 2008, 2009]).reshape((-1, 1))
x1 = np.array([2005, 2006, 2007, 2008, 2009,2012]).reshape((-1, 1))
y = np.array([12, 19, 29, 37, 45])
model = linear_model.LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(x1)
print('predicted response:', y_pred)
# naming the x axis 
plt.xlabel('Year') 
# naming the y axis 
plt.ylabel('Sales(in million dollars)') 
# giving a title to the graph 
plt.title('Sales per Year')
plt.scatter(x,y)
plt.plot(x1, y_pred, color='red')
plt.show()
#%%Q1b, 5pts
#Your code is here


print('\nEstimated sales in 2012 is, 70 million\n')


#%% Q2, 20 pts 
#Q2a, 15pts, just output the formula directly

from math import factorial
def nchoosek(n, k):
     return factorial(n) / factorial(k) / factorial(n-k)
def binomPMF(k, n, p):
     return nchoosek(n, k) * p**k * (1-p)**(n-k)
 
print ('P(at least 12 heads | coin is fair) =',sum([binomPMF(i, 15, 0.5) for i in range(12,16)]))

print('\n')

print('P(at least 12 heads or 12 tails | coin is fair) =', 2*(sum([binomPMF(i, 15, 0.5) for i in range(12,16)])))
  
print('\n')

#Q2b, 5pts, just output either 'accept' or 'reject'
print('We reject H0 as probability is less than or equal to the p-value. This is strong evidence that the null hypothesis is invalid.')

print('\n')

#%% Q3 setup, 70pts
import scipy.stats as stats
import numpy.random as rn
#%% Q3a, 15pts
rn.seed(0)
N = 16;
m = 10**5;
# 10**5 by 16 = 16 + 16 + ... + 16
# use the uniform or binomial functions to generate the data
nHeads = (rn.uniform(size=(m, N))>0.5).sum(1)

#%%plot the histgram
# Your code is here
# naming the x axis 
plt.xlabel('nHeads') 
# naming the y axis 
plt.ylabel('Number of coins') 
# giving a title to the graph 
plt.title('Q3a: Histogram')
plt.hist(nHeads, bins = range(18))
plt.show()

#%% Q3b, 15pts
# using plt.hist with parameter and density
#Your code is here
#nHeads =hist(prglength, bins=18)# naming the x axis 
counts, bins = np.histogram(nHeads, bins = range(18))
counts = counts/sum(counts)
# naming the x axis 
plt.xlabel('k') 
# naming the y axis 
plt.ylabel('P(nHeads = k)') 
# giving a title to the graph 
plt.title('Q3b: Probability Mass Function')

plt.hist(bins[:-1], bins, weights = counts)


plt.show()

#%% Q3c, 15pts

#You can calculate the probabilities/counts with your own code or using values returned from 2a/2b.
# Your code is here


# Now find the cdf
cdf = np.cumsum(counts)
# naming the x axis 
plt.xlabel('k') 
# naming the y axis 
plt.ylabel('P(nHeads = k)') 
# giving a title to the graph 
plt.title('Q3c: Cumulative Distribution Function')
# And finally plot the cdf
plt.plot(bins[:-1], cdf)
plt.show()


#%% Q3d, 25pts
# Use the binomial distribution CDF (use scipy.stats.binom.cdf)
import scipy
# Your code is here

def binomcdf():
    p = 0.5
    n = 16
    x = 0
    result = []
    for a in range(17):
        result.append(scipy.stats.binom.cdf(x, n, p))
        x += 1
    return result

# scatter plot
# Your code is here

# naming the x axis 
plt.xlabel('Empirical CDF') 
# naming the y axis 
plt.ylabel('Theoretical CDF') 
# giving a title to the graph 
plt.title('Q3d: scatter plot')
# And finally plot the cdf
plt.scatter(cdf, binomcdf())

plt.show()


# line plot
#Your code is here
# naming the x axis 
plt.xlabel('k') 
# naming the y axis 
plt.ylabel('CDF') 
# giving a title to the graph 
plt.title('Q3d: line plot')
# And finally plot the cdf
#plt.plot(bins[:-1], binomcdf(),cdf)
plt.plot(bins[:-1], cdf, 'o-',color='Blue', label='Empirical CDF')
plt.plot(bins[:-1], binomcdf(), 'o-',color='Orange', linestyle='dashed', label='Theoretical CDF')
plt.legend()
plt.show()

# Loglog scale plot
#your code is here

# naming the x axis 
plt.xlabel('Empirical CDF') 
plt.xscale("log")
# naming the y axis 
plt.ylabel('Theoretical CDF') 
plt.yscale("log")
# giving a title to the graph 
plt.title('Q3d:loglog plot')
# And finally plot the cdf
plt.plot(cdf, binomcdf(), 'o')
plt.show()






