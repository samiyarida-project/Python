from sklearn.linear_model import LinearRegression
import numpy as np

# Experience in years (input)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

# Salary in thousands (output)
y = np.array([20, 25, 30, 35, 40])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict salary for 6 years experience
prediction = model.predict([[6]])
print("Predicted Salary:", prediction[0], "thousand")


#Output:
#Predicted Salary: 45.0 thousand


