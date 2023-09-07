
def longestPalindrome(self, s: str) -> int:
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

        total = 0
        odd = False

        for k, v in hm.items():
            if v % 2 == 0:
                total += v
            else:
                if not odd:
                    total += v
                    odd = True
                else:
                    total += v-1
        return total
