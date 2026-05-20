class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []

        for i in range(n) :
            count = 0

            for num in range(1, n+1):
                if num in A[:i+1] and num in B[:i+1] :
                    count +=1

            ans.append(count)
        return ans
        