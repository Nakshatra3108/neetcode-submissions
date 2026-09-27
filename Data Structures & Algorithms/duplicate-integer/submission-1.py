class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l= len(nums)
        nums=set(nums)
        return not len(nums)==l