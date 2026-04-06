class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # As we need the whole combination, we will use backtrack instead of dynamic programming
        result = []

        # If we sort the candidates, we can early stop, could be an improvement in some way, not necessary to solve the problem
        candidates.sort()

        def backtrack(remaining, start_index, combs):
            # Base Case
            if remaining == 0:
                result.append(combs)
                return
            
            # Go through each number in the candidate:
            for i in range(start_index, len(candidates)):
                current_num = candidates[i]

                # If candidates are sorted, then we can early stop
                if current_num > remaining:
                    break

                # If duplicate values appeared
                if i > start_index and candidates[i-1] == candidates[i]:
                    continue

                backtrack(remaining - current_num, i+1, combs + [current_num])
        
        backtrack(target, 0, [])
        return result