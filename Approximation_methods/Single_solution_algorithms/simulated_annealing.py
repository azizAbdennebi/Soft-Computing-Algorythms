import random
import math
from operator import itemgetter

# function that select the initial solution of simulated_annealing method randomly
def select_initial_solution_randomly(numberOfElements, listOfElements, backPackSize):
    solution = []

    remaining_capacity = backPackSize
    listOfElements = sorted(listOfElements,key=itemgetter(1), reverse=True)
    value = 0
    for i in range(numberOfElements):
        if listOfElements[i][1] <= remaining_capacity:
            remaining_capacity -= listOfElements[i][1]
            value += listOfElements[i][0]
            solution.append(i)

    begin_solution = ['0' for i in range(numberOfElements)]
    for i in solution:
        begin_solution[i] = '1'
    
    items_selection_string = ''.join(e for e in begin_solution)

    return [value, items_selection_string]

#Test 
#result = select_initial_solution_randomly(4, [[9,6],[11,5],[13,9],[15,7]], 20)
#print(result)

# function that create a new solution based on the initial one (perturbation)
def create_new_solution(initial_solution, listOfElements, backPackSize ):
    new_solution = list(initial_solution[1].strip())
    newValue = initial_solution[0]
    total_size = 0
    
    for i in range(len(listOfElements)):
        if initial_solution[1][i] == '1':
            total_size = total_size + listOfElements[i][1]
    while True:
        index = random.randint(0,len(listOfElements)-1)

        if new_solution[index] == '0':
            if total_size + listOfElements[index][1] > backPackSize:
                continue
            new_solution[index] = '1'
            newValue = newValue + listOfElements[index][0]
            break
        else:
            new_solution[index] = '0'
            newValue = newValue - listOfElements[index][0]
            break

    return [newValue, ''.join(e for e in new_solution)]

#Test 
#print(create_new_solution([161, '0111101001'], [[55, 95], [10, 4], [47, 60], [5, 32], [4, 23], [50, 72], [8, 80], [61, 62], [85, 65], [87, 46]], 269))

    
def simulated_annealing_method(numberOfElements, listOfElements , backPackSize):
    # Initialisation
    T = 60
    Tmin = 10
    K = 0.8
    nb_it = 5
    i = 0
    M = 10

    solution = select_initial_solution_randomly(numberOfElements, listOfElements, backPackSize)
    #print("Initial solution: ", solution, ", S_Best = ", solution, "\n")

    best_solution = solution

    while T>Tmin and i<nb_it:
        i = i + 1

        m = 0        
        while m<M:
            m = m + 1

            #Perturbation
            new_solution = create_new_solution(solution, listOfElements, backPackSize )

            #Comparison
            diff = solution[0] - new_solution[0]
            
            if (diff <= 0):
                solution = new_solution 
                if (diff < 0 and solution[0] != best_solution[0]):  
                    best_solution = solution         
            else : 
                if random.uniform(0,1) <= math.exp(-diff/T): 
                    solution = new_solution
                    if (diff < 0 and solution[0] != best_solution[0]):  
                        best_solution = solution
        
        T = T * K
    #print("Final solution: ", solution)
    return best_solution