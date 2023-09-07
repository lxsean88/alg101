i
def addBinary(a: str, b: str) -> str:
    x, y = int(a, 2), int(b, 2)
    carryover = 0
    while y:
        ans = x ^ y
        carryover = (x & y) << 1
        x, y = ans, carryover
    return bin(x)[2:]
