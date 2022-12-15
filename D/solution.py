def waterreq(order):
    if len(order) == 1:
        return int(order)
    else:
        return int(order[0]) + 1

l1 = input().split()
n = int(l1[0])
s = int(l1[1])

tank = s
count = 0

for i in range(n):
    l = input()

    if (tank - waterreq(l) < 0):
        tank = s - waterreq(l)
        count += 1
    else:
        tank -= waterreq(l)

print(count)
