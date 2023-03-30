
def shuffle(card_num, shuffle_num,p,d):
    # d = (p의 인덱스(d의 벨류), d의 인덱스(p의 순서))
    # 원래 순서 p의 순서 => d의 value => d의 순서 =>p의 순서
    # 역방향 순서 p의 순서 => d의 순서 => d의 value => p의 순서
    # 즉 p와 같은 인덱스를 가지는 d의 벨류값이 원래 p의 순서
    if shuffle_num == 0:
        return p

    for i in range(card_num):
        tmp = p[i+1]
        p[d[i+1]] = tmp
# p[d[i]] = s
# d_ = d[d[i]]
    return shuffle(card_num,shuffle_num,p,d)

if __name__ == '__main__':
    card_num = int(input())
    shuffle_num = int(input())

    p = dict()
    for i in range(card_num):
        p[i+1] = int(input())

    d = dict()
    for i in range(card_num):
        d[i+1] = int(input())

    p = shuffle(card_num,shuffle_num,p,d)

    str = ''
    for i in range(card_num):
        if i != card_num-1:
            str += p[i]+' '
        else:
            str += p[i]
    print(str)
    