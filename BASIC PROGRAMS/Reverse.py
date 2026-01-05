n = int(input("Enter the Number:"))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //=10
print("The Number is ",rev)