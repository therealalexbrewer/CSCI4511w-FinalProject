import sys
import timeit
import time

sys.path.append('problems')
sys.path.append('algorithms')
sys.path.append('utils')

from towers import TowersOfHanoi

from search import ID_DFS
from search import DL_DFS
from search import DFS_Graph
from search import BFS_Graph
from search import BFS_Tree

from utils import Utils

#  THE GOAL OF THIS CODE:
#  The point of the following code is to test the question: what algorithm will consistently find the solution fastest at each variation of N discs in Towers of Hanoi?
#  To answer this question, there's a few tests that have been created to see which algorithm is the best performing with respect to time. There's 3 experiments that
#  are tested in this code, and they help answer the research question that has been propositioned.




def test_proj():
    
    

    # EXPERIMENT 1: THE GOAL EXPERIMENT 1 IS MEANT TO TEST EACH OF THE 3 ALGORITHMS, DFS, BFS, AND DLDFS. EACH ALGORITHM WILL SOLVE TOWERS WITH A DISC SIZE OF 3,4 AND 5. THE DEPTH 
    # LIMIT FOR DLDFS WILL ALWAYS BE SET TO THE OPTIMAL SOLUTION DEPTH HERE, WHICH IS 2^N - 1 MOVES. THE IDEA IS THAT THIS TEST WILL DETERMINE WHICH ALGORITHM CAN SOLVE THE TOWERS
    # OF HANOI PROBLEM THE FASTEST. 

    # ---- BEGIN EXPERIMENT 1 TESTS ----

    # -- NUMBER OF DISCS = 3 --

    # towers = 3 

    # # TEST 1 - BFS_GRAPH
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = BFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)

    # # TEST 2 - DFS_GRAPH (PARENT) 
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)
    # towers = towers + 1

    
    # # TEST 3 - DL_DFS (SET TO THE OPTIMAL SOLUTION)
    # depthLimit = 7
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DL_DFS(verbose=True, depth_limit=depthLimit)
    # Utils.solveProblem(title, problem, searchAlgorithm)  



    # # -- NUMBER OF DISCS = 4 --

    # towers = 4

    # # TEST 1 - BFS_GRAPH
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = BFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)

    # # TEST 2 - DFS_GRAPH (PARENT)
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)

    # # TEST 3 - DL_DFS (SET TO THE OPTIMAL SOLUTION)
    # depthLimit = 15
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DL_DFS(verbose=True, depth_limit=depthLimit)
    # Utils.solveProblem(title, problem, searchAlgorithm)  

    # # -- NUMBER OF DISCS = 5 --

    # towers = 5 

    # # TEST 1 - BFS_GRAPH
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = BFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)

    # # TEST 2 - DFS_GRAPH (PARENT)
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DFS_Graph(verbose=True)
    # Utils.solveProblem(title, problem, searchAlgorithm)

    # # TEST 3 - DL_DFS (SET TO THE OPTIMAL SOLUTION)
    # depthLimit = 31
    # title = "Towers: %d " % (towers)
    # problem = TowersOfHanoi(towers)
    # searchAlgorithm = DL_DFS(verbose=True, depth_limit=depthLimit)
    # Utils.solveProblem(title, problem, searchAlgorithm)  

    # ---- END OF EXPERIMENT 1 TESTS ----

    # EXPERIMENT 2: THE GOAL OF EXPERIMENT 2 IS TO DETERMINE WHAT THE "LIMITS" OF EACH ALGORITHM IS. THIS WILL HELP IN THE DISCOVERY OF WHICH ALGORITHM IS CONSISTENLY
    # PERFORMING FASTER THAN THE OTHERS. IF THE ALGORITHM TAKES MORE THAN ONE HOUR TO FIND THE SOLUTION, THE TEST WILL BE TERMINATED AND THE "LIMIT" OF THE ALGORITHM
    # WILL BE THE LAST TEST THAT TOOK UNDER AN HOUR.

    # ---- BEGIN EXPERIMENT 2 TESTS ----

    # RUN A LOOP THAT GOES UP TO 20 TO TEST THE TIME IT TAKES FOR EACH ALGORITHM TO SOLVE A CERTAIN AMOUNT OF DISCS AT A GIVEN TIME. IF THE ALGORITHM POSTS RESULTS
    # THAT EXCEED AN HOUR IN LENGTH, THE TESTS WILL BE TERMINATED AND THAT WILL BE THE THEORETICAL LIMIT FOR THAT ALGORITHM.
    # towers = 3
    # while towers < 15:
    #     # TEST 1 - BFS_GRAPH
    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = BFS_Graph(verbose=True)
    #     Utils.solveProblem(title, problem, searchAlgorithm)  
    #     towers = towers + 1

    # towers = 3
    # while towers < 15:
    #      # TEST 2 - DFS_GRAPH (PARENT)
    #     depthLimit = 50
    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = DL_DFS(verbose=True)
    #     Utils.solveProblem(title, problem, searchAlgorithm)
    #     towers = towers + 1

    # towers = 3
    # while towers < 15:
    #      # TEST 3 - DL_DFS (SET TO THE OPTIMAL SOLUTION DEPTH)
    #     depthLimit = (2**towers) -1
    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = DL_DFS(verbose=True,depth_limit=depthLimit)
    #     Utils.solveProblem(title, problem, searchAlgorithm)
    #     towers = towers + 1

    towers = 3
    while towers < 15:
         # TEST 3 - DL_DFS (SET TO THE 5000)
        depthLimit = 500
        title = "Towers: %d " % (towers)
        problem = TowersOfHanoi(towers)
        searchAlgorithm = DL_DFS(verbose=True,depth_limit=depthLimit)
        Utils.solveProblem(title, problem, searchAlgorithm)
        towers = towers + 1
        
    # ---- END OF EXPERIMENT 2 TESTS ----

    # EXPERIMENT 3: THE GOAL OF EXPERIMENT 3 IS TO TEST HOW DIFFERENT DEPTH LIMITS FOR DLDFS WILL EFFECT THE TIME IT TAKES TO FIND A SOLUTION. THE IDEA IS TO LEARN WHETHER
    # OR NOT RANDOM CHANCE CAN INCREASE THE LIKELIHOOD OF FINDING A SOLUTION TO TOWERS FASTER THAN BFS OR DFS. THE LIMITS ARE SET TO THE CURRENT NUMBER OF DISCS X100, X1000,
    # AND X10000. WE WILL START THE TESTS AT A DISC SIZE OF 3 AND INCREMENT UP TO A MAX OF 15, SINCE EXPERIMENT 2 SHOWED US THAT THE LIMITS OF THESE ALGORITHMS 
    # WITH RESPECT TO TIME WON'T EXCEED MORE THAN 15 DISCS.

    # ---- BEGIN EXPERIMENT 3 TESTS ----

    # towers = 3;
    # while towers < 15:
    #      # TEST 3 - ID_DFS
    #     depthLimit = 50
    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = DL_DFS(verbose=True, depth_limit=towers*100)
    #     Utils.solveProblem(title, problem, searchAlgorithm)  

    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = DL_DFS(verbose=True, depth_limit=towers*1000)
    #     Utils.solveProblem(title, problem, searchAlgorithm)  

    #     title = "Towers: %d " % (towers)
    #     problem = TowersOfHanoi(towers)
    #     searchAlgorithm = DL_DFS(verbose=True, depth_limit=towers*10000)
    #     Utils.solveProblem(title, problem, searchAlgorithm)  
    #     towers = towers + 1

    # ---- END OF EXPERIMENT 3 TESTS ----

 

    # ----- END TOWERS OF HANOI TESTS -----




# CALL TO test_proj TO START EXPERIMENTS
test_proj()

