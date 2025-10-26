def FirstSetBit(number):
    position=1
    mask=1
    while(not(number&mask)):
        mask=mask<<1
        position+=1
    return position
number=int(input("no"))
print("position",FirstSetBit(number))