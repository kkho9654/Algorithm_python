import sys
input = sys.stdin.readline


class Magic:
    def __init__(self):
        self.N, self.M = map(int, input().split(' '))
        self.ground = [list(map(int, input().split(' '))) for _ in range(self.N)]
        self.operator = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
        self.clouds = [(0,self.N-1),(1,self.N-1),(0,self.N-2),(1,self.N-2)]

    def move_cloud(self,d,s):
        x, y = self.operator[d-1]
        x *= s
        y *= s
        tmp = []
        while self.clouds:
            cloud_x, cloud_y = self.clouds.pop()
            tmp.append(((cloud_x+x)%self.N, (cloud_y+y)%self.N))
        self.clouds = tmp


    def rain(self):
        for cloud in self.clouds:
            cloud_x, cloud_y = cloud
            self.ground[cloud_y][cloud_x] += 1
        
    def remove_cloud(self):
        self.clouds.clear()

    def copy_water(self):
        arr = [1,-1]
        for cloud in self.clouds:
            cloud_x, cloud_y = cloud
            count = 0
            
            for i in arr:
                for j in arr:
                    if cloud_x+i>=0 and cloud_x+i < self.N and cloud_y+j>=0 and cloud_y+j < self.N \
                        and self.ground[cloud_y+j][cloud_x+i]>0:
                        count+=1
            self.ground[cloud_y][cloud_x] += count
            
            
    def create_clooud(self):
        tmp = []
        for i in range(self.N):
            for j in range(self.N):
                if self.ground[i][j]>=2:
                    if (j,i) not in self.clouds:
                        self.ground[i][j] -= 2
                        tmp.append((j,i))
        self.clouds = tmp
    def sum_waters(self):
        ret = 0
        for g in self.ground:
            ret += sum(g)
        return ret
    def printc(self):
        for g in self.ground:
            print(*g)
shark = Magic()
for i in range(shark.M):
    d, s = map(int,input().split(' '))
    shark.move_cloud(d,s)
    shark.rain()
    shark.copy_water()
    shark.create_clooud()
print(shark.sum_waters())
# shark.printc()


