class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('infinity')

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2

            res = min(res, nums[m])

            # if nums[l] <= nums[m]:
            #     if nums[r] >= nums[m]:
            #         r = m - 1
            #     else:
            #         l = m + 1
            # else:
            #     if nums[r] <= nums[m]:
            #         l = m + 1
            #     else:
            #         r = m - 1
            if nums[r] >= nums[m]:
                r = m -1 
            else:
                l = m + 1

        return res
