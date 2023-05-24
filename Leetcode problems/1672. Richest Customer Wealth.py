class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = sum(accounts[0])
        for i in accounts:
            m = max(sum(i),m)
        return m