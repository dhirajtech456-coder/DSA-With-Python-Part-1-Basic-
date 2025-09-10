a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
original_a=a
original_b=b
while b>0:
    r=a%b
    a=b
    b=r
    GCD=a
print(GCD)

LCM=(original_a*original_b)//GCD
print(LCM)