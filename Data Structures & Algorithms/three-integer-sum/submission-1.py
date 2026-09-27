class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        temp=[]
        nums.sort()
        for i in nums:
            temp=nums.copy()
            temp.remove(i)
            pairs= self.findTriplets(temp,-1*i)
            if pairs==[]:
                continue
            else:
                for x,y in pairs:
                    l2=[x,y,i]
                    l2.sort()
                    if l2 not in l:
                        l.append(l2)
        return l
            
    def findTriplets(self,numbers,target):
        i,j=0,len(numbers)-1
        pairs = []
        while i < j:
                if numbers[i] + numbers[j] < target:
                    i += 1
                elif numbers[i] + numbers[j] > target:
                    j -= 1
                else:
                    pairs.append([numbers[i], numbers[j]])
                    i += 1
                    j -= 1
        return pairs
        