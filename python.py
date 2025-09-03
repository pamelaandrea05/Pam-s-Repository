row=int(input("Enter Row: "))
col=int(input("Enter Column: "))
search = int(input("Search number: "))

for x in range(1,row+1):
    for y in range(1,col+1):
        ans = x*y
        if search == ans:
            print(f"[{ans}]", end=" ")
        else:
            print(ans, end=" ")
    print()
    