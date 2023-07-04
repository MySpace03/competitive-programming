class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        nums.sort()
        maxi = 1
        cur_max = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                cur_max += 1
            else:
                cur_max = 1
            maxi = max(maxi, cur_max)
        return maxi