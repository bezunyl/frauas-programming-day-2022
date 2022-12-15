n = int(input())

count = 0

for i in range(n):
    col = input().lower()

    if "pink" in col or "rose" in col:
        count += 1

if count == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)
