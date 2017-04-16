import parser
import networkx as nx
import matplotlib.pyplot as plt
#from plot import plotTSP

G=nx.Graph()
graphTups = parser.get_cities_tups();
G.add_edges_from(graphTups);
print(G.nodes())
nx.draw(G)
plt.show()

#def BruteForceTSP


