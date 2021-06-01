from matplotlib import pyplot as plt
import numpy as np
import pdb
import pandas as pd

#Question 1
# Read the data from the file fdata.csv using read_csv() and save the data in df. 
# The reference of read_csv(): https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/ 
# You need to set the parameters (sep, parse_dates, index_col) in read_csv() properly

df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)

# plot the figure
df.plot()

plt.show()

#Question 2


# Save the data in the variable "data"
# Each row is saved in a tuple 
data = [('2016-10-03', 772.559998),
        ('2016-10-04', 776.429993),
        ('2016-10-05', 776.469971),
        ('2016-10-06', 776.859985),
        ('2016-10-07', 775.080017 )]


print(data)

x = [date for (date, value) in data]
y = [value for (date, value) in data]

# Plot the data as a red line with round markers
plt.plot(x,y,'r-o')

plt.xticks(x)

# set the ticks, labels, titles, grids
# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
# giving a title
plt.title('Closing stock value of Alphabet Inc.')
# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()

# Customize the major grid
#plt.grid(which=XXX, linestyle=XXX, linewidth=XXX, color=XXX)
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')


plt.show()


#Question 3

# please save assign the data in variables 
#popularity = [XXX, XXX, ...]
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

# plot the bar chart 
# plt.XXX(XXX, XXX, color=XXX)
plt.bar(x_pos, popularity, color='blue')

# set ticks, labels, titles, grids
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

#Question 4
# save the data in variables
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
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
plt.scatter(weight, height, marker='*', color=['red']*10 + ['green']*10 +['blue']*10)
plt.xlabel('Weight', fontsize=16)
plt.ylabel('Height', fontsize=16)
plt.title('Group Wise Weight vs Height',fontsize=20)
plt.show()

