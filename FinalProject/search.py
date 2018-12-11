'''
The intent with this search function is to create a generic framework
that can be applied to any problem. It should be configured so that you
can use this search and the Node class for any problem constructed using
the Problem class.
'''

from collections import deque
from node import Node, NodeFactory
from algorithm import Algorithm
import sys

# Specific search algorithm classes are defined below, all derived from Search.
# These include BFS_Tree, BFS_Graph, DFS_Tree, DFS_Graph
# The default Search method is a BFS tree search.

class Search(Algorithm):
    # BFS Tree Search is the default
    def __init__(self, strategy="BFS", tree=True, verbose=False):
        Algorithm.__init__(self, verbose)
        #self.log_count = 1
        self.visited = []   # visisted/explored list for Graph Search
        self.solution = []  # list of solutions (only 1 if all_solutions=False)
        self.tree = tree    # True for tree search, False for Graph search
        if not strategy == "BFS" and not strategy == "DFS" and not strategy == "DL_DFS":
            raise Exception ('ERROR: strategy must be "DFS" or "BFS" (case sensitive)')
        else:
            self.strategy = strategy


    # expands the node to create all children. If in Graph Search, remove all
    # child nodes with states that have been previously visited
    def valid_children(self, node, problem, node_factory):
        children = node_factory.expand(node, problem)
        if self.tree:
            return children
        # vvvvvvvvv   COMPLETE THE ELSE PART FOR GRAPH SEARCH   vvvvvvvvvvvv
        # vvvvvvvvv   maintain self.visited by adding each child if not already visited
        # vvvvvvvvv   make sure you do not mutate the list over which you are iterating
        else:
            valids = []
            if self.strategy=="BFS":
                for c in children:
                    if not c.state in self.visited:
                        self.visited.append(c.state)
                        valids.append(c)
            if self.strategy=="DFS":
                for c in children:
                    if not self.node_in_parents(c):
                        valids.append(c)
                    
            return valids

    # The primary function to solve any problem with the instantiated search algorithm.
    # path=True indicates path is part of the solution.
    # Can choose to find 1 solution (if it exists) or all solutions.
    def solve(self, problem, path=True, all_solutions=False):
        self.reset()
        self.problem = problem

        # Generate the initial (root) node
        node_factory = NodeFactory(verbose=self.verbose, record_parent=path )
        self.max_frontier_node_count = 0
        
        if self.strategy == "DL_DFS":
            print("Depth limit: ", self.max_depth)
            result = self.depth_limited_search(problem, node_factory, self.max_depth)
            if result == 'cutoff':
                print("No solution found")
            return result

        if self.verbose:
            print("Searching nodes")

        node = node_factory.make_node( problem.initial_state )
        # if self.strategy == "BFS" and self.tree == False:
        #     return BFS_Graph.breadth_first_graph_search(self, problem, node_factory, all_solutions)

        # For efficiency, check if node is goal state BEFORE putting on Q
        if problem.is_goal( node.state ):
            self.solution.append(node)
            self.total_node_count = 1
            if not all_solutions:
                return self.solution

        # Start the frontier Q by adding the root
        frontier=deque()
        frontier.append(node)
        self.visited.append(node.state)

        # Select a node from the frontier (using the  til nothing left to explore (i.e. frontier is empty)
        # OR a solution is found
        while len(frontier) > 0:
            #print(frontier)
            # vvvvvvvvvvvvvvvvvvvvvvvvv    add code block for if and elif:
            if self.strategy=="BFS":
                node = frontier.popleft()
            elif self.strategy=="DFS":
                node = frontier.pop()

            for child in self.valid_children(node, problem, node_factory):
                if child.depth > self.max_depth:
                    self.max_depth = child.depth
                if problem.is_goal( child.state ):
                    if self.verbose:
                        print("")
                        print("")
                        print("Max Frontier Count: ", self.max_frontier_node_count)
                        print("Visited: ", len(self.visited))
                    self.solution.append(child)
                    self.total_node_count = node_factory.node_count
                    if not all_solutions:
                        return child
                frontier.append(child)
                if len(frontier) > self.max_frontier_node_count:
                    self.max_frontier_node_count = len(frontier)
        self.total_node_count = node_factory.node_count
        if self.solution==[]:
            self.solution = None
        return self.solution


    def node_in_parents (self, node):
        parent = node.parent
        while parent is not None:
            if node.state != parent.state:
                parent = parent.parent
            else:
                return True  
        return False


    def depth_limited_search(self,problem, node_factory, limit=50):

        def recursive_dls(node, problem, limit, depth):
            
            if problem.is_goal(node.state):
                self.solution.append(node)
                self.total_node_count = node_factory.node_count
                self.max_depth = depth
                return node
            elif limit == 0:
                return 'cutoff'
            else:
                cutoff_occurred = False
                # 
                children = node_factory.expand(node, problem)
                for child in children:
                    if not self.node_in_parents(child):
                        result = recursive_dls(child, problem, limit - 1, depth + 1)
                        if result == 'cutoff':
                            cutoff_occurred = True
                        elif result is not None:
                            return result
                return 'cutoff' if cutoff_occurred else None

        # Body of depth_limited_search:
        node = node_factory.make_node( problem.initial_state )
        return recursive_dls(node, problem, limit, 0)

    def iterative_deepening_search(self,problem):
        for depth in range(sys.maxsize):
            result = self.depth_limited_search(problem, depth)
            if result != 'cutoff':
                return result
#####################################################################################################
# These are variations of Search that were created to make it more user friendly.
# You can instantiate Search directly and set appropriate parameters to achieve the same results.

class BFS_Tree(Search):
    def __init__(self, verbose=False):
        Search.__init__(self, strategy="BFS", tree=True, verbose=verbose)

class BFS_Graph(Search):
    def __init__(self, verbose=False):
        Search.__init__(self, strategy="BFS", tree=False, verbose=verbose)

class DFS_Tree(Search):
    def __init__(self, verbose=False):
        Search.__init__(self, strategy="DFS", tree=True, verbose=verbose)

class DFS_Graph(Search):
    def __init__(self, verbose=False):
        Search.__init__(self, strategy="DFS", tree=False, verbose=verbose)

class ID_DFS(Search):
    def __init__(self, verbose = False, depth_limit=5, tree=True):
        Search.__init__(self, strategy = "DL_DFS", tree = tree, verbose = verbose)
        self.max_depth = depth_limit

    def solve(self, problem, path=True, all_solutions=False):
        depthLimit = 1
        no_solution = True
        while depthLimit <= self.max_depth and no_solution:
            searchAlgorithm = DL_DFS(verbose=self.verbose, depth_limit = depthLimit)
            searchAlgorithm.max_depth = depthLimit
            result = searchAlgorithm.solve(problem, path, all_solutions)
            no_solution = result is None or result == 'cutoff'
            depthLimit += 1
        if no_solution:
            return
        self.solution = searchAlgorithm.solution
        self.total_node_count = searchAlgorithm.total_node_count
        self.max_depth = searchAlgorithm.max_depth
        self.problem = problem

class DL_DFS(Search):
    def __init__(self, verbose=False,depth_limit=5, tree=True):
        Search.__init__(self, strategy = "DL_DFS",tree=tree,verbose=verbose)
        self.max_depth = depth_limit

 


