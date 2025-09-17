#CATABAY, LEILA KATRINA

def compatibility_score(name):

    score = 0
    for letter in name:
        
        if letter in "aeiou":
            score = score + 2
   
        elif letter == "j":
            score = score + 2
        elif letter == "b":
            score = score + 2
        elif letter == "k":
            score = score + 1
        elif letter == "t":
            score = score + 1
        elif letter == "q":
            score = score - 3
    
    score = score - (len(name) * 0.5)
    
    return int(score)


num_names = int(input("How many names do you want to check? "))

names = []
scores = []

i = 0
while i < num_names:
    name = input("Enter name: ").strip().lower()
    
    if not name.isalpha():
        print("Name can only have letters. Try again.")
        continue
    
    if name in names:
        print("You already entered that name. Try a different one.")
        continue
  
    names.append(name)
    scores.append(compatibility_score(name))
    i = i + 1


results = []
for j in range(len(names)):
    results.append([names[j], scores[j]])


results.sort(key=lambda x: (-x[1], x[0]))


print()
for item in results:
    print(item[0], ":", item[1])