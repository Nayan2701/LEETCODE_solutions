class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        count_v=0
        maxi = float("-inf")
        for r in range(len(s)):
            if s[r]=='a' or s[r]=='e' or s[r]=='i' or s[r]=='o' or s[r]=='u':
                count_v+=1

            if r-l+1>k:
                if s[l]=='a' or s[l]=='e' or s[l]=='i' or s[l]=='o' or s[l]=='u':
                    count_v-=1
                l+=1
                    
            if r-l+1 ==k:
                maxi=max(maxi,count_v)

        return maxi