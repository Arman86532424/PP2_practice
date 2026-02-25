import sys
import math

def shortest_path_around_circle(R, ax, ay, bx, by):
    """
    Shortest path from A(ax,ay) to B(bx,by) that stays outside or on
    the circle centered at (0,0) with radius R.
    Points A and B are guaranteed to be on or outside the circle.
    """
    # Distances from origin
    dA = math.hypot(ax, ay)
    dB = math.hypot(bx, by)
    
    # Straight-line distance
    straight = math.hypot(bx - ax, by - ay)
    if straight < 1e-10:
        return 0.0
    
    # Perpendicular distance from origin to line AB
    cross = abs(ax * by - bx * ay)
    dist_to_line = cross / straight
    
    # If line doesn't enter the interior (dist ≥ R), straight is allowed
    if dist_to_line >= R - 1e-9:
        return straight
    
    # Otherwise we must go around → use tangent + arc path
    
    # Angle at center between OA and OB
    cos_theta = (ax * bx + ay * by) / (dA * dB)
    cos_theta = max(min(cos_theta, 1.0), -1.0)
    theta = math.acos(cos_theta)
    
    # Length of the two tangent segments (same for both paths)
    len_tang = math.sqrt(max(0.0, dA*dA - R*R)) + math.sqrt(max(0.0, dB*dB - R*R))
    
    # Two possible paths: shorter arc and longer arc
    path_short_arc  = len_tang + R * theta
    path_long_arc   = len_tang + R * (2.0 * math.pi - theta)
    
    # Shortest detour is the minimum of the two
    return min(path_short_arc, path_long_arc)


def main():
    data = sys.stdin.read().split()
    
    R  = float(data[0])
    x1 = float(data[1])
    y1 = float(data[2])
    x2 = float(data[3])
    y2 = float(data[4])
    
    ans = shortest_path_around_circle(R, x1, y1, x2, y2)
    
    # Print with enough precision (matches example style)
    print(f"{ans:.10f}")


if __name__ == "__main__":
    main()