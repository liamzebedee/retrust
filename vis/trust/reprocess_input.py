import json

interactions = []
with open('data.txt', 'r') as f:
    for i, line in enumerate(f.read().split('\n')):
        if i == 0: 
            continue
        
        vals = line.split(' ')[1:-1]
        interactions.append(vals)

with open('interactions.json', 'w') as f:
    json.dump(interactions, f)