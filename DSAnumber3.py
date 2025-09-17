#CATABAY, LEILA KATRINA
def parse_row_input(row_input):
    
    parts = row_input.strip().split()
    if len(parts) == 1:
        
        if parts[0].isdigit() and len(parts[0]) > 1:
            
            return [int(ch) for ch in parts[0]]
        else:
            
            return [int(parts[0])]
    else:
        
        return [int(p) for p in parts]

def main():
    
    while True:
        rows = int(input("Enter the number of rows: "))
        if rows >= 3 and rows <= 100:
            break
        print("Please enter number between 3-100")

   
    while True:
        cols = int(input("Enter the number of columns: "))
        if cols >= 3 and cols <= 100:
            break
        print("Please enter a number between 3-100")

    matrix = []
    for i in range(1, rows + 1):
        while True:
            row_input = input(f"Row #{i}  ")
            row = parse_row_input(row_input)
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"Please enter exactly {cols} numbers.")

    print()  

 
    rotated = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            
            new_row.append(matrix[r][cols - 1 - c])
        rotated.append(new_row)

    
    print()
    for row in rotated:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    main()