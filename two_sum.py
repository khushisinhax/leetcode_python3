class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

""1.Create an empty dictionary num_dict to store the numbers and their indices.
2.iterate through the nums array.
3.For each number,  calculate the complement, which is the number that needs to be added to the current number to get the target.
4.check if the complement is already in the num_dict. If it is,  return the indices of the two numbers that add up to the target.
5the complement is not in the num_dict, add the current number and its index to the dictionary.""

