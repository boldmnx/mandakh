import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

# oyutnii suraltssan tsag bolon 30onooni shalgalt hoorondin hamaaral


# x = numpy.random.uniform(0.0, 5.0, 250)
data = {
    "grade": [20, 25, 10, 30,],
    "time": [30, 35, 20, 50]
}
df = pd.DataFrame(data)

plt.xlabel('суралцсан цаг')
plt.ylabel('30онооны шалгалт')
plt.scatter(df.time, df.grade)


reg = linear_model.LinearRegression()
reg.fit(df[['time']], df.grade)

pr = reg.predict([[47]])

# plt.show()
