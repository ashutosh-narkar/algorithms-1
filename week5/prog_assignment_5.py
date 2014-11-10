#!/usr/bin/env python
'''
Programming Assignment - 5
Implement Dijkstra's shortest-path algorithm on an
undirected weighted graph containing 200 nodes
Running time O(nm) where n = number of nodes, m = number of edges
'''
import os


def create_graph(graph_file):
    '''
    Given the graph file, create an undirected graph
    using the adjacency list representation.
    The graph is keyed on the node with value being a list of lists.
    First element is the node to which the key node is connected,
    while the second element is the weight of the edge.
    eg. {1:[[2, 10]]} -> node 1 connected to node 2 with an edge of weight 10
    '''
    ugraph = {}
    with open(graph_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split('\t')
            # sample output
            # ['1', '80,982', '163,8164', '170,2620',
            #'145,648', '55,6399', '\r\n']
            key = int(parts[0])
            value = []
            for item in parts[1:-1]:
                node_wt = map(int, item.split(','))
                value.append(node_wt)
            ugraph[key] = value
    return ugraph


def run_dijkstras(graph, source):
    '''
    Given an undirected graph and source vertex,
    run Dijkstra's shortest-path algorithm on this graph,
    to compute the shortest-path distances between source
    and every other vertex of the graph
    '''
    visited = {}
    # initially all nodes are unvisited
    unvisited = {node: float('inf') for node in graph}
    unvisited[source] = 0  # distance of source from itself
    shortest_path = {}
    shortest_path[source] = set()  # shortest path of source from itself

    current = source
    while unvisited:
        for neigh, wt in graph[current]:
            if neigh in unvisited:
                dist = _get_dijkstras_greedy_criterion(unvisited[current], wt)
                if dist < unvisited[neigh]:
                    unvisited[neigh] = dist
                    shortest_path[neigh] = shortest_path[current].union(set(
                                                                           [current, neigh]))
        visited[current] = unvisited[current]
        del unvisited[current]
        if not unvisited:
            break
        current, currentdist = sorted(unvisited.items(), key=lambda x: x[1])[0]

    return (visited, shortest_path)


def _get_dijkstras_greedy_criterion(tail_dist, egde_wt):
    '''
    Given the shortest distance of tail of the edge from source
    and the edge weight, return distance of head of the edge from source using
    Diijkstras_greedy_criterion given by:
    head_dist = tail_dist + edge_wt_tail_to_head
    '''
    return tail_dist + egde_wt


def main():
    path = os.path.expanduser('~/coursera/algorithms1/week5/dijkstraData.txt')
    mygraph = create_graph(path)
    dist, paths = run_dijkstras(mygraph, 1)
    print dist, paths

if __name__ == '__main__':
    main()
