
def string_shift(s: str, shift: List[List(int)]) - str:
    if not shift:
        return 0
    tmp, n = 0, len(s)

    for l in shift:
        tmp += l[1] if l[0] == 0 else -l[1]

    actual_shift = tmp % n
    if actual_shift < 0:
        actual_shift += n

    return s[actual_shift:] + s[:actual_shift]
