import math

def realArea(rad):
    return math.pi * rad ** 2

def approxArea(r, pm, pin):
    return (pin / pm) * ((r * 2) ** 2)

def compute(r, m, c):
    print("%f %f"%(realArea(float(r)), approxArea(float(r), int(m), int(c))))

while True:
    l = input()

    if l == "0 0 0":
        break

    s = l.split()
    compute(s[0], s[1], s[2])


