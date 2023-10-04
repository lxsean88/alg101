    def getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1, left + 1

    def longestPalindrome(self, s: str) -> str:
        ans = (0, 0)
        for mid in range(len(s)):
            ans = max(ans, self.getPalindrome(s, mid, mid))
            ans = max(ans, self.getPalindrome(s, mid, mid+1))
        
        return s[ans[1]: ans[0]+ans[1]]
