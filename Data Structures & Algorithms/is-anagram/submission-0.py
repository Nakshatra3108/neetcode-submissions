class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1,d2={},{}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for j in t:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
        for e in d1:
            if e not in d2:
                return False
            elif d1[e]!=d2[e]:
                return False
        return True
        