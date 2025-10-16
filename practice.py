# Count Frequency of Each Element in a List

# Sample list
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Empty dictionary to store frequency
frequency = {}

# Loop through each item in the list
for item in items:
    if item in frequency:
        frequency[item] += 1  # Increment count if already present
    else:
        frequency[item] = 1   # Add item with count 1 if not present

# Print result
print("Element Frequency:")
for key, value in frequency.items():
    print(f"{key}: {value}")
