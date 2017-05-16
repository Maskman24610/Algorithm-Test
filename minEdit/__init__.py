# -*- coding: UTF-8 -*- 
#coding = utf-8
#print('csie-tw.blogspot.com')
from msilib.schema import ReserveCost
def minEditDistance(s1, s2):
    #"""計算s1 -> s2 轉變的最小編輯距離。""
    len1 = len (s1)
    len2 = len (s2)
    
    #建構二維結構，並且讓m[i][j] = 0
    #for i in 0 .. len1 而 for j in 0 .. len2
    m = [None] * (len1+1)
    for i in range(len1+1) :
        m[i] = [0] * (len2+1)
        
    #設置水平行及垂直列的初始成本
    for i in range(1, len1+1):
        m[i][0] = i 
    for j in range(1,len2+1):
       m[0][j] = j     
     
     #最佳運算
    for i in range(1, len1+1) :
        for j in range(1,len2+1) :
             cost = 1
        if s1[i-1] == s2[j-1] : cost = 0;
        
        replaceCost = m[i-1][j-1] + cost  
        removeCost = m[i-1][j] + 1
        insertCost = m[i][j-1] + 1
        m[i][j] = min(replaceCost, removeCost, insertCost)
        
    return m[len1][len2]

print(minEditDistance("ABCD", "A"))