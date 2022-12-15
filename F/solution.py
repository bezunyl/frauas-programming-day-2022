class Part:
    def __init__(self, name, has, wants):
        self.name = name
        self.has = has
        self.wants = wants

people = []

n = int(input())

for i in range(n):
    s = input().split()

    x = Part(s[0], s[1], s[2])

    people.append(x)

maxc = 0

for p in people:
    c = 0
    target = p
    targets = []
    while True:
        inter = list(filter(lambda x: x.has == target.wants and x != target, people))

        if len(inter) == 0:
            break
        else:
            if inter[0] in targets:
                if c > maxc:
                    maxc = c
                break

            targets.append(inter[0])

            c += 1
            target = inter[0]

if maxc > 0:
    print(maxc)
else:
    print("No trades possible")


