import json
from os.path import abspath

def load():
    interactions = None
    opinions = None
    evidence = None

    with open(abspath('./interactions.json'), 'r') as f:
        interactions = json.load(f)
    with open(abspath('./opinions.json'), 'r') as f:
        opinions = json.load(f)
    with open(abspath('./evidence.json'), 'r') as f:
        evidence = json.load(f)



load()