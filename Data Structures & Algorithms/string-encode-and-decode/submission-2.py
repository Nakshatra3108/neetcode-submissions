class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            l=len(i)
            s+=str(l)+'#'+i
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        n=''
        p=False
        while i<len(s):
            if s[i].isdigit():
                if s[i+1]=='#' or s[i+2]=='#' or s[i+3]=='#':
                    n+=s[i]
                    p=True
            elif s[i]=='#' and p:
                p=False
                n=int(n)
                l.append(s[i+1:i+n+1])
                i+=n
                n=''
                

            i+=1
        return l
