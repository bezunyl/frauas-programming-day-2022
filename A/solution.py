n = input()
ls = input()

cups = 0
count = 0

for i in ls:
    if i == "1":
        cups = 2
        count += 1

    if i == "0":
        if cups > 0:
            count += 1
            cups -= 1

print(count)
