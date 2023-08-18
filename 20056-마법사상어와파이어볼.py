import sys
input = sys.stdin.readline

N,M,K = map(int,input().split(' '))

ground = [[[] for _ in range(N)] for _ in range(N)]

fireballs = []
operator = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]

# r(Y) c(X) m(질량) s(속력) d(방향)
for i in range(M):
    fireballs.append(list(map(int, input().split(' '))))

for i in range(K):
    ground = [[[] for _ in range(N)] for _ in range(N)]
    for idx, fireball in enumerate(fireballs):
        r, c, m, s, d = fireball
        fireballs[idx][0] = (r-1+operator[d][1]*s)%N
        fireballs[idx][1] = (c-1+operator[d][0]*s)%N

        ground[fireballs[idx][0]][fireballs[idx][1]].append((m,s,d))
        
    fireballs.clear()
    for idx1 in range(N):
        for idx2 in range(N):
            fireball_arr = ground[idx1][idx2]
            ball_num = len(fireball_arr)
            
            if ball_num == 1:
                fireballs.append([idx1+1,idx2+1,fireball_arr[0][0],fireball_arr[0][1],fireball_arr[0][2]])
                continue

            m_sum = 0
            s_sum = 0
            d_o = 0
            d_e = 0
            for fb in fireball_arr:
                m,s,d = fb
                m_sum += m
                s_sum += s
                if d%2 == 0:
                    d_e += 1
                else:
                    d_o += 1
            if ball_num == 0 or m_sum//5 ==0:
                continue
            
            else:
                for j in range(4):
                    if d_e == 0 or d_o == 0:
                        fireballs.append([idx1+1,idx2+1,m_sum//5,s_sum//ball_num,j*2])
                    else:
                        fireballs.append([idx1+1,idx2+1,m_sum//5,s_sum//ball_num,j*2 + 1])
    
    # for g in ground:
    #     print(*g)
    # print(fireballs)

total_sum = 0
for fb in fireballs:
    total_sum+=fb[2]

print(total_sum)

    