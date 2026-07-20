class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for n in nums:
            if n not in dup:
                dup.append(n)
            else:
                return True


        return False


x = Solution()
print(x.hasDuplicate([1, 2, 3, 3]))
        