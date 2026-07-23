from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostfreq = Counter(nums)
        res =sorted(mostfreq, key=mostfreq.get, reverse=True)
        return res[:k]
    


        