
import time


def minimumAbsoluteDifference(arr):
    minimun = 1000000001

    arr.sort()


    for j in range(len(arr)-1):
            

        if abs(arr[j] - arr[j+1]) < minimun:
            minimun = abs(arr[j] - arr[j+1])
                
        if minimun == 0:
            break

    return minimun

            



if __name__ == "__main__":
    start = time.time()
    print(minimumAbsoluteDifference([-59, -36, -13, 1 ,-53, -92, -2, -96, -54, 75]))    
    end = time.time()

    # total time taken
    print(f"Runtime of the program is {end - start}")
