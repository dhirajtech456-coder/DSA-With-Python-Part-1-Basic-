import math
def is_prime(num):
    if num<=1:
        return False
    if num %2==0:
        return False
    if num == 2:
        return True
    else:
        for i in range (3,int(math.sqrt(num))+1,2):
            if num % i==0:
                return False
        return True
print(is_prime(2))
print(is_prime(5))
print(is_prime(1))
print(is_prime(4))
print(is_prime(9))
