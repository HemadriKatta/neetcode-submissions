class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = defaultdict(list)
        for i in strs:
            res = "".join(sorted(i))
            temp[res].append(i)

        return temp.values()  

        