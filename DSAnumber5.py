# CATABAY, LEILA KATRINA

def main():
    print("input: ")
    T = int(input())
    for test in range(T):
        n_k = input().split()
        n = int(n_k[0])
        k = int(n_k[1])
        total_games = n * (n - 1) // 2

        found = False
        points_list = []

        if n <= 10:
            
            def dfs(idx, left, arr):
                nonlocal found, points_list
                if found:
                    return
                if idx == n:
                    if left == 0:
                        total = sum(x * x for x in arr)
                        if total == k:
                            found = True
                            points_list = arr[:]
                    return

                for win in range(min(left, n - 1), -1, -1):
                    arr.append(win)
                    dfs(idx + 1, left - win, arr)
                    arr.pop()

            dfs(0, total_games, [])
        else:
            
            arr = [0] * n
            left = total_games
            for i in range(n):
                give = min(left, n - 1)
                arr[i] = give
                left -= give
            total = sum(x * x for x in arr)
            if total == k:
                found = True
                points_list = arr[:]

        if not found:
            print("-1")
        else:
            # Build win matrix
            wins = [0] * n
            for i in range(n):
                wins[i] = points_list[i]

            mat = []
            
            for i in range(n):
                row = []
                for j in range(n):
                    if i == j:
                        row.append("0")
                    else:
                        if wins[i] > 0:
                            row.append("1")
                            wins[i] -= 1
                        else:
                            row.append("0")
                mat.append("".join(row))
            for row in mat:
                print(row)

if __name__ == "__main__":
    main()