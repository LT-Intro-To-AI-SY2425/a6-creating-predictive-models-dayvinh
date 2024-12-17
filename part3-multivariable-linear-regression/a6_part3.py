import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)
#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)
#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y),2)

print(coef)
print(intercept)
print(r_squared)

#Loop through the data and print out the predicted prices and the 
#actual prices

print("***************")
print("Testing Results")

predict = model.predict(xtest)
predict = np.around(predict, 2)
print(predict)

print("\nPredictions for specific scenarios:")
pOneMiles = 89000
pOneAge = 10
prediction = model.predict([[pOneMiles, pOneAge]])
print(f"Predicted worth when miles is {pOneMiles} and age is {pOneAge}: {prediction}")

pTwoMiles = 150000
pTwoAge = 20
predictionTwo = model.predict([[pTwoMiles, pTwoAge]])
print(f"Predicted worth when miles is {pTwoMiles} and age is {pTwoAge}: {predictionTwo}")

for index in range(len(xtest)):
    actual = ytest[index] 
    predicted_y = [index] 
    x_coord = xtest[index] 
    print(f"miles: {x_coord[0]} age: {x_coord[1]}  Actual: {actual} Predicted: {predicted_y}")