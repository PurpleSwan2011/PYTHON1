number=int(input("Input ur no"))
digits=len(str(number))
resultNumber=0
temp=number
while temp>0:
    digit=temp%10
    resultNumber+=digit ** digits
    temp//=10
    if number==resultNumber:
        print(number,"amstrong")
    else:
        print(number,"not amstrong")