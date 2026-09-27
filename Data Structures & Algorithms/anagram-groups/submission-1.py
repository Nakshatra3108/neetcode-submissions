class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        if len(strs)==1:
            l.append([strs[0]])
            return l

        d={}
        for i in strs:
            temp=[0]*26
            for j in i:
                temp[ord(j)-97]=i.count(j)
            s=str(temp)
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        
        for i in d.values():
            l.append(i)
        return l