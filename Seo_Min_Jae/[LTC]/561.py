class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i in range(len(nums)):
            if i%2 == 0:
                sum += nums[i]
        
        return sum

# python다운 방식
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])