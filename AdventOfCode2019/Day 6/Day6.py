class Node(object):
    def __init__(self):
        self.father = None
        self.id = None
        self.depth = None
        self.children = []

def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in node.children:
            n.depth = node.depth + 1
            dfs(graph,n,visited)
    return visited



# Read input
input = [line.rstrip('\n') for line in open('p6.txt')]
nodes = []
node_visited = set()


# Iterate over each line of input
for obj in input:
    tmp1 = obj.split(')')[0]
    tmp2 = obj.split(')')[1]

    # Parent Node
    if tmp1 not in node_visited:
        node_par = Node()
        node_par.id = tmp1
        nodes.append(node_par)
        node_visited.add(tmp1)
        # Check if root
        if tmp1 == 'COM':
            root = node_par
            root.depth = 0
    ## Node already created
    else:
        for i in range(len(nodes)):
            if tmp1 == nodes[i].id:
                node_par = nodes[i]

    # Child node
    if tmp2 not in node_visited:
        node_ch = Node()
        node_ch.id = tmp2
        nodes.append(node_ch)
        node_visited.add(tmp2)
    ## Node already created
    else:
        for i in range(len(nodes)):
            if tmp2 == nodes[i].id:
                node_ch = nodes[i]

    #Father child relationship
    node_ch.father = node_par
    node_par.children.append(node_ch)

#DFS traversal of tree to create depths
dfs(nodes,root,[])

""" Part1
# Run through all nodes one more to calculate depths
sum = 0
for i in range(len(nodes)):
    sum = sum + nodes[i].depth
print(sum)
"""

#Part 2
# Find depth of YOU, SAN and all their ancestors
for i in range(len(nodes)):
    if nodes[i].id == 'YOU':
        you_depth = nodes[i].depth
        you_ancestors = []
        ancestor = nodes[i]
        while ancestor.father.id != 'COM':
            you_ancestors.append(ancestor.father)
            ancestor = ancestor.father
    if nodes[i].id == 'SAN':
        san_depth = nodes[i].depth
        san_ancestors = []
        ancestor = nodes[i]
        while ancestor.father.id != 'COM':
            san_ancestors.append(ancestor.father)
            ancestor = ancestor.father
# Check LCA (lowest common ancestor) and find his depth
i = 0
while (you_ancestors[len(you_ancestors)-i-1] == san_ancestors[len(san_ancestors) - i-1]):
    i += 1
lca_depth = you_ancestors[len(you_ancestors)-i].depth

# Calculate distance
print (you_depth - lca_depth + san_depth - lca_depth - 2)
