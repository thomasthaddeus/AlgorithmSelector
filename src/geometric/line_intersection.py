class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class LineIntersection:
    @staticmethod
    def on_segment(p, q, r):
        """Given three collinear points p, q, and r, check if point q lies on line segment 'pr'"""
        if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
            return True
        return False

    @staticmethod
    def orientation(p, q, r):
        """Find orientation of ordered triplet (p, q, r).
        Returns 0 if p, q and r are collinear, 1 if Clockwise, 2 if Counterclockwise"""
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clock or counterclock wise

    @staticmethod
    def do_intersect(seg1, seg2):
        """Return true if line segments 'seg1' and 'seg2' intersect."""
        p1, q1 = seg1.p1, seg1.p2
        p2, q2 = seg2.p1, seg2.p2

        # Find four orientations needed for general and special cases
        o1 = LineIntersection.orientation(p1, q1, p2)
        o2 = LineIntersection.orientation(p1, q1, q2)
        o3 = LineIntersection.orientation(p2, q2, p1)
        o4 = LineIntersection.orientation(p2, q2, q1)

        # General case
        if o1 != o2 and o3 != o4:
            return True

        # Special Cases
        if o1 == 0 and LineIntersection.on_segment(p1, p2, q1):
            return True
        if o2 == 0 and LineIntersection.on_segment(p1, q2, q1):
            return True
        if o3 == 0 and LineIntersection.on_segment(p2, p1, q2):
            return True
        if o4 == 0 and LineIntersection.on_segment(p2, q1, q2):
            return True

        return False  # Doesn't fall in any of the above cases

# Example usage
line1 = LineSegment(Point(1, 1), Point(10, 1))
line2 = LineSegment(Point(1, 2), Point(10, 2))
print("Do line1 and line2 intersect?", LineIntersection.do_intersect(line1, line2))

line3 = LineSegment(Point(10, 0), Point(0, 10))
line4 = LineSegment(Point(0, 0), Point(10, 10))
print("Do line3 and line4 intersect?", LineIntersection.do_intersect(line3, line4))
