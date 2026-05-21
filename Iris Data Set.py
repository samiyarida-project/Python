# Import libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset
flowers = load_iris()

# Input and output
inputs = flowers.data
targets = flowers.target

# Create Decision Tree model
tree = DecisionTreeClassifier()

# Train model
tree.fit(inputs, targets)

# Print accuracy
print("Accuracy:", tree.score(inputs, targets))

# Draw Decision Tree
plot_tree(
    tree,
    feature_names=flowers.feature_names,
    class_names=flowers.target_names,
    filled=True
)

# Display graph
plt.show()

#Output:
#Accuracy:1.0
