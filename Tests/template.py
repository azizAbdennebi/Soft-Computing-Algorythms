import time
import sys

# setting path
sys.path.append('Approximation_methods\\Single_solution_algorithms')

from simulated_annealing import simulated_annealing_method
from glouton_search import glouton_search_method
from tabu_search import tabu_search_method


class Team1:
    def __init__(self):
        self.name = "Team 1"
        self.solvingMethods = ["simulated_annealing","glouton_search","tabu_search"] # List of methods that are exactly the name of the methods used

    def simulated_annealing(self, numberOfElements, listOfElements , backPackSize):
        return simulated_annealing_method(numberOfElements, listOfElements , backPackSize)

    def glouton_search(self, numberOfElements, listOfElements , backPackSize):
        return glouton_search_method(numberOfElements, listOfElements , backPackSize)

    def tabu_search(self, numberOfElements, listOfElements , backPackSize):
        return tabu_search_method(numberOfElements, listOfElements , backPackSize)
    
    # Don't forget to add any new methods name to the solvingMethods list above
    # Edit only team 1, and the program will automatically compare the results of both teams and all the methods used by each team

class Team2:
    def __init__(self):
        self.name = "Team 2"
        self.solvingMethods = ["bruteForce"] 
    
    def bruteForce(self, numberOfElements, listOfElements , backPackSize):
      # brute force knapsack 0/1
      maxi = 0
      answer = ''
      for i in range(2**numberOfElements):
        weight = 0
        value = 0
        for j in range(numberOfElements):
          if i & (1 << j):
            weight += listOfElements[j][1]
            value += listOfElements[j][0]
        if weight <= backPackSize:
          if value > maxi:
            maxi = value
            answer = i 
      answer = bin(answer)[2:].zfill(numberOfElements)
      return [maxi, answer]




# Don't change anything below this line unless you know what you are doing
# This is the main function that will run the program

if __name__ == "__main__":
    # this is the input data, you can change it to test your code with different inputs
    f= open("Tests\\f1_l-d_kp_10_269","r")
    numberOfElements, backPackSize = map(int, f.readline().split())
    listOfElements = []
    for i in range(numberOfElements):
        listOfElements.append(list(map(int, f.readline().split())))
    f.close()

    team1 = Team1()
    team2 = Team2()
    for method in team1.solvingMethods:
        start = time.time()
        print(team1.name, method)
        print(getattr(team1, method)(numberOfElements, listOfElements, backPackSize))
        print("Time taken:",time.time() - start, "\n")
    print()
    for method in team2.solvingMethods:
        start = time.time()
        print(team2.name, method)
        print(getattr(team2, method)(numberOfElements, listOfElements, backPackSize))
        print("Time taken:",time.time() - start, "\n")