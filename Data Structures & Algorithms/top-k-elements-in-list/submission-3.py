class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for i, f in counts.items():
            if f in d:
                if i not in d[f]:
                    d[f].append(i)
            else:
                d[f]=[i]
        x=list(d.keys())
        x.sort()
        for i in range(k):
            if d[x[-1]]==[]:
                x.pop()
            t=d[x[-1]].pop()
            l.append(t)
        return l