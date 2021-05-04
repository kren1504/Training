"""
23 minutos

def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3

"""

def dirReduc(arr):
    opposite =  [["NORTH", "SOUTH"],["EAST", "WEST"],["WEST","EAST"],["SOUTH","NORTH"]]
    i = 0
    aux = []
    while i< (len(arr)-1):
        aux.append(arr[i])
        aux.append(arr[i+1])
        if aux in opposite:
            del arr[i]
            del arr[i]
            i=0
            aux.clear()
            
            continue        
        i+=1
        aux.clear()

    return arr

if __name__ == "__main__":
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))