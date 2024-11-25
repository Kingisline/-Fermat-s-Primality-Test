import math


def fun():
    prime =int(input("Enter the prime number: "))
    
# base value or it can be changed as any prime number below the target value.
    a = 2

    fermat = prime - 1
    fermat = math.pow(a, fermat)
    # print(fermat)

    result = fermat % prime
    if(result == 1):
        print("The given number", prime, "is a prime number")
        pass
    else:
        print("The given number", prime, "is not a prime number")



    
while True:
    fun()