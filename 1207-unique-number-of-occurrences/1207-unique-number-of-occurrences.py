class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        seen = set()

        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        for num in d:
            if d[num] in seen:
                return False
            
            seen.add(d[num])

        return True