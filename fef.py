#function
def numberOfBits(n):
    ones=0
    zeros=0
    #right shift
    while(n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n >>=1
    print("\n\nones=",ones,"\nzeros",zeros)
number=int(input("number"))
numberOfBits(number)