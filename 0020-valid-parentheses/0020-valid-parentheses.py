class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        q = []

        for ch in s:
            if ch in pairs:
                if not q:
                    return False

                if q[-1] != pairs[ch]:
                    return False

                q.pop()

            else:
                q.append(ch)

        return len(q) == 0