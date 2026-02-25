import json
import sys

NOT_FOUND = object()  # unique marker

def resolve_query(data, query):
    i = 0
    n = len(query)
    cur = data

    while i < n:
        # read key
        key = ""
        while i < n and query[i] not in ".[":
            key += query[i]
            i += 1

        if key:
            if not isinstance(cur, dict) or key not in cur:
                return NOT_FOUND
            cur = cur[key]

        # read indices
        while i < n and query[i] == "[":
            i += 1
            idx = ""
            while i < n and query[i] != "]":
                idx += query[i]
                i += 1
            if i >= n:
                return NOT_FOUND
            i += 1  # skip ]

            if not idx.isdigit():
                return NOT_FOUND
            idx = int(idx)

            if not isinstance(cur, list) or idx >= len(cur):
                return NOT_FOUND
            cur = cur[idx]

        if i < n and query[i] == ".":
            i += 1

    return cur

data = json.loads(sys.stdin.readline().strip())
q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().strip()
    result = resolve_query(data, query)
    if result is NOT_FOUND:
        print("NOT_FOUND")
    else:
        print(json.dumps(result, separators=(',', ':')))