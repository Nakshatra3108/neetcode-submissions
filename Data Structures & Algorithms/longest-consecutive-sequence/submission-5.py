class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        c=0
        for i in nums:
            d[i]=i+1
        x=list(d.keys())
        e=None
        m=c
        
        for i in d:
            if i-1 not in d:
                e=i
                c=1
                while e+1 in d:
                    e=e+1
                    c=c+1
                m=max(c,m)
        return m

