#Simple greeting program

name= input("Enter your name:")
print("WELCOME",name)

#Greeting based on time
import datetime

hour = datetime.datetime.now().hour

if hour < 12:
    print("Good morning", name)
elif hour < 18:
    print("Good afternoon", name)
else:
    print("Good evening", name)



#Output:

#Enter your name:Eleven
#WELCOME Eleven
#Good afternoon Eleven    
