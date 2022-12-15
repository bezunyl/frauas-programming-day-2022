from sys import stdin

def calcRuneValue(rune):
    res = 0
    for r in rune:
        res += ord(r) - 32

    return res

lines = stdin.readlines()

l1 = input().split()
rune = l1[0]
trans = l1[1]

letters = [chr(a) for a in range(ord("a"), ord("z") + 1)]

offset = letters.index(trans) - calcRuneValue(rune)

for i in range(8):
    l = input()

    if l == "":
        break

    res = ""

    runes = l.split()

    for r in runes:
        if r == "0":
            res += " "
            continue
        elif r == "<":
            res += ","
            continue
        elif r == ">":
            res += "."
            continue

        res += letters[(calcRuneValue(r) + offset) % len(letters)]

    print(res)

