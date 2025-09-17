for x in range(1,101):
    print(f"{x}", end=" ")
    if x%5==0:
        print()
        print()
        
for x in range(1,6):
    for y in range(6,11):
        print(f"{x}{y}", end=" ")
    print()


for x in range(10,0,-1):
    print(f"{x}", end=" ")
        
while True:
    print("Enter number: ")
    x=int(input())
    if x==0 or x<0:
        break