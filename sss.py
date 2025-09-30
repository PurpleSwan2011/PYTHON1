def print_factors(number):
    print("factors",number,"r")
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number=int(input("number"))
            
print_factors(number)