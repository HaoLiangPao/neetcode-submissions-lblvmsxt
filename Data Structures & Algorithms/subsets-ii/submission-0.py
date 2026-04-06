class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Sort the list so duplication is easier to be found
        nums.sort()

        def backtrack(index, path):
            # Base Case
            result.append(path.copy())

            # Recurrence
            for i in range(index, len(nums)):
                # Skip the element if it is duplicated
                # Because it is checking within the subproblem so duplicates values but unique element combs like [1, 1] will be kept 
                if i > index and nums[i-1] == nums[i]:
                    continue
                
                # 1) include the element
                path.append(nums[i])
                backtrack(i+1, path)

                # 2) not include the element
                path.pop()

        backtrack(0, [])
        return result