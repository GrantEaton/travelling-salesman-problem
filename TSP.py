import parser
import networkx as nx
import matplotlib.pyplot as plt
#from plot import plotTSP

G=nx.Graph()
graphTups = parser.get_cities_tups();


count = 1
for point in graphTups:
    G.add_node(count, pos = (point[0],point[1]))
    count+=1
print(G.nodes())
#G.add_edges_from(graphTups);
nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=300)
#nx.draw(G)
plt.show()

#string bestPath
#int bestScore

def BruteForceTSP (edges, start, curNode, path, score, visited):
    
    for node in edges[curNode]:
        if(node == start and len(visited) == len(edges) and score > bestScore):
            bestPath = path
            bestScore = score
        else:
            visited[curNode] = 1
            #BruteForceTSP(edges, node, (path + str(node)), 
