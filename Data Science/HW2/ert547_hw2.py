#Download the file ert547_hw2.py; Open the file in Spyder; Run the code by clicking the “Run” button


from matplotlib import pyplot as plt
import numpy as np
import pdb
import pandas as pd
import datetime as DT
from matplotlib.dates import date2num



#Question 1
# Read the data from the file fdata.csv using read_csv() and save the data in df. 
# The reference of read_csv(): https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/ 
# You need to set the parameters (sep, parse_dates, index_col) in read_csv() properly
#df = pd.read_csv(XXX, sep=XXX, parse_dates=XXX, index_col=XXX)

#1. your code is here
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()

#Question 2


# Save the data in the variable "data"
# Each row is saved in a tuple 
#data = [('2016-10-03', 772.559998), ... ]

#2. your code is here
data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y,'r-o')

# Set the xtick locations
graph.set_xticks(x)

# Set the xtick labels
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data])

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
 # giving a title  
plt.title('Closing stock value of Alphabet Inc.') 

# Customize the grid

plt.minorticks_on()

plt.grid(which='major', color='red', linestyle='--')
plt.grid(which='minor', color='black', linestyle=':')
plt.show()




#Question 3

# please save assign the data in variables 
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
lang_pos = [i for i, _ in enumerate(languages)]
plt.bar(lang_pos, popularity, color='b')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.xticks(lang_pos, languages, rotation=90)
plt.subplots_adjust(bottom=0.4, top=.8)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()




#Question 4
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
lang_pos = [i for i, _ in enumerate(languages)]
plt.barh(lang_pos, popularity, color ='g')
plt.ylabel("Languages")
plt.xlabel("Popularity")
plt.title("Popularity of Programming Language")
plt.yticks(lang_pos, languages, rotation=0)
plt.subplots_adjust(bottom=0.4, top=.8)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

plt.show()

#Question 5
weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 
weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 
weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
weight=np.concatenate((weight1,weight2,weight3))
print(weight)
height=np.concatenate((height1,height2,height3))

plt.scatter(weight1, height1, marker='*', color='r')
plt.scatter(weight2, height2, marker='*', color='g')
plt.scatter(weight3, height3, marker='*', color='b')
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
plt.show()


