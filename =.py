def checkIfSame(number1,number2):
  if ((number1^number2)!=0):
    print("nos r not =")
  else:
    print("both nos r =")
number1=int(input("number 1:"))
number2=int(input("number 2:"))
checkIfSame(number1,number2)