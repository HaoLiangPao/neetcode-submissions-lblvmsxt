class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, path):
            if left == 0 and right == 0:
                result.append(path)
                return

            if left > 0:
                backtrack(left-1, right, f"{path}(")
            if right > left:
                backtrack(left, right-1, f"{path})")

        backtrack(n,n,"")
        return result