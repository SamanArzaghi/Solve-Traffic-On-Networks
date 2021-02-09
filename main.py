from subGraphs import powerSet
from checkConection import finalCheck
from findTheNash import theNashEquilibrum

def findTheBestStructure(mainGraph, startNode, finalNode, averageDrivers):
    
    # creat a dictionary for every sub estimate time in nash equilibrium and another decionary for density of edges in nash
    timeForSubgraphs = {}
    densiyForSubgraphs = {}
    
    # creat a list of all subgraphs
    mainGraphEdges = []
    for i in mainGraph :
        mainGraphEdges.append(i)
    allSubgraphs = powerSet(mainGraphEdges)

    # find all subgraphs best time
    for ii in allSubgraphs :

        # check if there is a way from start node to the final node
        listOfPaths = finalCheck(ii, startNode, finalNode)        
        if listOfPaths :
            currentGraph = ii

            # creat a dictionary of paths and drivers in it
            driversInPaths = {}
            for iii in listOfPaths :
                driversInPaths[tuple(iii)] = 0

            # choose a optional way for all drivers
            driversInPaths[list(driversInPaths.keys())[0]] = averageDrivers

            # find the average time it takes for all  players to travel from startNode to finalNode and density of edges
            averageTimeAndDensityOfEdges = theNashEquilibrum(mainGraph, startNode, finalNode, averageDrivers, currentGraph, listOfPaths, driversInPaths)
            timeForSubgraphs[tuple(ii)] = averageTimeAndDensityOfEdges[0]
            densiyForSubgraphs[tuple(ii)] = averageTimeAndDensityOfEdges[1]   

    # sorted timeForSubgraphs to find the minimum
    sortedTimeForSubgraphs = dict(sorted(timeForSubgraphs.items(), key=lambda item: item[1]))

    # print the best subgraph and the nash equilibrium for it
    bestSubgraph = list(sortedTimeForSubgraphs.keys())[0]
    timeOfBestSubgraph = list(sortedTimeForSubgraphs.values())[0]
    nashOfBestSubgraph = densiyForSubgraphs[bestSubgraph]
    print(f"best subgraph for solving traffic is {bestSubgraph}.")
    print(f"the average tie it takes for eaach driver is {timeOfBestSubgraph}.")
    print(f"nash equilibrium for bestSubgraph is {nashOfBestSubgraph}.")

    # if you want to see all subgraphs and its times and nash equilibruim for each one use the code below
    #print(timeForSubgraphs)   
    #print(densiyForSubgraphs)  
 
 
#~~~~~~~~~~~~~~~~~~~~~~~~~let's see how it works~~~~~~~~~~~~~~~~~~~~~#       
# mainGraph = {"ac":[1/100,0], "cb":[0,45], "ad":[0,45], "db":[1/100,0], "cd":[0,0]}
# startNode = "a"
# finalNode = "b"
# averageDrivers = 4000
# findTheBestStructure(mainGraph, startNode, finalNode, averageDrivers)
#  
# outPut ---> best subgraph for solving traffic is ('ac', 'cb', 'ad', 'db').
#             the average tie it takes for eaach driver is 65.0.
#             nash equilibrium for bestSubgraph is {'ac': 2000, 'cb': 2000, 'ad': 2000, 'db': 2000}.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#







        




