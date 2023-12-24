import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ClosestPair:
    def __init__(self, points):
        self.points = points

    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def brute_force(self, points):
        min_dist = float('inf')
        pair = None
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                dist = self.distance(points[i], points[j])
                if dist < min_dist:
                    min_dist, pair = dist, (points[i], points[j])
        return pair, min_dist

    def strip_closest(self, strip, d):
        min_dist = d
        pair = None
        strip.sort(key=lambda point: point.y)

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j].y - strip[i].y < min_dist:
                    dist = self.distance(strip[i], strip[j])
                    if dist < min_dist:
                        min_dist, pair = dist, (strip[i], strip[j])

        return pair, min_dist

    def closest_pair_rec(self, points_x, points_y):
        n = len(points_x)
        if n <= 3:
            return self.brute_force(points_x)

        mid = n // 2
        Qx = points_x[:mid]
        Rx = points_x[mid:]
        midpoint = points_x[mid].x
        Qy = list(filter(lambda point: point.x <= midpoint, points_y))
        Ry = list(filter(lambda point: point.x > midpoint, points_y))

        (p1, q1), dist1 = self.closest_pair_rec(Qx, Qy)
        (p2, q2), dist2 = self.closest_pair_rec(Rx, Ry)

        d = min(dist1, dist2)
        if d == dist1:
            d_pair = (p1, q1)
        else:
            d_pair = (p2, q2)

        strip = [point for point in points_y if abs(point.x - midpoint) < d]
        (p3, q3), dist3 = self.strip_closest(strip, d)

        if dist3 < d:
            return (p3, q3), dist3
        else:
            return d_pair, d

    def closest_pair(self):
        points_x = sorted(self.points, key=lambda point: point.x)
        points_y = sorted(self.points, key=lambda point: point.y)
        return self.closest_pair_rec(points_x, points_y)

# Example usage
points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
cp = ClosestPair(points)
pair, distance = cp.closest_pair()
print(f"Closest pair: {pair[0].x, pair[0].y} and {pair[1].x, pair[1].y} with distance {distance}")
