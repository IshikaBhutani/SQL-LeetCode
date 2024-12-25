from typing import List
import math

def find_higgs(particles: List[List[int]]) -> List[int]:
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def closest_pair(points_sorted_by_x, points_sorted_by_y):
        n = len(points_sorted_by_x)
        if n <= 3:
            min_dist = float('inf')
            closest = None
            for i in range(n):
                for j in range(i + 1, n):
                    d = distance(points_sorted_by_x[i], points_sorted_by_x[j])
                    if d < min_dist:
                        min_dist = d
                        closest = (points_sorted_by_x[i], points_sorted_by_x[j])
            return min_dist, closest

        mid = n // 2
        midpoint_x = points_sorted_by_x[mid][0]
        left_x = points_sorted_by_x[:mid]
        right_x = points_sorted_by_x[mid:]
        left_y = list(filter(lambda p: p[0] <= midpoint_x, points_sorted_by_y))
        right_y = list(filter(lambda p: p[0] > midpoint_x, points_sorted_by_y))
        left_min, left_closest = closest_pair(left_x, left_y)
        right_min, right_closest = closest_pair(right_x, right_y)

        if left_min < right_min:
            d = left_min
            closest = left_closest
        else:
            d = right_min
            closest = right_closest

        strip = [p for p in points_sorted_by_y if abs(p[0] - midpoint_x) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                d_strip = distance(strip[i], strip[j])
                if d_strip < d:
                    d = d_strip
                    closest = (strip[i], strip[j])

        return d, closest

    points = [(x, y, i) for i, (x, y) in enumerate(particles)]
    points_sorted_by_x = sorted(points, key=lambda p: (p[0], p[1]))
    points_sorted_by_y = sorted(points, key=lambda p: (p[1], p[0]))
    _, closest = closest_pair(points_sorted_by_x, points_sorted_by_y)
    return sorted([closest[0][2], closest[1][2]])

# Example Usage
particles = [[3, 2], [-4, -1], [1, -1], [8, 1], [0, 5]]
print(find_higgs(particles))  # Output: [0, 2]