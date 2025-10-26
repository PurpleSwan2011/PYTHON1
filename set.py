def setOrNot(number,n):
    if number&(1 <<(n-1)):
        print("\nset")
    else:
        print("\nnot set")
number=int(input("number"))
n=int(input("bit no"))
setOrNot(number,n)