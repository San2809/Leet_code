        if not board:
            return False
        N,M=len(board),len(board[0])
        stack=[]
        for i in range(N):
            for j in range(M):
                if board[i][j]==word[0]:
                    stack.append((i,j,0,{(i,j)}))
        while stack:
            i,j,step,visit=stack.pop()
            step+=1
            if step==len(word):
                return True
            for (ni,nj) in [(i+x,j+y) for x,y in [(1,0),(-1,0),(0,1),(0,-1)]]:
                if (ni,nj) not in visit and 0<=ni<N and 0<=nj<M and board[ni][nj] == word[step]:
                    stack.append((ni,nj,step,visit.union({(ni,nj)})))
        return False
