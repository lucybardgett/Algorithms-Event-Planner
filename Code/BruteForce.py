from Input import inputData
from itertools import combinations #this was allowed in the specification
import time# needs time function to measure run time

def possibleCombos(activities):
    n = len(activities)+1
    possibleCombinations = []
    for i in range(n):
        for element in list(combinations(activities,i)):
            possibleCombinations.append(list(element))
    return possibleCombinations 
#returns a list of combinations as lists as they appear in activities

def BruteForce(file): #picks activities from possible combinations
    start_time=time.time()#start timer
    activities, budget = inputData(file)
    TotalEnjoyment=0 # the value of total enjoyment will be compared between combinations
    TotalHours = 0
    TotalCost = 0
    bestCombination=[]
    possibleCombinations = possibleCombos(activities)
    for combination in possibleCombinations:#checks each combination
        combinationsCost=0
        combinationsEnjoyment=0
        combinationsHours=0
        for activity in combination:#checks each activity in the current combination
            combinationsHours += int(activity[1])#adds the hours since hours is in the 2nd slot
            combinationsCost += int(activity[2])#adds the cost since cost is in the 3rd slot
            combinationsEnjoyment += int(activity[3])#adds the enjoyment since enjoyment value is in the 4th slot
        if combinationsCost <= budget:#checks if combination is possible with current budget
            if combinationsEnjoyment > TotalEnjoyment:#checks if current combination is better than previous best combination
                TotalEnjoyment = combinationsEnjoyment
                TotalHours = combinationsHours
                TotalCost = combinationsCost
                bestCombination = combination

    activityList = []        
    for i in bestCombination:
        actString = str(i[0]) + " (" + str(i[1]) + " hours, £" + str(i[2]) + ", enjoyment " + str(i[3]) + ")"
        activityList.append(actString)

    total_time = time.time() - start_time
    total_time ="{:.4f}".format(total_time)
    return activityList, TotalHours, TotalCost, TotalEnjoyment, total_time