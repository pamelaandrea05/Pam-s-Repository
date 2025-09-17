#CATABAY, LEILA KATRINA

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
z1 = int(input("Enter z1: "))
z2 = int(input("Enter z2: "))


bit_x = (x1 >> x2) & 1
bit_y = (y1 >> y2) & 1
bit_z = (z1 >> z2) & 1


result = bit_x & bit_y & bit_z


print(result)