
def isPalindrome(self, s: str) -> bool:
    if not s:
        return False
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalpha() and not s[l].isdigit():
            l += 1
        while l < r and not s[r].isalpha() and not s[r].isdigit():
            r -= 1

        if l < r and s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1
    return True
