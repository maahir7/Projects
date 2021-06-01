#Download the file ert547_hw5.py; Open the file in Spyder; Run the code by clicking the “Run” button
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import pdb
from csv import reader
from random import seed
from random import randrange
from sklearn import linear_model
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2

##%% Question 1
# Since we have three points to fit
# Lets define list x_data and y_data for points
x_data = np.array([ 0.5 , 2 , 3 ])
y_data = np.array([ 1 , 2.5 , 3 ])
# Lets get y_predicted value for all four models
y_predicted = []
# Defining parameter of models
model = [(1 , 0.5) , (1 , 1) , (0.8 , 0.3) , (0.8 , 0.7)]
for model_i in model:
    (a , b) = model_i
    y = []
    for x in x_data:
            yi = a * x + b
            y.append(yi)
    y_predicted.append(y)
y_predicted = np.array(y_predicted)
# Now we will calculate error for each model
error = []
for y_pred in y_predicted:
    error.append(np.sum(np.power(y_data - y_pred , 2)) / len(y_pred))
# Displaying error obtained from each model
for i in range(0 , len(error)):
    print("Error obtained from model {} is {} ".format(i , error[i]))



##%% Question 2
print('''
If your modeling problem is that you have too many features, a solution to this problem is LASSO regularization. By forcing some feature coefficients to be zero, you remove them, thus reducing the number of features that you are using in your model. LASSO solves the problem of too many features through feature selection. Ridge regression is primarily a tool for dealing with collinearity. It does this by allowing some bias in exchange for greatly reducing the variance of the estimators.

Difference

1. Lasso and Ridge are all part of the Linear Regression family where the x (input) and y (output) are assumed to have a linear relationship. The main difference among them is whether the model is penalized for its weights.

2. Lasso is a modification of linear regression, where the model is penalized for the sum of absolute values of the weights. During training, the objective function become:

(1/2m) Σ(y- Χw)^2 + alpha Σ|Wj| 

As you see, Lasso introduced a new hyper parameter, alpha, the coefficient to penalize weights.

3. Ridge takes a step further and penalizes the model for the sum of squared value of the weights. Thus, the weights not only tend to have smaller absolute values and more evenly distributed, but also tend to be close to zeros. The objective function becomes:

Σ(y- Χw)^2  + alpha Σ Wj^2

4. Lasso tends to give sparse weights (most zeros), because the l1 regularization cares equally about driving down big weights to small weights, or driving small weights to zeros. If you have a lot of predictors (features), and you suspect that not all of them are that important, Lasso may be really good idea to start with.

5. Ridge tends to give small but well distributed weights, because the l2 regularization cares more about driving big weight to small weights, instead of driving small weights to zeros. If you only have a few predictors, and you are confident that all of them should be really relevant for predictions, try Ridge as a good regularized linear regression method.

Advantage of Lasso regression

There are many advantages in using LASSO method, first of all it can pro- vide a very good prediction accuracy, because shrinking and removing the coefficients can reduce variance without a substantial increase of the bias, this is especially useful when you have a small number of observation

Disadvantage of LASSO:

LASSO selects at most n variables before it saturates. LASSO can not do group selection. If there is a group of variables among which the pairwise correlations are very high, then the LASSO tends to arbitrarily select only one variable from the group

Advantage of ridge regression

Advantage is coefficient shrinkage and reducing model complexity.  The most important one is that it penalizes the estimates. Adding a penalty term reduces overfitting. Second, the penalty term guarantees that we can find a solution.

Disadvantage of ridge regression

It will shrink the coefficients for least important predictors, very close to zero. But it will never make them exactly zero. In other words, the final model will include all predictors. However, in the case of the lasso, the L1 penalty has the effect of forcing some of the coefficient estimates to be exactly equal to zero when the tuning parameter λ is sufficiently large.
''') 

##%% Question 3
def gini(c1,c2):
   return 1 - (c1/(c1+c2))**2 - (c2/(c1+c2))**2

def entropy(c1,c2):
   return - (c1/(c1+c2))*np.log2(c1/(c1+c2)) - (c2/(c1+c2))*np.log2(c2/(c1+c2))

def classification_error(c1,c2):
   return 1 - np.max([c1/(c1+c2),c2/(c1+c2)])

def gini_split(c1,c2,c3,c4,c5,c6):
   return ((c3+c4)/(c1+c2))*gini(c3,c4) + ((c5+c6)/(c1+c2))*gini(c5,c6)

def entropy_split(c1,c2,c3,c4,c5,c6):
   return entropy(c1,c2) - (((c3+c4)/(c1+c2))*entropy(c3,c4) + ((c5+c6)/(c1+c2))*entropy(c5,c6))

def classification_error_split(c1,c2,c3,c4,c5,c6):
   return classification_error(c1,c2) - (((c3+c4)/(c1+c2))*classification_error(c3,c4) + ((c5+c6)/(c1+c2))*classification_error(c5,c6))

print ("a left gini index = ",gini(3,9))

print ("a right gini index = ",gini(17,1))

print ("b left gini index = ",gini(10,5))

print ("b right gini index = ",gini(10,5))

print ("c left gini index = ",gini(19,2))

print ("c right gini index = ",gini(1,8))

print("\n")

print ("a left entropy = ",entropy(3,9))

print ("a right entropy = ",entropy(17,1))

print ("b left entropy = ",entropy(10,5))

print ("b right entropy = ",entropy(10,5))

print ("c left entropy = ",entropy(19,2))

print ("c right entropy = ",entropy(1,8))

print("\n")

print ("a left misclassification  error = ",classification_error(5,12))

print ("a right misclassification  error = ",classification_error(20,3))

print ("b left misclassification  error = ",classification_error(12,8))

print ("b right misclassification  error = ",classification_error(12,8))

print ("c left misclassification  error = ",classification_error(20,5))

print ("c right misclassification  error = ",classification_error(5,10))

print("\n")

print ("a gini index splitting = ",gini_split(20,10,3,9,17,1))

print ("b gini index splitting = ",gini_split(20,10,10,5,10,5))

print ("c gini index splitting = ",gini_split(20,10,19,2,1,8))

print("\n")

print ("a entropy splitting = ",entropy_split(20,10,3,9,17,1))

print ("b entropy splitting = ",entropy_split(20,10,10,5,10,5))

print ("c entropy splitting = ",entropy_split(20,10,19,2,1,8))

print("\n")

print ("a misclassification error splitting = ",classification_error_split(30,10,5,12,20,3))

print ("b misclassification error splitting = ",classification_error_split(30,10,12,8,12,8))

print ("c misclassification error splitting = ",classification_error_split(30,10,20,5,5,10))

print("\n")

print('''
conclusion:

Based in the following    

1. Gini index splitting - Minimum (0.0) when all records belong to one class,implying most interesting information
2. Enthropy splitting - Measures Reduction in Entropy achieved because of the split. Choose the split that achieves most reduction (maximizes GAIN)
3. Misclassification error splitting - Measures Reduction in error achieved because of the split. Choose the split that achieves most reduction (maximizes error).
    
Thus c > a > b is the order of best choices. 
''')


##%% Question 4
print('''
Training Error at parent node A = 10/30 = 0.34

So, Pessimistic error at parent node A = (10 + 0.5)/30 = 10.5/30 = 0.35

As we know , For a tree with 30 leaf nodes and 10 errors ,training error reduced by 1%

Hence, Training Error at leaf nodes = 9/30 = 0.30

Error in 1 leaf node is : e’(t) = (e(t)+0.5) where e(t) = training error. ( given )

Hence , Total errors for 4 leafs are : e’(t) = e(t) + 4 × 0.5.

Pessimistic error at leaf nodes = (9 + 4 × 0.5)/30 = 11/30 = 0.37

Yes, this tree should be pruned as Pessimistic error at leaf nodes is more than Pessimistic error at parent node A [ Pessimistic error at leaf nodes ( 0.37 ) > Pessimistic error at parent node A ( 0.35 ) ]

Tree should be PRUNED !
''') 


##%% Question 5
# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Convert string column to integer
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
        print('Class %s ID => %d' % (value, i))
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup

# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for _ in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):

    distance = 0.0
    ### your code starts
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    ### your code ends
    return sqrt(distance)


# Locate the most similar neighbors and return the list of neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
    ### your code starts
        dist = euclidean_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    ### your code ends
    
    neighbors = list()
    for i in range(num_neighbors):
      neighbors.append(distances[i][0])
    return neighbors


# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    ### your code starts
	# get all neighbors and make the prediction based on majority of neighbors
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    ### your code ends
    return prediction

# kNN Algorithm
def k_nearest_neighbors(train, test, num_neighbors):
    predictions = list()
    for row in test:
        output = predict_classification(train, row, num_neighbors)
        predictions.append(output)
    return(predictions)


# Test the kNN on the Iris Flowers dataset
seed(1)
filename = 'iris.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)

# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)

# evaluate algorithm
n_folds = 5
num_neighbors = 5
scores = evaluate_algorithm(dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
# the output is

#The output scores is 96.66666666666667
#The mean accuracy is 96.667%

