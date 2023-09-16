
# https://www.lintcode.com/problem/3639/
def issplitable(s: str) -> bool:
    if not s or len(s) % 3 == 1:
        return False

    len2str = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            if count == 3:
                count = 1
            else:
                count += 1
        else:
            if count == 1:
                return False
            elif count == 2:
                len2str += 1
                if len2str > 1:
                    return False
            count = 1

    if count == 2:
        len2str += 1
    if count ==1 or len2str != 1:
        return False
    
    return True
