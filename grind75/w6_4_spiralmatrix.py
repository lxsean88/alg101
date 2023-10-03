def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    rst = []
    up, left = 0
    down, right = len(matrix) - 1, len(matrix[0]) - 1

    while up <= down and left <= right:
        for i in range(left, right+1):
            rst.append(matrix[up][i])
        up += 1
        if up > down:
            break

        for i in range(up, down+1):
            rst.append(matrix[i][right])
        right -= 1

        for in in range(right, left-1, -1):
            rst.append(matrix[down][i])
        down -= 1
        if left > right:
            break

        for i in range(down, up-1, -1):
            rst.append(matrix[i][left])
        left += 1

    return rst
