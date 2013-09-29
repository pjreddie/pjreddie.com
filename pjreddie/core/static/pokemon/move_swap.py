import json
a = json.loads(open("moves_old.json").read())
b = open("verbs.list").read().split()
mapping = {}
new = {}
for name in a:
    nn = b.pop()
    mapping[name] = nn
    new[nn] = a[name]
    new[nn]['name'] = nn

out = open("moves.json", "w")
out.write(json.dumps(new))

p = open("pokemon_old.json").read()
for item in mapping:
    print "'"+item+"'", "'"+mapping[item]+"'"
    p = p.replace(item, mapping[item])

out2 = open("pokemon.json", "w")
out2.write(p)
