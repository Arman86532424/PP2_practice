import json


with open("sample-data.json", encoding="utf-8") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("DM"+' '*49 + 'Description'+' '*10 + 'Speed'+' '*2 +'MTU'+' '*6)
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    print(f"{attrs['dn']:<50} {attrs.get('descr',''):<20} {attrs['speed']:<6} {attrs['mtu']}")
    