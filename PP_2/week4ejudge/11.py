import json
import sys

def apply_patch(source, patch):
    for key, p_val in patch.items():
        if p_val is None:
            source.pop(key, None)  # remove if exists
        elif key in source and isinstance(source[key], dict) and isinstance(p_val, dict):
            apply_patch(source[key], p_val)  # recursive update
        else:
            source[key] = p_val  # add or replace
    return source

# Read input
source = json.loads(sys.stdin.readline().strip())
patch = json.loads(sys.stdin.readline().strip())

result = apply_patch(source, patch)

# Print compact JSON with sorted keys
print(json.dumps(result, separators=(',', ':'), sort_keys=True))