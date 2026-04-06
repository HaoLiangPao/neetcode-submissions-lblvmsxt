class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Each element will be used exactly once
        result = []

        def backtrack(candidates, sub_results):
            # Base Case
            if len(candidates) == 0:
                result.append(sub_results)

            # Recurrence
            for i in range(len(candidates)):
                # Create a new array as the python will use the pointer to the array
                tmp_results = sub_results.copy()
                tmp_results.append(candidates[i])
                backtrack(candidates[:i] + candidates[i+1:], tmp_results)
            
            return
        
        backtrack(nums, [])
        return result
