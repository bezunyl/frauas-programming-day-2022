import math

s = input().split()

h = int(s[0])
a = int(s[1])

if a >= 0 and a <= 180:
    print("safe")
else:
    angle = a

    if a > 180 and a < 270:
        angle = 270 + (270 - angle)

    angle = angle - 270

    print(math.floor(h / (math.cos(math.radians(angle)))))

