lets = input()
letters = [l for l in lets]
words = []

n = int(input())

for i in range(n):
    word = input()
    words.append(word)

for word in words:
    if len(word) >= 4:
        cond = True
        for l in word:
            if not l in letters:
                cond = False
                break
        if not letters[0] in word:
            cond = False

        if cond:
            print(word)


