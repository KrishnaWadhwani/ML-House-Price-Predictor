from matplotlib import style
import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.DataFrame({'Id':[1, 2, 3, 4, 5],
                          'Floor': [1, 2, 3, 4, 5],
                         'Price': [500, 900, 800, 956, 745]},columns=['Floor','Price'])
dataframe.plot(x = 'Floor', y = 'Price', kind = "scatter")
from statistics import mean
import numpy as np
x = np.array(dataframe.Floor, dtype=np.float64)
y = np.array(dataframe.Price, dtype=np.float64)
def line(x, y):
    m = ( ((mean(x) * mean(y)) - mean(x*y)) /
           ((mean(x)* mean(x)) - mean(x * x)) )
    b = mean(y) - m*mean(x)
    return m, b

m,b = line(x, y)
print("Best Fit Slope:", m,"Best Fit Line:", b)
style.use('fivethirtyeight')

regression_line = [(m*x)+b for x in x]
predict_x = int(input('Which Floor Price To Predict: '))
predict_y = (m*predict_x)+b
print('Cost Of This Floor Is: ', predict_y)
plt.scatter(x,y)
plt.scatter(predict_x, predict_y)
plt.plot(x, regression_line)
plt.show()

Another Dataset

dataframe = pd.DataFrame({'Id':[1],
                          'Floor': [7, 8, 9],
                         'Price': [7400000, 7200000, 7000000]},columns=['Floor','Price'])