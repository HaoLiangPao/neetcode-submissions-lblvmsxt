class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        substraction_mapping = {}
        for index, num in enumerate(nums):
            # Check previous records
            if num in substraction_mapping:
                return sorted([index, substraction_mapping[num]])
            # Enter new records
            substracted = target - num
            if substracted not in substraction_mapping:
                substraction_mapping[substracted] = index
        # (if not returned) Than, the last element is been used
        return sorted([len(nums)-1, substraction_mapping[target-nums[-1]]])