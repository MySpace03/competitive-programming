class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = dict()
        n = len(nums)//3
        ans = []
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for i in nums:
            if d[i]>n and i not in ans:
                ans.append(i)
        return ans