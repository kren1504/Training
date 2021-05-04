def sort(arr):

    for i in range(len(arr)):

        for j in range(i,len(arr)):

            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]



    return arr





if __name__ == "__main__":
    print(sort([1,8,4,9,0]))
