class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            # Base Case
            result.append(path.copy())

            # Recurrence
            for i in range(index, len(nums)):
                # 1) include the element
                path.append(nums[i])
                backtrack(i+1, path)

                # 2) not include the element
                path.pop()

        backtrack(0, [])
        return result