def inputData(file=r"input_10.txt"):
    filename = file # Change for file input

    file = [] 
    with open(filename) as f: # Read file and store in a list 
        for line in f:
            file.append(line.rstrip())

    f.close()

    # Set up basic variables in place
    numberOfActivities = file[0] # Number of activies 
    temp = file[1].split() 
    time = temp[0] # number of hours avaliable for the event
    budget = temp[1] # max budget that avaliable for the event

    # list of activites
    activityList = [] # Going to be a list of lists 
    for i in range (len(file) - 2):
        activity = (file[i+2].split())
        activityList.append(activity)

    # activityList is structured as a list of lists ->["Activity Name", time, cost, enjoymentValue]
    return activityList , int(budget)