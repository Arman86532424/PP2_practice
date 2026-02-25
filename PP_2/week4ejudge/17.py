import sys
import math

def radar_coverage_length(R, x1, y1, x2, y2):
    d1 = math.hypot(x1, y1)
    d2 = math.hypot(x2, y2)
    L = math.hypot(x2 - x1, y2 - y1)
    
    if L < 1e-9:
        return float(d1 <= R)
    
    # Perpendicular distance from (0,0) to line
    dist_to_line = abs(x1 * y2 - x2 * y1) / L
    
    if dist_to_line > R + 1e-9:
        return 0.0
    
    if d1 <= R and d2 <= R:
        return L
    
    # Find intersection parameters
    # t = [ -b ± sqrt(b² - c) ]
    b = (x1*(x2-x1) + y1*(y2-y1)) / L
    c = d1*d1 - R*R
    disc = b*b - c
    
    if disc < 0:
        disc = 0
    
    sd = math.sqrt(disc)
    t_enter = max(0.0, -b - sd)
    t_leave = min(L, -b + sd)
    
    if t_enter >= t_leave:
        return 0.0
    
    return t_leave - t_enter


def main():
    data = sys.stdin.read().split()
    R  = float(data[0])
    x1 = float(data[1])
    y1 = float(data[2])
    x2 = float(data[3])
    y2 = float(data[4])
    
    ans = radar_coverage_length(R, x1, y1, x2, y2)
    print(f"{ans:.10f}")


if __name__ == "__main__":
    main()