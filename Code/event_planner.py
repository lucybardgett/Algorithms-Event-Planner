from Input import inputData
from Dynamic import dynamicFunction
from BruteForce import BruteForce
import time

file = "input_medium.txt" 
extFile = "Input_Files/" + file
with open(extFile) as f: # Read file and store in a list
        i = 0
        data = []
        while i <= 1:
            for line in f:
                data.append(line.rstrip())
            i += 1

f.close()
cons = data[1].split(" ")
totalHours, totalBudget = int(cons[0]), int(cons[1])


dynaActs, dynaHours, dynaCost, dynaEnjoy, dynaExec = dynamicFunction(extFile)
bruteActs, bruteHours, bruteCost, bruteEnjoy, bruteExec = BruteForce(extFile)

print("========================================\nEVENT PLANNER - RESULTS\n========================================")

print("\nInput File:", file)
print("Available Time:", totalHours, "hours")
print("Available Budget: £" + str(totalBudget))

#Brute Force Algorithm output section
print("\n--- BRUTE FORCE ALGORITHM ---")
print("Selected Activities:")
print(bruteActs)
for act in bruteActs:
    print(" - " + act)

print("\nTotal Enjoyment:", bruteEnjoy)
print("Total Time Used:", bruteHours, "hours")
print("Total Cost: £" + str(bruteCost))

print("\nExecution Time:", bruteExec, "seconds")

#Dynamic Algorithm output section
print("\n--- DYNAMIC PROGRAMMING ALGORITHM ---")
print("Selected Activities:")
for act in dynaActs:
    print(" - " + act)

print("\nTotal Enjoyment:", dynaEnjoy)
print("Total Time Used:", dynaHours, "hours")
print("Total Cost: £" + str(dynaCost))

print("\nExecution Time:", dynaExec, "seconds")
