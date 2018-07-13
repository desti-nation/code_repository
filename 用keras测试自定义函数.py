import keras
import keras.backend as K
import numpy as np

def smoothL1(y_true, y_pred):
   x   = K.abs(y_true - y_pred)
   print(x)
   x   = K.switch(x < 1, 0.5 * x ** 2, x - 0.5)
   return  K.sum(x)

y_true = K.variable(np.array([[10, 10, 1, 5], [10, 10, 1, 5]]))
y_pred = K.variable(np.array([[5, 3, 2, 2], [5, 3, 2, 2]]))
print(K.eval(smoothL1(y_true, y_pred)))