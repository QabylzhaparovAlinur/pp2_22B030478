import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print('Interface Status')
print('=' * 80)
print('DN                                                 Description           Speed    MTU  ')
print('-' * 50, ' ', '-' * 20, '  ', '-' * 6, '  ', '-' * 6)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    mtu = attributes['mtu']
    print(f'{dn:<50}{"":<21}inherit   {mtu:<6}')
