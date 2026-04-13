class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0]) # In the requirement, the board length is always positive
        W = len(word)

        # Avoid duplicate position
        path = set()

        # DFS (backtrack)
        def dfs(row: int, col: int, word_index: str) -> bool:
            # The entire word has been found
            if word_index == W:
                return True
            
            if ((row >= N or row < 0) or # board size requirement
                (col >= M or col < 0) or
                ((row, col) in path) or # Make sure each char been used once
                (board[row][col] != word[word_index]) # compare the first char
                ):
                return False

            path.add((row, col))
            result = (dfs(row+1, col, word_index+1) or dfs(row-1, col, word_index+1)
                    or dfs(row, col+1, word_index+1) or dfs(row, col-1, word_index+1))
            path.remove((row, col))
            return result


        for i in range(N):
            for j in range(M):
                # One possible solution will satisfy the requirement
                if dfs(i, j, 0):
                    return True
        
        return False