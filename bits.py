def numberOfBits(n):
    count=0
    while (n):
        count += 1
        n>>=1
    return count
number=int(input("number:"))
print("total bits:", numberOfBits(number))