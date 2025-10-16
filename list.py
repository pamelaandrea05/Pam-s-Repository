#sum of numbers list
def lst(promt):
     return list(map(int,input(promt).split()))

numbers = lst("Enter number: ")
sum = 0
for num in numbers:
    sum += num

    print("The sum of numbers ", sum)

#for duplicate(magremove)
names = input("Enter names: ").split()
overall = []
for name in names:
    if name not in overall:
            overall.append(name)

    print("List of names after removing duplicate ", overall)

#ito reverse     
orig = input("Enter names: ").split()
reversed_lst = []


for i in range(len(orig) - 1, -1, -1):
     reversed_lst.append(orig[i])

     print("The reversed list: ", reversed_lst)


#ito nestedlist na ifaflat
flat = []
nested_lst = int(input("Sublists: "))
for i in range(nested_lst):
     sublist = lst(f"Enter number for sublist {i+1}:")
     flat.append(sublist)

     
flattened = []
for sublist in flat:  
     for item in sublist:
          flattened.append(item) 
     print("The flattened: ", flattened)

#magdetermine ng largest
nums = lst("Enter numbers: ")

unique = list(set(numbers))

if (len(nums)) < 2:
     print("Not enough")
else:
     unique.sort()
     print("The 2nd largest number is ", unique[-2])