import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.filename = filename
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def check_empty_graph(self):
        if len(self.graph.nodes()) == 0:
            raise ValueError("Graph is empty")

    def check_node(self, node):
        """
        Check to make sure the node exists in the graph
        """
        if node and node not in self.graph.nodes():
            raise ValueError(f"Node {node} does not exist in the graph")

    
    def bfs_traversal(self, start):
        """
        Return a list, visited, of all the nodes that were traversed in the order they were traversed
        """
        queue = [start] # list of queue nodes, including the start
        visited = [ ] # list of visited nodes

        while queue:

            current_node = queue.pop(0) # Get the first node in the queue
            visited.append(current_node) # Add first node to the visited list
            frontier = [n for n in self.graph.neighbors(current_node)] # Get list of frontier nodes from the current node
            
            for frontier_node in frontier: 
                
                # If the frontier node in the froniter has not yet been visited and has not been in the queue
                if frontier_node not in visited and frontier_node not in queue:
                    queue.append(frontier_node) # Add frontier node to queue

        return visited


    def bfs_shortest_path(self, start, end):
        """
        Return a dictionary containing the parent node for each node
        """
        queue = [start] # List of quueu nodes, including the start
        visited = [ ] # List of visited ndoes
        parent_node = {start:None} # Keep track of parent nodes
        break_flag = False # switch when encountered end node

        while queue:

            current_node = queue.pop(0)
            visited.append(current_node)
            frontier = [n for n in self.graph.neighbors(current_node)]

            for frontier_node in frontier:

                if frontier_node not in visited and frontier_node not in queue:
                    queue.append(frontier_node)
                    parent_node[frontier_node] = current_node

                    if frontier_node == end:
                        break_flag = True
                        break;

                if break_flag:
                    break;
        
        return parent_node 
        
    def trace_parent_nodes(self, end, parent_node):
        """
        Combing the parent_node dictionary into a list
        If the end node does not exist in the parent_node dictionary, return none
        """
        if end not in parent_node:
            output = None

        else:
            node_lineage = [end]
            curr_node = end

            while curr_node:
                nde = parent_node[curr_node]
                node_lineage.append(nde)
                curr_node = nde
            
            node_lineage.pop()
            output = node_lineage[::-1]

        return output


    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Make sure the graph is not empty
        self.check_empty_graph()
        # Make sure that the start and end nodes exist in graph
        self.check_node(start)
        self.check_node(end)

        if end: # If end contains a valid node then run bfs and return the shortest path
            if end == start: # No need to run diddly squat
                output = end

            else:
                parent_node_list = self.bfs_shortest_path(start, end) # Get the list of parent nodes
                output = self.trace_parent_nodes(end, parent_node_list) # Get the node lineage

        else: # No end node input, return a list of nodes with the order of BFS traversal
            output = self.bfs_traversal(start)
    
        return output