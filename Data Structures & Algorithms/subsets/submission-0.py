class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at least 1 number in nums
        result = []
        
        subset = []
        def dfs(index):
            # print(f"Inserting index {index}")
            # Every num shall have one layer of node in the tree
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            # The case where this element DOES been included
            subset.append(nums[index])
            dfs(index+1)
            
            # The case where this element DOES NOT been included
            subset.pop(-1)
            dfs(index+1)

        
        dfs(0)
        return result

