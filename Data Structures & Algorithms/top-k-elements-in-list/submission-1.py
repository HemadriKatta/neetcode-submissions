class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)
        for n in nums:
            temp[n] += 1
        
        sortedDict = dict(sorted(temp.items(), key=lambda item:item[1], reverse=True))
        return list(sortedDict.keys())[:k]