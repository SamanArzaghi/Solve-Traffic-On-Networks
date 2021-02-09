def check(exampleGraph,startPoint,endPoint):
    global currentPath
    global final
    global string
    if bool(currentPath) == False:
        currentPath.append(startPoint)
        for p in exampleGraph:
            if p[0] == currentPath[-1]:
                if p[1] not in currentPath:
                    currentPath.append(p[1])

                    if p[1] == endPoint:
                        for i in currentPath:
                            string += str(i)

                        final.append(string)
                        string = ''
                        currentPath.pop()

                    else:
                        check(exampleGraph,startPoint,endPoint)
                        currentPath.pop()


    else:
        for p in exampleGraph:
            if p[0] == currentPath[-1]:
                if p[1] not in currentPath:
                    currentPath.append(p[1])


                    if currentPath[-1] == endPoint:
                        for i in currentPath:
                            string += str(i)

                        final.append(string)
                        string = ''
                        currentPath.pop()

                    else:
                        check(exampleGraph,startPoint,endPoint)
                        currentPath.pop()


def finalCheck(exampleGraph,startPoint,endPoint):
    global finalfinal
    global currentPath
    global final
    global string
    finalfinal = []
    final = []
    currentPath = []
    string = ''

    check(exampleGraph,startPoint,endPoint)
    for p in range(len(final)):
        pastPoint = final[p][0]
        currentRoad = ''
        finalfinal.append([])
        for i in range(1,len(final[p])):
            currentRoad =  pastPoint + final[p][i]
            pastPoint = final[p][i]
            finalfinal[p].append(currentRoad)

    return finalfinal


#~~~~~~~~~~~~~~~~~~~~~~~~~let's see how it works~~~~~~~~~~~~~~~~~~~~~#       
# exampleGraph = ['ae','ab','ac','ad','cd','db','cb']   
# print(finalCheck(exampleGraph,'a','b'))
#
# outPut ---> [['ab'], ['ac', 'cd', 'db'], ['ac', 'cb'], ['ad', 'db']]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#