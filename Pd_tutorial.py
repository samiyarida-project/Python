import pandas as pd
data={
    "Name":["Harry","sara","john"],
    "Marks":[85,90,89],
    "College":["ABC College","ABC College","ABC College"]
    
   
    }

df=pd.DataFrame(data)

print(df)

print("\n Highest Marks:",df["Marks"].max())
print("\n Average Marks:",df["Marks"].mean())
print("\n Lowest Marks:",df["Marks"].min())

output:
   Name  Marks      College
0  Harry     85  ABC College
1   sara     90  ABC College
2   john     89  ABC College

 Highest Marks: 90

 Average Marks: 88.0

 Lowest Marks: 85

