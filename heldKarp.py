import itertools
import random
import sys

"""
Held-Karp algorithm to solve TSP
distMatrix is a matrix of distances from vertex to vertex
"""
    
def heldKarp(distMatrix):
    n = len(distMatrix)

    # <key -> subset, value -> cost to read subset>
    # also takes into accout what node was used before subset, in order
    # to reconstruct the final path
    costs = {}

    #set costs for all vertexes to dist(startVertex, vertex)
    for k in range(1, n):
        costs[(1 << k, k)] = (distMatrix[0][k], 0)

    # iterate through, get costs and put them in costs matrix
    for subset_size in range(2, n):
        #get all subsets possible 
        for subset in itertools.combinations(range(1, n), subset_size):
            # represent the subset as bits to be used for the map key
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # get lowest cost for subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for i in subset:
                    if (i == 0 or i == k):
                        continue
                    res.append((costs[(prev, i)][0] + distMatrix[i][k], i))
                costs[(bits, k)] = min(res)

    bits = (2**n - 1) - 1

    # get optimal cost
    res = []
    for k in range(1, n):
        res.append((costs[(bits, k)][0] + distMatrix[k][0], k))
    opt, parent = min(res)

    path = []
    for i in range(n - 1):
        path.append(parent)
        newBits = bits & ~(1 << parent)
        _, parent = costs[(bits, parent)]
        bits = newBits

    path.append(0)

    return opt, list(reversed(path))


def getDistances(n):
    distMatrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            distMatrix[i][j] = distMatrix[j][i] = random.randint(1, 99)

    return distMatrix


if __name__ == '__main__':
    arg = sys.argv[1]

    distMatrix = getDistances(int(arg))

    # Pretty-print the distance matrix
    for row in distMatrix:
        print(''.join([str(n).rjust(3, ' ') for n in row]))

    print('')

    print(heldKarp(distMatrix))
