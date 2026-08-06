class Solution:
    def jump(self, nums: List[int]) -> int:
        
        result = 0
        l, r = 0, 0

        while r < len(nums)-1:
            highest = 0
            for i in range(l, r+1):
                highest = max(highest, i+nums[i])
            l = r+1
            r = highest
            result = result + 1
        return result