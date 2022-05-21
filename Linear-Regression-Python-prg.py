import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (6.0, 4.0)
# Preprocessing Input data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
plt.scatter(x, y)
plt.show()

X_mean = np.mean(x)
Y_mean = np.mean(y)

num = 0
den = 0
for i in range(len(x)):
    num += (x[i] - X_mean)*(y[i] - Y_mean)
    den += (x[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

print (m, c)

plt.scatter(x, y, color = "r",marker = "*", s = 100) 

# predicted response vector 
y_pred = c + m*x 

# plotting the regression line 
plt.plot(x, y_pred, color = "g") 

# putting labels 
plt.xlabel('x') 
plt.ylabel('y') 

# function to show plot 
plt.show()