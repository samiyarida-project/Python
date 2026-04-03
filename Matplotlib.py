import matplotlib.pyplot as plt
#Line Graph

x=[1,2,3,4]
y=[10,20,30,40]
 
plt.plot(x,y)
plt.title("Line Graph")
plt.show()

#Bar Graph

Subjects=["Pyhton","Java","C++","DBMS"]
marks=[80,90,75,90]

plt.bar(Subjects,marks)
plt.title("Bar Graph")
plt.show()

#Pie Chart

activities=["Study","Sleep","Mobile","Exercise","playing"]
hours=[6,8,5,3,2]
plt.pie(hours,labels=activities,autopct='%1.1f%%')
plt.title("Daily Activities Pie Chart")
plt.axis('equal')

plt.tight_layout()

#Show All plots
plt.show()
