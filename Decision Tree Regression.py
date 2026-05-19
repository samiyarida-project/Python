from sklearn.tree import DecisionTreeRegressor

# Input data (house size in 1000 sq ft)
X = [[1], [2], [3], [4], [5]]

# Output data (house price in lakhs)
y = [30, 50, 70, 90, 110]

# Create model
model = DecisionTreeRegressor()

# Train model 
model.fit(X, y)

# Predict house price
prediction = model.predict([[3]])

print("Predicted House Price:", prediction[0], "lakhs")
 
#Output:
Predicted House Price:70.0 lakhs
