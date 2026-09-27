class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        x=1
        i,j=0,1
        d={s[0]:0}
        while j<len(s):
            if s[j] in d and i<=d[s[j]]:
                i=d[s[j]]+1
            d[s[j]]=j
            x=max(x,j-i+1)
            j+=1
        return x

    