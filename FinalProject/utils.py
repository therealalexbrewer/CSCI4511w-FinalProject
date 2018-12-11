import sys, getopt
import timeit
import time

class Utils:
    @staticmethod
    def print_title(title):
        title = "--- %s ---" % title
        print()
        print("=" * len(title))
        print(title)
        print("=" * len(title))
        print()
    @staticmethod
    def print_elapsed_time(start):
        end = timeit.default_timer()
        seconds = end - start
        hours, rem = divmod(seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        print("Elapsed time: {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

    # @staticmethod
    # def printElapsedTime(start):
    #     end = timeit.default_timer()
    #     elapsed_time = end - start

    @staticmethod
    def solveProblem(title, problem, algorithm):
        Utils.print_title(title)
        start = timeit.default_timer()
        algorithm.solve(problem)
        Utils.print_elapsed_time(start)

        algorithm.print_solution()
        algorithm.print_stats()

    # @staticmethod
    # def loadArgv():
    #     try:
    #         opts, args = getopt.getopt(sys.argv,"hi:o:",["ifile=","ofile="])
    #     except getopt.GetoptError:
    #         print ('test.py -i <inputfile> -o <outputfile>')
    #         sys.exit(2)
    #     for opt, arg in opts:
    #         if opt == '-h':
    #             print ('test.py -i <inputfile> -o <outputfile>')
    #             sys.exit()
    #         elif opt in ("-i", "--ifile"):
    #             inputfile = arg
    #         elif opt in ("-o", "--ofile"):
    #             outputfile = arg