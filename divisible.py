# Get input from the user
number = int(input("Enter an integer: "))

# Check divisibility
divisible_by_5 = (number % 5 == 0)
divisible_by_6 = (number % 6 == 0)

# Output results
if divisible_by_5 and divisible_by_6:
    print(f"{number} is divisible by both 5 and 6.")
elif divisible_by_5:
    print(f"{number} is divisible by 5 but not by 6.")
elif divisible_by_6:
    print(f"{number} is divisible by 6 but not by 5.")
else:
    print(f"{number} is not divisible by 5 nor by 6.")
