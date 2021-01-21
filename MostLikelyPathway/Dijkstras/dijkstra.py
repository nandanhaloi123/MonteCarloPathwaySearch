# =============================================================================
# We will create a dictionary to represent the graph
# =============================================================================
import numpy as np

def dijkstra(graph,start,goal):

    shortest_distance = {} #dictionary to record the cost to reach to node. We will constantly update this dictionary as we move along the graph.
    track_predecessor = {} #dictionary to keep track of path that led to that node.
    unseenNodes = graph #to iterate through all nodes
    infinity = 5000 #infinity can be considered a very large number
    track_path = [] #dictionary to record as we trace back our journey



# =============================================================================
# Initially we want to assign 0 as the cost to reach to source node and infinity as cost to all other nodes
# =============================================================================

    for node in unseenNodes:
        shortest_distance[node] = infinity

    shortest_distance[start] = 0

# =============================================================================
# The loop will keep running until we have entirely exhausted the graph, until we have seen all the nodes
# =============================================================================
# =============================================================================
# To iterate through the graph, we need to determine the min_distance_node every time.
# =============================================================================

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

# =============================================================================
# From the minimum node, what are our possible paths
# =============================================================================

        path_options = graph[min_distance_node].items()


# =============================================================================
# We have to calculate the cost each time for each path we take and only update it if it is lower than the existing cost
# =============================================================================

        for child_node, weight in path_options:
            if child_node not in unseenNodes:
                continue
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:

                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
# if track_pred[min_distance_node]!=child_node:
#
                track_predecessor[child_node] = min_distance_node
                if (child_node==27 or child_node==28):
                    print(track_predecessor[child_node])
# =============================================================================
# We want to pop out the nodes that we have just visited so that we dont iterate over them again.
# =============================================================================
        unseenNodes.pop(min_distance_node)
        #print(len(unseenNodes))


# =============================================================================
# Once we have reached the destination node, we want trace back our path and calculate the total accumulated cost.
# =============================================================================

    currentNode = goal
    #print(currentNode)
    while currentNode != start:
        try:
            #print(track_path)
            track_path.insert(0,currentNode)
            currentNode = track_predecessor[currentNode]
            #if(currentNode!=279 and currentNode!=280):
#            print(currentNode)
        except KeyError:
            print('Path not reachable')
            break
    track_path.insert(0,start)


# =============================================================================
#  If the cost is infinity, the node had not been reached.
# =============================================================================
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(track_path))
    return (shortest_distance[goal],track_path)


