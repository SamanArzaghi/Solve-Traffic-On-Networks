import itertools
from subGraphs import powerSet

def theNashEquilibrum(mainGraph, startNode, finalNode, averageDrivers, currentGraph, listOfPaths, driversInPaths) :
    
    # make copy of mainGraph
    mainGraphCopy = mainGraph.copy()

    # pop those eadge which not contain paths
    for i in currentGraph[:] :
        if i not in list(itertools.chain(*listOfPaths)) :
            currentGraph.remove(i)

    # pop thoses edge which not exist in currentGraph
    for key in list(mainGraphCopy) :
        if key not in currentGraph :
            mainGraphCopy.pop(key)
    
    # creat a dictionary for drivers in each edge
    driversInEdges = {}
    for key,Value in driversInPaths.items() :
        for ii in key :
            try :
                driversInEdges[ii] += Value
            except :
                driversInEdges[ii] = Value

    # time it takes to pass eache path
    timeOfPaths = {}
    for iii in listOfPaths :
        timeOfPaths[tuple(iii)] = 0
        for iv in iii :
            timeOfPaths[tuple(iii)] += mainGraphCopy[iv][0]*driversInEdges[iv] + mainGraphCopy[iv][1]

    # times it takes to pass each edge
    timeOfEdges = {}
    for key,value in mainGraphCopy.items() :
        timeOfEdges[key] = value[0]*driversInEdges[key] + value[1]
    
    # calculate the best path and its time
    bestTime = float("inf")
    bestPath = list(timeOfPaths.values())[0]
    for key, value in timeOfPaths.items() :
        if value == bestTime and len(bestPath) > len(key) :
            bestPath = key
        if value < bestTime :
            bestTime = value
            bestPath = key

    # find the most time it takes to pass from startNode to finalNode
    timeOfPaths = dict(sorted(timeOfPaths.items(), key=lambda item: item[1]))
    biggestKey = tuple(list(timeOfPaths.keys())[-1])
    biggestValue = list(timeOfPaths.values())[-1]

    # check if there is a worse path than bestpath
    if biggestValue > bestTime and driversInPaths[biggestKey] > 1 :

        # coefficient of change
        descent = averageDrivers//100

        # move a driver to the better path
        driversInPaths[biggestKey] -= descent
        driversInPaths[bestPath] += descent

        # repeat again 
        return theNashEquilibrum(mainGraphCopy, startNode, finalNode, averageDrivers, currentGraph, listOfPaths, driversInPaths)
                
    # so now we are in nash equilibrium
    else:
        # calculate the average time it takes for each driver to travel from startNode to finalNode
        socialCost = 0
        for key,value in driversInPaths.items() :
            if value > 0 :
                socialCost += timeOfPaths[key]*value
        averageTravelTimeForThisPath = socialCost/averageDrivers
        return (averageTravelTimeForThisPath, driversInEdges)


#~~~~~~~~~~~~~~~~~~~~~~~~~let's see how it works~~~~~~~~~~~~~~~~~~~~~#     
# from subGraphs import powerSet
# from checkConection import finalCheck  
# mainGraphCopy = {"ac":[1/100,0], "cb":[0,45], "ad":[0,45], "db":[1/100,0], "cd":[0,0]}
# startNode = "a"
# finalNode = "b"
# averageDrivers = 4000
# currentGraph = ["ac", "cb", "ad", "db", "cd"]
# mainGraphEdges = []
# for i in mainGraphCopy :
#     mainGraphEdges.append(i)
# allSubgraphs = powerSet(mainGraphEdges)
# listOfPaths = finalCheck(currentGraph, startNode, finalNode)        
# driverInWays = {}
# for i in listOfPaths :
#     driverInWays[tuple(i)] = 0
# driverInWays[list(driverInWays.keys())[0]] = averageDrivers 
# print(theNashEquilibrum(mainGraphCopy, startNode, finalNode, averageDrivers, currentGraph, listOfPaths, driverInWays))
#
#
# outPut ---> [80.0, {'ac': 4000, 'cb': 0, 'cd': 4000, 'db': 4000, 'ad': 0}]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
