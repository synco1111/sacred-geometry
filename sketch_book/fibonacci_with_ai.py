# The following is an Fibonacci implentation base on linear regression
# as describe in: https://towardsdatascience.com/teaching-ai-the-fibonacci-sequence-849430397963

#predicting fibonacci sequence with linear regression
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

fibonacci = pd.DataFrame([[1, 1, 2], 
                          [2, 1, 3], 
                          [3, 2, 5],
                          [5, 3, 8],
                          [8, 5, 13]
])
fibonacci.columns = [0, 1, 2]
fibonacci.iloc[0]
print(fibonacci)
# Training the model
reg = LinearRegression().fit(fibonacci[[0, 1]], fibonacci[2])
reg.score(fibonacci[[0, 1]], fibonacci[2])
#given any 2 numbers, the model will return their sum as properly learned from the training data
def pred(x):
  return reg.predict(np.array([x]))

list1 = [4, 7]
for k in range(5):
  #the np results of prediction for 1+1 may be 1.999999: transformed into an int, it becomes one. I am using rint to round it to the closest numpy int, then converting it into an int
  list1.append(int(np.rint(pred([list1[k], list1[k+1]]))))
print(list1)