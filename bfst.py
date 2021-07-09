def bfs(self):
   
    que.append(self.left)
    self.left.bfs()
    que.append(self.right)
    self.right.bfs()

que = []