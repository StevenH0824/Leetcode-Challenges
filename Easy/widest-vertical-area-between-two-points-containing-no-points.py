#1637. Widest Vertical Area Between Two Points Containing No Points

# Given n points on a 2D plane where points[i] = [xi, yi],
# Return the widest vertical area between two points such that no points
# are inside the area.

points1 = [[8,7],[9,9],[7,4],[9,7]]
points2 = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
points3 = [[1,5],[1,70],[3,1000],[55,700],[999876789,53],[987853567,12]]
result1 = 1
result2 = 3
result3 = 987853512
"""
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()  # Sort points on the x-coordinate from left to right
        max_width = 0
        for i in range(len(points)):
            if max_width < points[i][0] - points[i-1][0]:
                max_width = points[i][0] - points[i-1][0]
            else:
                continue
        return max_width
"""

def check(a,b) -> bool:
    return a == b

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    points.sort()  # Sort points on the x-coordinate from left to right
    max_width = 0
    for i in range(len(points)):
        if max_width < points[i][0] - points[i-1][0]:
            max_width = points[i][0] - points[i-1][0]
        else:
            continue
    return max_width



print(check(maxWidthOfVerticalArea(points1),result1),"\n")
print(check(maxWidthOfVerticalArea(points2),result2),"\n")
print(check(maxWidthOfVerticalArea(points3),result3),"\n")
