Kion = [0,4,32,17,12,23]
n = len(Kion) - 1

for g in range(1, n, 1):
    Hoz = g
    for j in range(g+1, n+1, 1):
        if Kion[j] < Kion[Hoz]:
            Hoz = j
    if Hoz != g:
        Kion[0] = Kion[g]
        Kion[g] = Kion[Hoz]
        Kion[Hoz] = Kion[0]

for k in range(1, n+1, 1):
    print(Kion[k])