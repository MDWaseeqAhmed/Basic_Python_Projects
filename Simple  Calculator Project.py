print('SIMPLE CALCULATOR')  # Needs to be in Bold Letters

Num1=int(input("ENTER THE NUMBER 1:- "))
Num2=int(input("ENTER THE NUMBER 2:- "))
opr=input("Enter the Operator.(+,-,*,/):- ")
if opr=="+":
    print(Num1+Num2)
elif opr=="-":
    print(Num1-Num2)
elif opr=="*":
    print(Num1*Num2)
elif opr=="/":
    print(Num1/Num2)
else:
    print("RESULT NOT FOUND")