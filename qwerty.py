from heapq import *
import math

n, m = map(int, input().split())

biba = []
for i in range(n):
    biba.append(-1)
boba = []

for i in range(n):
    boba.append([])

lolik = [(0, 0)]

bolik = [0]
buffer = []
for i in range(n):
    buffer.append(math.inf)

bolik.extend(buffer)

for i in range(m):
    buffer = input().split()
    for j in range(len(buffer)):
        buffer[j] = int(buffer[j])

    boba[buffer[1] - 1] = boba[buffer[1] - 1] + [(buffer[2], buffer[0] - 1)]
    boba[buffer[0] - 1] = boba[buffer[0] - 1] + [(buffer[2], buffer[1] - 1)]

while lolik:
    qwerty = heappop(lolik)[1]
    for pica in boba[qwerty]:
        don = pica[1]
        asshole = bolik[qwerty] + pica[0]
        if asshole >= bolik[don]:
            continue
        else:
            bolik[don] = asshole
            biba[don] = qwerty
            heappush(lolik, (bolik[don], don))

if bolik[n - 1] != math.inf:
    zebra = []
    ananas = n - 1
    while True:
        if ananas == -1:
            break
        zebra = zebra + [ananas + 1]
        ananas = biba[ananas]

    print(' '.join(map(str, reversed(zebra))))
else:
    print(-1)