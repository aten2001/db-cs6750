from sys import stdin
from collections import defaultdict
# Taking in the relation
relation = input().split(',')
# Taking in functional dependencies
deps = {}
for line in stdin:
    fd = line.split('>')
    deps[fd[0]] = list(fd[1][:-1])
print("Relation:")
print(relation)
print("Functional Dependencies:")
print(deps)
def closure(attr, deps):
    def dfs(attr, deps, visited):
        visited.add(attr)
        if attr not in deps:
            return

        for neigh in deps[attr]:
            if neigh not in visited:
                dfs(neigh, deps, visited)
    
    visited = set()
    dfs(attr, deps, visited)
    return visited

print("------------------------------------------------")

# Finding attribute closure:
Fplus = {}
print("Attribute closure:")
for attr in relation:
    print(attr + "+:")
    closed = sorted(list(closure(attr, deps)))
    print(closed)
    Fplus[attr] = closed

print("------------------------------------------------")

# Find attributes that only occur on the RHS as a trivial dependency
candidate_key = set()
for attr in Fplus:
    flag = False
    for key in Fplus:
        if attr in Fplus[key] and key is not attr:
            flag = True
    if not flag:
        candidate_key.add(attr)
print("Candidate key:\n", candidate_key)



    
