# write tests for bfs
import pytest
from search import graph

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    test_network = 'data/citation_network.adjlist'
    start_node = "Luke Gilbert"
    end_node_good = "Martin Kampmann"
    end_node_bad = "Reza Abbasi-Asl"
    end_node_same = "Luke Gilbert"
    supposed_lineage = ['Luke Gilbert', '33483487', 'Martin Kampmann']

    g = graph.Graph(test_network)

    bfs_output_good = g.bfs(start = start_node, end = end_node_good)
    bfs_output_bad = g.bfs(start = start_node, end = end_node_bad)
    bfs_output_same = g.bfs(start = start_node, end = end_node_same)

    assert(bfs_output_good == supposed_lineage)
    assert(bfs_output_bad == None)
    assert(bfs_output_same == end_node_same)
    assert(bfs_output_same == start_node)

def test_checkNode():
    # Test two start nodes, one that we know exists in the network, one that does not
    good_node = "Luke Gilbert"
    bad_node = "Luke Glibert"

    test_network = 'data/tiny_network.adjlist'
    g = graph.Graph(test_network)

    # Test the good node:
    try:
        good_test = g.check_node(good_node)
    except:
        good_test = False
    
    # Test the bad node:
    try: 
        bad_test = g.check_node(bad_node)
    except:
        bad_test = False

    assert((good_test == None) and bad_test == False)

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    test_network = 'data/tiny_network.adjlist'
    g = graph.Graph(test_network)
    start_node = "Luke Gilbert"
    traversal_output = g.bfs(start = start_node)
     
    assert(traversal_output[5] == "Martin Kampmann")

def test_empty_network():
    empty_network = 'test/empty_network.adjlist'
    g_empty = graph.Graph(empty_network)

    try: 
        empty_check = g_empty.check_empty_graph()
    except:
        empty_check = False

    test_network = 'data/tiny_network.adjlist'
    g_test = graph.Graph(test_network)

    try:
        test_check = g_test.check_empty_graph()
    except:
        test_check = False

    assert ((test_check == None) and (empty_check == False))