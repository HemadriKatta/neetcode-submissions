class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = defaultdict(int)
        for i in nums:
            freqDict[i] +=1
        
        sorted_dict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_dict.keys())[:k]


        