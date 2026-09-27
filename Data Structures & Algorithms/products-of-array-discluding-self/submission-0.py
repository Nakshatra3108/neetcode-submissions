class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,pre,suf=[],[],[]
        p,s=1,1
        pre.append(p)
        suf.append(s)
        for i in range(len(nums)-1):
            p*=nums[i]
            pre.append(p)
        
            s*=nums[(i+1)*-1]
            suf.append(s)
        for j in range(len(pre)):
            res.append(pre[j]*suf[(j+1)*-1])
        return res
