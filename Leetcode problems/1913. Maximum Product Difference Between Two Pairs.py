class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        ans = (nums[l-1]*nums[l-2]) - (nums[0]*nums[1])
        return ans