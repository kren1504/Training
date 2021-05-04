def minTime(machines, goal):
    cantItems = 0
    daysRequired = 0
    i = 0
    day = 1

    machines.sort()

    while cantItems < goal:

        for time in machines:
            
            if day % time == 0:
                cantItems += 1

            if cantItems == goal:
                return day




        day +=1




if __name__ == "__main__":
    print(minTime([1,3,4],10))