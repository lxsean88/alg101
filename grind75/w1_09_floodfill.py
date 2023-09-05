
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    curcolor = image[sr][sc]
    newcolor = color
    if curcolor != newcolor:
        return image
    flood(image, sr, sc, curcolor, newcolor)
    return image

def flood(image, sr, sc, curcolor, newcolor):
    if sr < 0 or sc < 0 or sr > len(image) or sc > len(image[0]) or image[sr][sc] != curcolor:
        return

    image[sr][sc] = newcolor
    flood(image, sr+1, sc, curcolor, newcolor)
    flood(image, sr-1, sc, curcolor, newcolor)
    flood(image, sr, sc+1, curcolor, newcolor)
    flood(image, sr, sc-1, curcolor, newcolor)
