maneras = 0


def backtrack(pos, escalones):

    if pos >= escalones:
        print("maneras +1")
        global maneras
        maneras +=1

        return

    else:
        
        for i in range(1,4):
            print("else",i)
            if pos+i > escalones:
                break
            backtrack(pos+i,escalones)





def david(escalones):


    backtrack(0,escalones)

    return maneras



if __name__ == "__main__":
    print(david(3))
