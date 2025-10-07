def hcf(numberSmallest,numberLargest):
    while(numberSmallest):
        numberStore=numberSmallest
        numberSmallest=numberLargest%numberSmallest
        numberLargest=numberStore
    return numberLargest
numberLargest=int(input("largest no:"))
numberSmallest=int(input("smallest no"))
lcm=int((numberSmallest/hcf(numberSmallest,numberLargest))*numberLargest)
print("LCM is:",lcm)