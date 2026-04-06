class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Two Pointer
        result = []

        if len(temperatures) == 1:
            return [0]

        for start in range(len(temperatures)):
            for end in range(start+1, len(temperatures)):
                print(f"start is ({start},{temperatures[start]} , end is ({end}, {temperatures[end]}")
                if temperatures[end] > temperatures[start]:
                    result.append(end - start)
                    break
                elif end == len(temperatures) - 1:
                    result.append(0)
        result.append(0)
        return result

