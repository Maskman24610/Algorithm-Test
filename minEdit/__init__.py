# -*- coding: UTF-8 -*- 
#coding = utf-8
print('csie-tw.blogspot.com')
REPLACE = 0
REMOVE = 1
INSERT = 2
def minEditDistance(s1, s2):
    #"""計算s1 -> s2 轉變的最小編輯距離。""
    len1 = len (s1)
    len2 = len (s2)
    
    #建構二維結構，並且讓m[i][j] = 0
    #for i in 0 .. len1 而 for j in 0 .. len2
    m = [None] * (len1+1)
    op = [None] * (len1+1)
    for i in range(len1+1) :
        m[i] = [0] * (len2+1)
        op[i] = [-1] * (len2+1)
    #設置水平行及垂直列的初始成本
    for i in range(1, len1+1):
        m[i][0] = i 
    for j in range(1, len2+1):
       m[0][j] = j     
     
     #最佳運算
    for i in range(1, len1+1) :
        for j in range(1, len2+1) :
            cost = 1
            if s1[i-1] == s2[j-1] : cost = 0;
        
            replaceCost = m[i-1][j-1] + cost  
            removeCost = m[i-1][j] + 1
            insertCost = m[i][j-1] + 1
            costs = [replaceCost, removeCost, insertCost]
            m[i][j] = min(costs)
            op[i][j] = costs.index(m[i][j] )
    
    ops = []
    i = len1
    j = len2
    while i != 0 or j != 0:
        if op[i][j] == REMOVE or j==0:
            ops.append('remove {}-th char {} of  {}'.format(i,s1[i-1],s1))
            i = i-1
        elif op[i][j] == INSERT or i ==0:
            ops.append('insert {}-th char {} of  {}'.format(j,s2[j-1],s2))
            j = j-1
        else:
            if m[i-1][j-1] < m[i][j]:
                fmt = 'replace {}-th char of {} ({}) with {}' 
                ops.append(fmt.format(i, s1, s1[i-1], s2[j-1]))
            i, j = i-1, j-1
                
    return m[len1][len2],ops

print(minEditDistance('GCTAC', 'CTCA'),"is minimum distance")