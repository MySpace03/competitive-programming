class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        can_max = max(candies)
        ans = []
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= can_max):
                ans.append(True)
            else:
                ans.append(False)
        return ans