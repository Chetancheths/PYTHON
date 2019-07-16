# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:01:56 2019

@author: c.shivaji.pattar
"""

"""
Simple linear Regression
"""
#imorporting libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing datatset
#os.chdir("C:\\Users\\c.shivaji.pattar\\Desktop\\Python\\Machine Learning A-Z Template Folder\\Part 2 - Regression\\Section 4 - Simple Linear Regression")

dataset = pd.read_csv('salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

#splitiing teh dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

#Feature scaling dont need for simple linear regression
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScalar()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScalar
y_train = sc_y.fit_transform(y_train)"""

#Fitting Simple linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regresser = LinearRegression()
regresser.fit(X_train, y_train)


#predicting the test set results
y_pred = regresser.predict(X_test)


#visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regresser.predict(X_train), color='blue')
plt.title("Salary vs Experience (Training set)")
plt.xlabel("year of Experience")
plt.ylabel("Salary")
plt.show()



#visualising the test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regresser.predict(X_train), color='blue')
plt.title("Salary vs Experience (Training set)")
plt.xlabel("year of Experience")
plt.ylabel("Salary")
plt.show()





