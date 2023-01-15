def glouton_search_method(numberOfElements, listOfElements , backPackSize):
    


    items = sorted(listOfElements, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    total_weight = 0
    result=list()
    taken = [0] * len(items)
    for i in range(len(items)):
        if total_weight + items[i][1] <= backPackSize:
            taken[listOfElements.index(items[i])] = 1
            total_weight += items[i][1]
            total_value += items[i][0]
    result.append(total_value)
    result.append("".join(str(i) for i in taken))
    return(result)
    print (total_value, total_weight, taken)

# items = [(60, 20), (100, 50), (120, 30)]
# max_weight = 50

# print (glouton_search_method(2,items, max_weight))
#Test
#glouton_search_method(4,[[8,5],[11,7],[6,4],[4,3]],14)
#glouton_search_method(3,[[3,4],[4,1],[6,5]],8)
#glouton_search_method(5,[[2,1],[5,4],[3,2],[1,5],[6,7]],17)



        
                   
                   





