class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Substring (results have to be consecutive) 
        # All possible substring -> Backtrack

        N = len(s)

        # # Use DP to record the palindrom status for faster backtracking
        # T = [[False for _ in range(N)] for _ in range(N)]

        # # Recurrence
        # for i in range(N):
        #     for j in range(N):
        #         # Base Case
        #         if i == j:
        #             T[i][j] = True
        #         # T[i][j] = 1) item i == item j T[i+1][j-1] 2) item i != item j False
        #         if j-1 >= i+1 and s[i] == s[j]:
        #             T[i][j] = T[i+1][j-1]
        
        # # Print out the table
        # for i in range(N):
        #     print(T[i])

        def backtrack(path, start):
            # Found a successfully splitted palindrome partition
            if start == N:
                results.append(path[:])
                return
            for end in range(start, N):
                # If find a palindrome
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(path, end + 1)
                    path.pop()
        
        results = []
        path = []
        backtrack(path, 0)

        return results