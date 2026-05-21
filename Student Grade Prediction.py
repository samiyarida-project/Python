#STUDENT GRADE PREDICTION
# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset
data = {
    'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
    'Attendance': [40, 50, 60, 65, 70, 75, 85, 95],
    'Grade': ['F', 'F', 'D', 'C', 'B', 'B', 'A', 'A']
}

# Convert to DataFrame
df = pd.DataFrame(data)

print("Full Dataset:")
print(df)

# Input and output
X = df[['Hours_Studied', 'Attendance']]
y = df['Grade']

# Split data (random but fixed using random_state)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\n Training Data (X_train):")
print(X_train)

print("\n Testing Data (X_test):")
print(X_test)

# Model
model = DecisionTreeClassifier()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("\n Accuracy:", accuracy_score(y_test, y_pred))




#Output:
Full Dataset:
   Hours_Studied  Attendance Grade
0              1          40     F
1              2          50     F
2              3          60     D
3              4          65     C
4              5          70     B
5              6          75     B
6              7          85     A
7              8          95     A

# Training Data (X_train):
   Hours_Studied  Attendance
5              6          75
0              1          40
7              8          95
3              4          65
6              7          85
4              5          70

 #Testing Data (X_test):
   Hours_Studied  Attendance
2              3          60
1              2          50

# Predicted Grades:
['D' 'F']

# Actual Grades:
['D' 'F']

# Accuracy: 1.0
