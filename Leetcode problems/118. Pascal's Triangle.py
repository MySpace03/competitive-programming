class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows > 1:
            pascal = [[1], [1,1]]
            n = 1
            while n < numRows - 1:
                i = 0
                tri =[1]
                while i+1 != len(pascal[n]):
                    tri.append(pascal[n][i] + pascal[n][i+1])
                    i+=1
                tri.append(1)
                pascal.append(tri)
                n+=1
            return pascal
        else:
            if numRows == 1:
                return [[1]]