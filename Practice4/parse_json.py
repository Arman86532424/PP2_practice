import json

# Read the JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Print header
print("Interface Status")
print("=" * 80)

# Print column headers
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + "  " + "-" * 6 + " " + "-" * 6)

# Parse and print each interface
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr'] if attributes['descr'] else ''
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    # Print formatted row
    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")