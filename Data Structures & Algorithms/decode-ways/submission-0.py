class Solution:
    def numDecodings(self, s: str) -> int:

        # Base Case
        T = [0 for _ in range(len(s))]
        n = len(s)

        # Recurrance
        # T(i) = T(i-1) + 1 (if s[i] is valid)
        #      + T(i-2) + 1 (if s[i-1: i+1] is valid)
        for i in range(n):
            # Base Case
            # T[0] = 1 if s[0] is valid
            # T[1] = 1 if s[1] is valid
            if i == 0:
                T[i] = 1 if self.valid(s[i]) else 0
            elif i == 1:
                T[i] = T[i-1] if self.valid(s[i]) else 0
                T[i] += 1 if self.valid(s[i-1:i+1]) else 0
            else:
                T[i] = T[i-1] if self.valid(s[i]) else 0
                T[i] += T[i-2] if self.valid(s[i-1:i+1]) else 0

        # T[i] = number of ways to decode the string at index i
        return T[-1] if n > 0 else 0 

    def valid(self, s:str) -> bool:
        # Assume s are always able to be converted to a valid integer
        if len(s) > 2:
            return False
        elif len(s) == 2:
            # 0x are invalid
            if s[0] == '0':
                return False
        if int(s) > 26 or int(s) < 1:
            return False
        return True
        
