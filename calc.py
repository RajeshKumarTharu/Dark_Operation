num1=int(input("enter 1st num:"))
num2=int(input("enter 2nd num:"))
print("choose calculation:\n" 
       "add\n ",
       "subtract\n",
       "multiply\n",
        "divide\n",)

calc=input()
if calc=="add":
    ans=num1+num2
elif calc=="subtract":
       ans=num1-num2
elif calc=="multiply":
       ans=num1*num2
elif calc=="divide":
       ans=num1/num2 
print(ans)   