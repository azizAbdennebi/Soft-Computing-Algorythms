

import time

from recherche_taboue import recherche_taboue
from recuit_simule import recuit_simule

class Team1:
    def __init__(self):
        self.name = "Team 1"
        self.solvingMethods = ["Recherche_Taboue","Recuit_Simule"] # List of methods that are exactly the name of the methods used
    
    def Recherche_Taboue(self, numberOfElements, listOfElements , backPackSize):
      # Your code here
      # Return the solution as a list of the optimal value and a string of "0"s and "1"s representing the items that are in the backpack
      # Example: [10, "010101"]
      # Check the example below
      return(recherche_taboue(numberOfElements, listOfElements , backPackSize))


    def Recuit_Simule(self, numberOfElements, listOfElements , backPackSize):
      return(recuit_simule(numberOfElements, listOfElements , backPackSize))
      

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
    f= open("f1_l-d_kp_10_269","r")
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
        print("Time taken:",time.time() - start)
    print()
    for method in team2.solvingMethods:
        start = time.time()
        print(team2.name, method)
        print(getattr(team2, method)(numberOfElements, listOfElements, backPackSize))
        print("Time taken:",time.time() - start)

