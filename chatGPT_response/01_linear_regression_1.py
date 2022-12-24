# input: plot a linear regression with Python using numpy and matplotlib
# human fix:
# pip install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Generate some fake data for the regression
np.random.seed(0)
x = np.random.rand(100, 1)
y = 2 + 3 * x + np.random.rand(100, 1)

# Add a column of ones to x so that we can fit an intercept term
X = np.c_[np.ones((100, 1)), x]

# Compute the least squares solution using the normal equations
theta = np.linalg.inv(X.T @ X) @ X.T @ y

# Make some predictions on a new set of x values
x_new = np.array([[0], [1]])
X_new = np.c_[np.ones((2, 1)), x_new]
y_pred = X_new @ theta

# Plot the data and the regression line
plt.plot(x, y, "b.")
plt.plot(x_new, y_pred, "r-")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.axis([0, 1, 0, 10])
plt.show()