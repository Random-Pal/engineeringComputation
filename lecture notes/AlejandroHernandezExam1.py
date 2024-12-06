currentDistance = float(input("Please provide sensor distance data: "))

robotIsRunning = True

while robotIsRunning == True: ## while loop to mimic an autonomous system.
    if currentDistance < 0.5:
        print("Danger! Stop Immediately!")
        break
    elif currentDistance >= 0.5 and currentDistance <= 2:
        print("Caution! Slow down.")
        break
    elif currentDistance > 2:
        print("Safe to proceed.")
        break