# Import libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dataset
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Annual_Income": [15, 16, 17, 18, 80, 85, 90, 95],
    "Spending_Score": [39, 81, 6, 77, 40, 60, 90, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Select features for clustering
X = df[["Annual_Income", "Spending_Score"]]

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=2, random_state=42)

# Create clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Print final output
print("Customer Segmentation Result:\n")
print(df)

#Output:
Customer Segmentation Result:

   CustomerID  Annual_Income  Spending_Score  Cluster
0           1             15              39        0
1           2             16              81        0
2           3             17               6        0
3           4             18              77        0
4           5             80              40        1
5           6             85              60        1
6           7             90              90        1
7           8             95              95        1
