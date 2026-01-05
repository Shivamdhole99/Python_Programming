s = input("Enter a String:")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count +=1
print("Vowels is ",count)