
   def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            if len(h) < k:
                heapq.heappush(h, (- point[0] **2 - point[1] ** 2, point))

            elif point[0] **2 + point[1] ** 2 < - h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (- point[0] **2 - point[1] ** 2, point))

        rst = []
        for x, p in h:
            rst.append(p)

        return rst
