n = int(input())
cond = False

for i in range(n):
    c = int(input())
    name = input()
    food = []

    for j in range(c):
        f = input()
        food.append(f)

    if ("pea soup" in food) and ("pancakes" in food):
        print(name)
        cond = True
        break

if cond == False:
    print("Anywhere is fine I guess")
