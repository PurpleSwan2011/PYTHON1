def powerOf8(number):
    bitPosition=0
    mask=1
    while (bitPosition<=63):
        mask<<=bitPosition
        if (mask==number):
            return True
        bitPosition+=3
        mask=1
    return False
number=int(input("number"))
if(powerOf8(number)):
    print("yes",number,"pow of 8")
else:
    print("No",number,"not a pow of 8")