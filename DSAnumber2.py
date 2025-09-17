#CATABAY,LEILA KATRINA

n = int(input("Please enter the value of n: "))


digits = str(n)
found = []  

for d in digits:
    if d.isdigit() and int(d) > 3:
        found.append(d)

# Print result
if found:
    for digit in found:
        print(digit)
else:
    print("none")