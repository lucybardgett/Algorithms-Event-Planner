from Input import inputData 
import time

def dynamicFunction(file): #Budget is max budget, enjoyment is a array of enjoyment values, costs if the related cost to enjoyment values
    
    #starts the runtime timer and runs the input handling function
    startTime = time.time()
    activities, Budget = inputData(file)
    
    n = len(activities)+1 # N is number of Activities 
    memoTable = [] # The table for memorisation 
    Budget += 1 # Convert budget to int value and add 1
    # Populate table will create a 2D array of 0s 
    for i in range(n):
        tempLine = []
        for j in range(Budget):
            tempLine.append(0)
        memoTable.append(tempLine)

    # Fill table with correct enjoyment values and costs
    for i in range (n):
        for j in range(Budget):
            # Check to see if the value is "Fake" and just needed not to cause an error 
            if i ==0 or j == 0:
                memoTable[i][j] = 0 # If so keep the value 0
            else:
                pick = 0 # instantiate pick
            
                if (int)(activities[i-1][2]) <= j: # Check to see if the activity puts you over budget for that column 
                    pick = (int)(activities[i-1][3]) + memoTable[i-1][j - (int)(activities[i-1][2])] # Pick if doesnt go over budget 
                    notPick = memoTable[i-1][j]
                    memoTable[i][j] = max(pick, notPick) # pick max out of 2 options to see if picking is better than not
    # Create a list of the actual activities that we have proven
    chosen = []
    i = n-1
    j = Budget - 1
    costCount = 0
    hoursCount = 0

    while i > 0 and j > 0: # Loop 
        if memoTable[i][j] == memoTable[i-1][j]: # If its equal to the one above that means it didn't get included so don't add to list
            i -= 1 # Decrement to look at next item in the list
        else:
            activity = activities[i-1] # if not then must have been included so add to list
            actString = str(activity[0]) + " (" + str(activity[1]) + " hours, £" + str(activity[2]) + ", enjoyment " + str(activity[3]) + ")"
            chosen.append(actString)

            cost = int(activity[2]) #takes the cost from the activity
            costCount += cost #adds it to the total cost count
            j -= cost
            i -= 1

            hours = int(activity[1])  #takes the hours from the activity
            hoursCount += hours #adds it to the total hours count

    #stops the runtime timer and formats the time to 3 decimal places
    execTime = time.time() - startTime
    execTime ="{:.4f}".format(execTime)

    # Return the activity list, total hours, total cost and total enjoyment respectively
    return chosen, hoursCount, costCount, memoTable[n-1][Budget-1], execTime