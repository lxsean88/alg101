
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for c in magazine:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

        for c in ransomNote:
            if c in hm and hm[c] >= 1:
                hm[c] -= 1
            else:
                return False

        return True
