import sys, collections
input = sys.stdin.readline

N = int(input())
voca = []
for _ in range(N):
    k = list(input().strip())
    voca.append(collections.deque(k))

score_dict = collections.defaultdict(int)
alphabet_dict = {}

for idx, v in enumerate(voca) :
    score = 1
    for a in reversed(v):
        score_dict[a] += score
        score *= 10
k = sorted(score_dict.items(), key=lambda x:x[1])
num = 9
while k:
    alphabet,_ = k.pop()
    alphabet_dict[alphabet] = str(num)
    num -= 1

total = 0
for idx, v in enumerate(voca):
    v_num = ''
    for a in v:
        v_num += alphabet_dict[a]
    total+=int(v_num)
print(total)