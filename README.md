# Most Important node finder
This is python module is used to find the top k nodes in an undirected un-weighted graphs usinf the concept of betweenness centrality. <br/>


# Use this 

Import this file and make an object of class Graph and pass the pa

```
import


>>> vertices = [1, 2, 3, 4,5,6,7,8]
>>> edges  = [(1,2), (1, 3), (2, 3), (3, 4), (2, 6), (3,5), (4, 5), (4,6), (5,6), (6,8), (6,7), (5,8), (7,8), (5,7)]
>>> graph = Graph(vertices, edges)
>>> graph.top_k_betweenness_centrality()

```


This will top_k_betweenness_centrality() returns a list of all the nodes that have highest b
