def reverse_words(s):
    
    s = s.split(" ")
    s=s[::-1]
    
    return " ".join(s)

if __name__ =="__main__":
    print(reverse_words("The greatest victory is that which requires no battle"))