def powerSet(s):
    # input must be a list
    totallSubSets = []
    x = len(s)
    for i in range(1 << x):
        totallSubSets.append([s[j] for j in range(x) if (i & (1 << j))])
    return totallSubSets
    
 
#~~~~~~~~~~~~~~~~~~~~~~~~~let's see how it works~~~~~~~~~~~~~~~~~~~~~#       
# print(powerSet(["ab","bc"]))   
#  
# outPut ---> [[], ['ab'], ['bc'], ['ab', 'bc']]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#