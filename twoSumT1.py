class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(i,j)
                if nums[i] + nums[j] == target:
                    ret = [i,j]
                    return ret


nums = [3,2,4]
solution = Solution()
print(solution.twoSum(nums,6))
