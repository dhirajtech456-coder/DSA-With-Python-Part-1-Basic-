num = int(input("Enter a number to check if it is an Armstrong number: "))
original_num = num
num_digits = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total += digit ** num_digits
    num //= 10
if total == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
