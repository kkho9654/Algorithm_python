import sys

N, K = list(map(int, sys.stdin.readline().split(' ')))

temp = []
accum = []
accum.append(0)
inp = list(map(int, sys.stdin.readline().split(' ')))

for idx, t in enumerate(inp):
    temp.append(t)
    if idx>0:
        accum.append(accum[idx]+t)
    else:
        accum.append(t)

maxt = -10000000

if K == N:
    maxt = accum[N]
elif K==1:
    maxt = max(temp)
else:
    for i in range(N -K+1):
        ttmp = accum[i+K] - accum[i]
        maxt = max(ttmp,maxt)

# print(accum)
print(maxt)