from sklearn.linear_model import LogisticRegression
import numpy as np

# Marks
X = np.array([30, 40, 50, 60, 70]).reshape(-1, 1)

# Pass(1) / Fail(0)
y = np.array([0, 0, 0, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict for 65 marks
prediction = model.predict([[65]])

# Probability
probability = model.predict_proba([[65]])

print("Prediction:", prediction[0])
print("Probability:", probability)


#Output:
#Prediction: 1
#Probability: [[0.12 0.88]]
