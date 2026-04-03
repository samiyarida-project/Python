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

