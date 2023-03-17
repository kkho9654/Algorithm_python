# 세로 2n-1
# 가로 4n-3
# 가로 공백 2n-3

#별이 n-1번 연속으로나오면 
# 대조군 2개

def star(n):
    x=''
    y=''
    blank = []
    for i in range(2*n-3):
        blank.append(' ')
    for i in range(n):
        x += '*'
        if i == 0 or i==n-1:
            y+='*'
        else:
            y+=' '
    flag = 0
    first_blank = []
    last_blank = []
    for i in range(2*n-1):
        if i==0 or i==2*n-2:
            tmp = ''.join(blank)
            print(f'{x}{tmp}{x}')
        else:
            row = ''
            if flag == 0:
                if len(blank)==1:
                    flag = 1
                    first_blank.append(' ')
                    last_blank.append(' ')
                    row += str(''.join(first_blank) + y + y + ''.join(last_blank)).replace('**','*')
                else:
                    first_blank.append(blank.pop())
                    last_blank.append(blank.pop())
                    row += ''.join(first_blank) + y + ''.join(blank) + y # + ''.join(last_blank)
                print(row)
            else:
                first_blank.pop()
                last_blank.pop()
                row += ''.join(first_blank) + y + ''.join(blank) + y # + ''.join(last_blank)
                blank.append(' ')
                blank.append(' ')
                print(row)

if __name__ == '__main__':
    star(int(input()))