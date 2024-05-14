# Online Python compiler (interpreter) to run Python online.

def printInformation(location):
    print("Location " + location + " is Dirty.")
    print("Cost for Cleaning " + location + ": 1")
    print("Location " + location + " has been Cleaned.\n")

def vacuumCleaner(goalState, currentState, location):
    print("Goal State Required:", goalState, '\n')
    print("Vacuum is placed in Location " + location)

    totalCost = 0

    while (currentState != goalState):
        if (location == "A"):
            # cleaning
            if (currentState["A"] == 1):
                currentState["A"] = 0
                totalCost += 1
                printInformation("A")
            # moving
            if (currentState["B"] == 1):
                print("Moving right to the location B.\nCost for moving RIGHT: 1")
                location = "B"
                totalCost += 1

        elif (location == "B"):
            # cleaning
            if (currentState["B"] == 1):
                currentState["B"] = 0
                totalCost += 1
                printInformation("B")
            # moving
            if (currentState["A"] == 1):
                print("Moving left to the location A.\nCost for moving LEFT: 1")
                location = "A"
                totalCost += 1
       
    print("GOAL STATE:", currentState)
    return totalCost

goalState = {"A": 0, "B": 0}
currentState = {"A": -1, "B": -1}

location = input("Enter Location of Vacuum (A/B): ")
currentState["A"] = int(input("Enter status of A (0/1): "))
currentState["B"] = int(input("Enter status of B (0/1): "))

# calling function
totalCost = vacuumCleaner(goalState, currentState, location)
print("Performance (Total Cost) :", totalCost)

