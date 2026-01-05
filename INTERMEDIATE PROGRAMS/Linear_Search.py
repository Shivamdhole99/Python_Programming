lst = list(map(int, input("Enter the List:").split()))
key = int(input("Enter the Key:"))
for i in lst:
    if i == key:
        print("Found")
        break
else:
    print("Not Found")
