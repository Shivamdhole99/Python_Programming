n = int(input("Enter a Number:"))
temp = n
sum = 0
while temp > 0:
    d = temp % 10
    sum += d ** 3
    temp //= 10

if sum == n:
    print("The Number is Armstrong")
else:
    print("The Number is Not Armstrong")
