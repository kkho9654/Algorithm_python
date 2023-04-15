import sys, copy
from collections import deque

# DFS는 스택 - first in last out
# BFS는 큐 

class Graph:
    def __init__(self):
        self.NextNode = []
        self.Node = {}
        self.stack = []
        self.queue = deque([])
        self.pastPath = set()
        self.dfsArr = []
        self.bfsArr = []
        self.count = 0

    def addNextNode(self,currentNode, nextNode):
        try:
            tmp = self.Node[currentNode]
        except:
            self.Node[currentNode] = []
        try:
            tmp = self.Node[nextNode]
        except:
            self.Node[nextNode] = []
        self.Node[currentNode].append(nextNode)
        self.Node[nextNode].append(currentNode)

    def dfs(self,currentNode):
        try:
            self.Node[currentNode]
        except:
            self.dfsArr.append(currentNode)
            return
        if currentNode in self.pastPath:
            try:
                self.dfs(self.stack.pop())
            except:
                pass
            return
        self.pastPath.add(currentNode)
        self.dfsArr.append(currentNode)
        tmp = copy.deepcopy(self.Node[currentNode])
        tmp.sort(reverse=True)
        for t in tmp:
            self.stack.append(t)
        try:
            self.dfs(self.stack.pop())
        except:
            return

    def bfs(self,currentNode):
        try:
            self.Node[currentNode]
        except:
            self.bfsArr.append(currentNode)
            return
        
        while True:
            if currentNode in self.pastPath:
                try:
                    currentNode = self.queue.popleft()
                except:
                    return
                continue
            
            self.pastPath.add(currentNode)
            self.bfsArr.append(currentNode)
            self.count += 1
            tmp = copy.deepcopy(self.Node[currentNode])
            tmp.sort()
            
            for t in tmp:
                self.queue.append(t)

            currentNode = self.queue.popleft()

    def print(self):
        # print(*self.dfsArr)
        # print(len(self.dfsArr)-1)
        # print(*self.bfsArr)
        print(len(self.bfsArr)-1)

if __name__ == '__main__':
    sys.stdin.readline()
    # input = list(map(int,sys.stdin.readline().split(' ')))
    graph = Graph()

    for i in range(int(sys.stdin.readline())):
        path = list(map(int,sys.stdin.readline().split(' ')))
        graph.addNextNode(path[0],path[1])
    # graph.dfs(1)
    # graph.pastPath.clear()
    # graph.num = 0
    graph.bfs(1)
    graph.print()


