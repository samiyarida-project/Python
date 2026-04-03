from sklearn.tree import DecisionTreeClassifier
 
#Study hours
x=[[1],[2],[3],[4],[5]]

#Result(0= fail,1=pass)
y=[0,0,1,1,1]

model=DecisionTreeClassifier()

model.fit(x,y)

#prediction
result1=model.predict([[2]])
result2=model.predict([[4]])
result3=model.predict([[5]])


print("2 hours study:",result1)
print("4 hours study:",result2)
print("5 hours study:",result3)

