def powerOf4(number):
    count=0
    if number==(number &(~(number-1))):
        while(number>1):
            number >>=1
            count=count+1
        if count % 2==0:
            print("4^",count//2)
            return True 
        else:
            return False
number=int(input("number"))
if (powerOf4(number)):
    print(number,'is apo of 4')
else:
    print(number,'is notapo of 4')