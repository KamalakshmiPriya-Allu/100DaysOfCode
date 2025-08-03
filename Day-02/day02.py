#Tip Calculator
print("Welcome to the tip calculator!!")
Bill = float(input("What was the total bill?"))
Tip = int(input("How much tip would you like to give?"))
Total = Tip/100*Bill+Bill
print("Total Amount:" + str(Total))
People = int(input("No of people:"))
Per_Person = Total/People
print("Amount per person:" + str(Per_Person))

