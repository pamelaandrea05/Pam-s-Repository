sentence = input("Enter your sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequency: ")
for word, count in frequency.items():
    print(f"{word}: {count}")
