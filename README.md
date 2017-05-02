# travelling-salesman-problem
An implementation of a brute-force and Held-Karp algorithm in python to the TSP. This program is designed to use TSPLib graphs from http://www.math.uwaterloo.ca/tsp/vlsi/index.html. 
Additionally, this will graph the given nodes and show the optimal tour.
The given implementations only work up to around 24 cities (due to space/time).


This was used for a research paper on the TSP. Check TSPPaper.tex for Latex code or the pdf file to see the final paper. 

# to run: 
1. Clone repository
2. cd into directory
3. ~python TSP.py

# Notes: 
The program defaults to running test.tsp. 
File format:

NAME : xqf131
COMMENT : Bonn VLSI data set with 131 points
COMMENT : Uni Bonn, Research Institute for Discrete Math
COMMENT : Contributed by Andre Rohe
TYPE : TSP
DIMENSION : 4
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
1 0 1
2 0 2
3 1 0
4 1 2
EOF

You can easily add nodes to your liking. The format is:
Node-Number x-coordinate y-coordinate

This program makes use of Carl Ekerot's Held-Karp implementation found at:
https://github.com/CarlEkerot/held-karp
