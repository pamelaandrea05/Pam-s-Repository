def convertTo_usd(money_amount):
    
    # conversion rates
    usdTOinr = 87.99     # 1 USD = 87.99 INR
    usdTOgbp = 0.74      # 1 USD = 0.74 GBP
    usdTOcny = 7.18      # 1 USD = 7.18 CNY

    rupee = money_amount * usdTOinr
    pound = money_amount * usdTOgbp
    yuan  = money_amount * usdTOcny

    return rupee, pound, yuan

def main():
    while True:
        money = input("Enter dollar amount (or press * to exit): ").strip()
        if money == "*":
            print("Bye")
            break

        parts = money.split("@")
        lst_dollar = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            try:
                # allow decimals
                value = float(p)
                lst_dollar.append(value)
            except ValueError:
                print(f"Invalid: '{p}'")
        
        if not lst_dollar:
            print("No valid amounts. Please provide an amount.")
            continue

        # Print conversion
        for usd in lst_dollar:
            rupee, pound, yuan = convertTo_usd(usd)
        print(f"{'Dollar ($)':<15}{usd:<15.2f}")#{usd:<15.2f} Format numbers nicely, maybe 2 decimal places
        print(f"{'Indian Rupee (R)':<20}{rupee:<20.2f}")#{rupee:<20.2f} Format numbers nicely, maybe 2 decimal places
        print(f"{'British (Pound)':<20}{pound:<20.2f}")#{pound:<20.2f} Format numbers nicely, maybe 2 decimal places
        print(f"{'China (Y)':<15}{yuan:<15.2f}")#{yuan:<15.2f} Format numbers nicely, maybe 2 decimal places
        
            
if __name__ == "__main__":
    main()
