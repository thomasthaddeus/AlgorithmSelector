class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class ConvexHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    @staticmethod
    def orientation(p, q, r):
        """Return positive if p-q-r are clockwise, neg if counterclockwise, zero if collinear."""
        return (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

    def graham_scan(self):
        # Find the bottom-most point (or choose the left-most point in case of tie)
        min_y = min(self.points, key=lambda point: (point.y, point.x))
        self.points.sort(key=lambda p: (atan2(p.y - min_y.y, p.x - min_y.x), p.y, p.x))

        for p in self.points:
            while len(self.hull) >= 2 and self.orientation(self.hull[-2], self.hull[-1], p) <= 0:
                self.hull.pop()
            self.hull.append(p)

    def get_hull_points(self):
        if not self.hull:
            self.graham_scan()
        return self.hull

# Example usage
points = [Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
          Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)]
convex_hull = ConvexHull(points)
hull_points = convex_hull.get_hull_points()

print("Convex Hull Points:")
for point in hull_points:
    print(point)
