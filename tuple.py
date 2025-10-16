# 1️⃣ Swap Tuples
print("\n--- Swap Tuples ---")
# Get user input for two tuples (as comma-separated values)
tuple1 = tuple(input("Enter values for first tuple (comma-separated): ").split(","))
tuple2 = tuple(input("Enter values for second tuple (comma-separated): ").split(","))

print("Before swap:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Swapping using a temporary variable
tuple1, tuple2 = tuple2, tuple1

print("After swap:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)


# 2️⃣ Tuple Unpacking
print("\n--- Tuple Unpacking ---")
# Get a tuple with exactly 3 values to unpack
input_tuple = tuple(input("Enter exactly 3 values (comma-separated): ").split(","))

if len(input_tuple) != 3:
    print("Error: You must enter exactly 3 values to unpack.")
else:
    a, b, c = input_tuple
    print("Unpacked values:")
    print("a =", a)
    print("b =", b)
    print("c =", c)


# 3️⃣ Zip Lists into Tuple List
print("\n--- Zip Lists into Tuple List ---")
list1 = input("Enter first list of items (space-separated): ").split()
list2 = input("Enter second list of items (space-separated): ").split()

# Use zip to combine them
zipped = list(zip(list1, list2))

print("Zipped list of tuples:")
print(zipped)
