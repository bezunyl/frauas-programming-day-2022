houseid = 1

def getCoordsOfChar(tiles, char):
    for i, ts in enumerate(tiles):
        if char in ts:
            return (i, ts.index(char))

def startVelocity(tiles, ci):
    if ci[0] == 0:
        return (1, 0)
    elif ci[0] == len(tiles) - 1:
        return (-1, 0)
    elif ci[1] == 0:
        return (0, 1)
    elif ci[1] == len(tiles[0]) - 1:
        return (0, -1)

def addTup(a, b):
    return(a[0] + b[0], a[1] + b[1])

def reverseTup(a):
    return (a[1], a[0])

def inverseTup(a):
    return (a[0] * -1, a[1] * -1)

def directionChange(tiles, pos, v):
    if tiles[pos[0]][pos[1]] == "\\":
        return reverseTup(v)
    
    if tiles[pos[0]][pos[1]] == "/":
        return inverseTup(reverseTup(v))

    else:
        return v

def printMap(tiles):
    for ts in tiles:
        print("".join(ts))

while True:
    l = input()

    if (l == "0 0"):
        break

    s = l.split()

    w = int(s[0])
    h = int(s[1])

    tiles = []
    
    for i in range(h):
        ts = input()
        tiles.append([t for t in ts])

    entry = getCoordsOfChar(tiles, "*")
    v = startVelocity(tiles, entry)
    pos = addTup(entry, v) 

    while True:
        if tiles[pos[0]][pos[1]] == "x":
            tiles[pos[0]][pos[1]] = "&"
            break

        v = directionChange(tiles, pos, v)
        pos = addTup(pos, v)

    print("HOUSE %d"%(houseid))
    printMap(tiles)

    houseid += 1

