class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combs = [[] for i in range(n+1)]
        for i in range(0, n+1):
            # Base Case
            if i == 0:
                combs[i] += [""]
            # Recurrence
            else:
                temp_combs = set()
                # Not only check the i-1, check all 
                for j in range(i):
                    for left in combs[j]:
                        for right in combs[i - 1 - j]:
                            combs[i].append(f"({left}){right}")
        return combs[n]

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # dp[i] stores a list of all valid combinations for i pairs
#         dp = [[] for _ in range(n + 1)]
#         dp[0] = [""]  # Base case: zero pairs is an empty string

#         for i in range(1, n + 1):
#             for j in range(i):
#                 # j pairs inside the first bracket, i-1-j pairs outside
#                 # Pattern: "(" + [left_part] + ")" + [right_part]
#                 for left in dp[j]:
#                     for right in dp[i - 1 - j]:
#                         dp[i].append(f"({left}){right}")
        
#         return dp[n]