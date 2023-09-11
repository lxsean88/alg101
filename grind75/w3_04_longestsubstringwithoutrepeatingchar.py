
def lenthOfLongestSubstring(s: str) -> int:
    unique = set()
    r, longest = 0, 0
    for l in range(len(s)):
        while r < len(s) and s[r] not in unique:
            unique.add(s[r])
            r += 1
        longest = max(longest, r - l)
        unique.remove(s[l])
    return longest
