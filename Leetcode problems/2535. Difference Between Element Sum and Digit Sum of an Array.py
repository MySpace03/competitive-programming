class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele = 0
        digi = 0
        for i in range(len(nums)):
            ele += nums[i]
            n = nums[i]
            while(n>0):
                temp = n%10
                n = n//10
                digi += temp
        return abs(ele-digi)