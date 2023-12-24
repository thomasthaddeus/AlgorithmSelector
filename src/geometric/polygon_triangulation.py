class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PolygonTriangulation:
    def __init__(self, vertices):
        self.vertices = vertices

    def is_convex(self, prev, curr, next):
        """Return true if the triangle made with the provided points is convex."""
        return (curr.x - prev.x) * (next.y - prev.y) - (curr.y - prev.y) * (next.x - prev.x) > 0

    def is_ear(self, prev, curr, next, vertices):
        """Return true if the triangle made with the provided points is an ear."""
        if self.is_convex(prev, curr, next):
            for vertex in vertices:
                if vertex != prev and vertex != curr and vertex != next:
                    if self.is_point_inside_triangle(vertex, prev, curr, next):
                        return False
            return True
        return False

    def is_point_inside_triangle(self, p, t1, t2, t3):
        """Check if point p is inside the triangle formed by t1, t2 and t3."""
        def sign(p1, p2, p3):
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        d1 = sign(p, t1, t2)
        d2 = sign(p, t2, t3)
        d3 = sign(p, t3, t1)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

    def triangulate(self):
        """Triangulate the polygon and return a list of triangles."""
        vertices = self.vertices.copy()
        triangles = []

        while len(vertices) > 2:
            for i in range(len(vertices)):
                prev = vertices[i - 1]
                curr = vertices[i]
                next = vertices[(i + 1) % len(vertices)]

                if self.is_ear(prev, curr, next, vertices):
                    triangles.append((prev, curr, next))
                    vertices.remove(curr)
                    break

        return triangles

# Example usage
vertices = [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
polygon = PolygonTriangulation(vertices)
triangles = polygon.triangulate()

print("Triangles:")
for t in triangles:
    print(f"({t[0].x}, {t[0].y}) ({t[1].x}, {t[1].y}) ({t[2].x}, {t[2].y})")
