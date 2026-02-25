import json
import sys

def to_json_literal(value):
    if value == "<missing>":
        return value
    return json.dumps(value, separators=(',', ':'))

def deep_diff(a, b, path=""):
    diffs = []

    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        new_path = f"{path}.{key}" if path else key

        in_a = key in a
        in_b = key in b

        if not in_a:
            diffs.append((new_path, "<missing>", b[key]))
        elif not in_b:
            diffs.append((new_path, a[key], "<missing>"))
        else:
            va, vb = a[key], b[key]
            if isinstance(va, dict) and isinstance(vb, dict):
                diffs.extend(deep_diff(va, vb, new_path))
            elif va != vb:
                diffs.append((new_path, va, vb))

    return diffs

# Read input
obj1 = json.loads(sys.stdin.readline().strip())
obj2 = json.loads(sys.stdin.readline().strip())

differences = deep_diff(obj1, obj2)

if not differences:
    print("No differences")
else:
    for path, old, new in sorted(differences, key=lambda x: x[0]):
        print(f"{path} : {to_json_literal(old)} -> {to_json_literal(new)}")