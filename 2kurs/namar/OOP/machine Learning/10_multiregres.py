

import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

# it is like linear regression But to predict a value based on two or more variables
X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict the CO2 emission of a car where the weight is
# 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print([predictedCO2])  # output: [107.2087328]
print([df])  # output: [107.2087328]
