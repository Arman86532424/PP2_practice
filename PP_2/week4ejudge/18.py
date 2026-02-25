import sys

def find_reflection_point(x1, y1, x2, y2):
    """
    Light goes from A(x1,y1) → P(x,0) on x-axis → B(x2,y2)
    Uses method of image: reflect B over x-axis to B'(x2, -y2)
    The intersection of A–B' with the x-axis is the reflection point P.
    """
    # Image of B over x-axis
    xb_prime = x2
    yb_prime = -y2
    
    # Line from A(x1,y1) to B'(xb_prime, yb_prime)
    dx = xb_prime - x1
    dy = yb_prime - y1
    
    # Special case: A is already on mirror → degenerate (but y1=0 not typical)
    if abs(y1) < 1e-12:
        # Usually problem assumes y1 > 0, but return sensible point
        return x1, 0.0
    
    # Parameter t where line crosses y = 0
    # y = y1 + t * dy = 0  ⇒  t = -y1 / dy
    t = -y1 / dy
    
    # x-coordinate of intersection
    x = x1 + t * dx
    y = 0.0
    
    return x, y


def main():
    input = sys.stdin.read
    data = input().split()
    
    # Read coordinates
    x1 = float(data[0])
    y1 = float(data[1])
    x2 = float(data[2])
    y2 = float(data[3])
    
    xr, yr = find_reflection_point(x1, y1, x2, y2)
    
    # Print with high precision (10 decimal places matches examples)
    print(f"{xr:.10f} {yr:.10f}")


if __name__ == "__main__":
    main()