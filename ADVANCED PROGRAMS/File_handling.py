f = open("data.txt", "w") #Create a file dta
f.write("Hello Python") #write the text in file
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()
