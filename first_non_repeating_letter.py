def first_non_repeating_letter(string):
    
    aux = string.lower()
    for i in range(len(string)):
        if aux.count(aux[i]) == 1:
            return string[i]

    return ""



if __name__ =="__main__":
    print(first_non_repeating_letter('sTreSS'))