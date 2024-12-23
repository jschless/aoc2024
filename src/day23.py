from collections import defaultdict
import networkx as nx

fname = "./examples/day23.txt"
fname = "./inputs/day23.txt"
conns = [(x[:2], x[3:]) for x in open(fname).read().strip().split()]
links = defaultdict(set)
ts = []
for a, b in conns:
    links[a].add(b)
    links[b].add(a)
    if a.startswith("t"):
        ts.append(a)
    if b.startswith("t"):
        ts.append(b)


triples = set()
for t in ts:
    # Only check triangles beginning with a t node
    for n in links[t]:
        # iterate through neighbors of neighbors and see if connected
        for n2 in links[n]:
            if n2 in links[t]:
                triples.add(tuple(sorted([t, n, n2])))

print("Part 1:", len(triples))

# P2 one liner courtesy of networkx
print("Part 2:", ",".join(sorted(max(nx.find_cliques(nx.Graph(conns)), key=len))))
