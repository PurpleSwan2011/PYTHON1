def totalFlips(number1,number2):
    flips=0
    while(number1>0 or number2>0):
        t1=(number1&1)
        t2=(number2&1)
        if(t1!=t2):
            flips+=1
        number1>>=1
        number2>>=1
    return flips
number1=int(input("enter first no"))
number2=int(input("enter second no"))
print("\nnumber of flips:",totalFlips(number1,number2))