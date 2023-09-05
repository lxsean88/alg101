
def isAnagram(self, s: str, t: str) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    s2 = ''.join(sorted(s))
    t2 = ''.join(sorted(t))
    return s2 == t2

def isAnagram2(self, s: str, t: str) -> bool:
    if not s and not t:
            return True
        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        hm = {}
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]] += 1
            else:
                hm[s[i]] = 1

            if t[i] in hm:
                hm[t[i]] -= 1
            else:
                hm[t[i]] = -1

        for key in hm:
            if hm[key] != 0:
                return False
        return True
