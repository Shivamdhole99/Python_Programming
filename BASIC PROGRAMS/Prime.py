n = int(input("Enter a Number:"))

if n > 1:
    for i in range(2,n):
        if n % i== 0:
            print("The Number is not Prime")
            break
    else:
        print("The Number is Prime")