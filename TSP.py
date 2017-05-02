import math
import parser
import networkx as nx
import matplotlib.pyplot as plt
import heldKarp as hk
import time

#from plot import plotTSP

G=nx.Graph()
graphTups = parser.get_cities_tups();
dictNodes = parser.get_cities_dict();
graphNodes = {}

count = 0
for node in dictNodes:
    #for some reason the api I used gives me the points twice, so dont add if < len()
    if(count < len(dictNodes)/2):
        graphNodes[node[0]] = node[1]
    count+=1

count = 1
for point in graphTups:
    if(count-1 < len(dictNodes)/2):
        G.add_node(count, pos = (point[0],point[1]))
    count+=1
print(G.nodes())

bestScore = 999999999
bestPath = []

def getDistancesMatrix(nodes):
    distances = [[ 0 for i in range(len(nodes))] for j in range(len(nodes))]
    i = 0
    for curNode,xy in nodes.iteritems():
        j = 0
        for node,xy in nodes.iteritems():
            dist = math.sqrt(((xy[0] - nodes[curNode][0]) * (xy[0] - nodes[curNode][0])) + 
                    ((xy[1] - nodes[curNode][1]) * (xy[1] - nodes[curNode][1])))
            distances[i][j] = dist
            j+=1
        i+=1
    return distances

print getDistancesMatrix(graphNodes)

def bruteForceTSPHelper (nodes, start, curNode, path, score, visited):

    global bestScore
    global bestPath
 
    
    for node,xy in nodes.iteritems():
        if(len(visited) is 0):
            start = node
        #skip visited nodes
        if(node in visited):
            continue
        
        #compute distance
        dist = math.sqrt(((xy[0] - nodes[curNode][0]) * (xy[0] - nodes[curNode][0])) +
                ((xy[1] - nodes[curNode][1]) * (xy[1] - nodes[curNode][1])))
        # print "computing dist from a: %s and b: %s dist is: %d"% ( node, curNode, dist) 
        #update values
        prevNode = curNode
        curNode = node
        path.append(node)
        score += dist
        visited[node] = 1
        
        #did we visit them all?
        if(len(visited) == len(graphNodes)): 
            #compute distance
            distToStart = math.sqrt(((xy[0] - graphNodes[start][0]) * (xy[0] - graphNodes[start][0])) + 
                    ((xy[1] - graphNodes[start][1]) * (xy[1] - graphNodes[start][1])))
            score += distToStart
             
            if(score < bestScore): #update score if new best
                print "best: ", bestScore
                bestPath = path
                bestScore = score
        else:
            #recursively call function to get all permutations
            bruteForceTSPHelper(nodes, start, curNode, path, score, visited)
            
        del visited[node]
        #print("deleted : ", node)
        del path[-1]
        score -=dist
        curNode = prevNode

def bruteForceTSP(nodes):

    startNode = next (iter (nodes.keys()))

    bruteForceTSPHelper(nodes = nodes, 
            start = 0,
            curNode = startNode,
            path = [],
            score = 0,
            visited = {})

    print "best: ",bestScore
    print(bestPath)

start_time = time.time()
bruteForceTSP(graphNodes)
print("--- Brute Force ran in %s seconds ---" % (time.time() - start_time))

start_time = time.time()
a = hk.heldKarp(getDistancesMatrix(graphNodes))
print("--- Held-Karp ran in %s seconds ---" % (time.time() - start_time))
optimalPath = [x+1 for x in a[1]]
optimalPath.append(optimalPath[0])
print optimalPath

G.add_path(optimalPath)

nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=300)
plt.show()


