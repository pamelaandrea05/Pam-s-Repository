def main():
    cart = {}

    try:
        size = int(input("Matrix size: "))
    except ValueError:
        print("Invalid input. Exiting.")
        return

    for i in range(size):
        item = input(f"Shopping item/s {i + 1}: ")
        cart[i] = item

    print(f"\nYou have {len(cart)} item/s in the cart.\n")

    while True:
        choice = input("What would you like to do [C]hange items [R]emove [D]isplay  [S]earch [*]Exit? ").strip().lower()

        if choice == 'c':
            k_input = input("\nEnter key to search [0]1 [1]2 [2]3: ").strip()
            if not k_input.isdigit():
                print("Im sorry, not in the cart\n")
                continue

            key = int(k_input)
            value = cart.get(key)
            if value is not None:
                print(f"Found {value} item.")
                new_val = input("Enter value: ")
                cart[key] = new_val
                print()
            else:
                print("Im sorry, not in the cart\n")

        elif choice == 'r':
            k_input = input("\nEnter key to search [0]1 [1]2 [2]3: ").strip()
            if not k_input.isdigit():
                print("Key not found\n")
                continue

            key = int(k_input)
            value = cart.get(key)
            if value is not None:
                print(f"The key {key} with value {value} has been deleted\n")
                del cart[key]
            else:
                print("Key not found\n")

        elif choice == 's':
            search = input("\nEnter item to search: ").strip()
            found = False
            for val in cart.values():
                if val.lower() == search.lower():
                    print(f"Found {search} item\n")
                    found = True
                    break
            if not found:
                print("Im sorry, item is not in the cart\n")

        elif choice == 'd':
            print("\nDisplaying Values")
            print(f"{'Value':<10}{'Key'}")
            for key, value in cart.items():
                print(f"{value:<10}{key}")
            print()

        elif choice == '*':
            print("Bye")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
