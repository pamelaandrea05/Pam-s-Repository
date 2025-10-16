# 1️⃣ Count Frequency
print("\n--- Count Frequency of Elements in a List ---")
items = input("Enter elements (separated by spaces): ").split()

frequency = {}
for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency Dictionary:")
print(frequency)


# 2️⃣ Merge Dictionaries
print("\n--- Merge Two Dictionaries ---")
# Get first dictionary input
dict1 = {}
n1 = int(input("Enter number of key-value pairs for first dictionary: "))
for _ in range(n1):
    key = input("Key: ")
    value = input("Value: ")
    dict1[key] = value

# Get second dictionary input
dict2 = {}
n2 = int(input("Enter number of key-value pairs for second dictionary: "))
for _ in range(n2):
    key = input("Key: ")
    value = input("Value: ")
    dict2[key] = value

# Merge the dictionaries (dict2 values override dict1)
merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged Dictionary:")
print(merged_dict)


# 3️⃣ Group by First Letter
print("\n--- Group Words by First Letter ---")
words = input("Enter words (separated by spaces): ").split()
grouped = {}

for word in words:
    first_letter = word[0].lower()
    if first_letter not in grouped:
        grouped[first_letter] = [word]
    else:
        grouped[first_letter].append(word)

print("Grouped Dictionary:")
print(grouped)


# 4️⃣ Invert Dictionary
print("\n--- Invert a Dictionary ---")
inv_dict = {}
n = int(input("Enter number of key-value pairs for dictionary to invert: "))
for _ in range(n):
    key = input("Key: ")
    value = input("Value: ")
    inv_dict[key] = value

# Invert (assuming values are unique)
inverted = {value: key for key, value in inv_dict.items()}

print("Inverted Dictionary:")
print(inverted)
