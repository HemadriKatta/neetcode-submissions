class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in temp:
                return [temp[diff]+1, i+1]
            temp[numbers[i]] = i
        


        