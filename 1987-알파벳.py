import sys
input = sys.stdin.readline

R,C = map(int, input().strip().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))
global mx
mx = 0
def bt(depth,cur_r,cur_c, alphabet):
    global mx

    directions = [[cur_r-1, cur_c], [cur_r+1, cur_c], [cur_r, cur_c-1], [cur_r, cur_c+1]]
    alphabet[ord(board[cur_r][cur_c]) - ord('A')] = True

    mx = max(depth,mx)
    
    for direction in directions:
        next_r = direction[0]
        next_c = direction[1]
        if next_r >=0 and next_r <R and next_c >=0 and next_c <C:
            n = ord(board[next_r][next_c]) - ord('A')
            if alphabet[n]:
                continue
            bt(depth+1, next_r, next_c,alphabet)
            alphabet[n] = False
    
bt(0,0,0,[False] * 30)

print(mx+1)