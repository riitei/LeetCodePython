class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j] == target):
                    return [i, j]
                    break


ans = Solution()
ans = ans.twoSum([0, 2, 7, 11, 15], 9)
print(ans)
