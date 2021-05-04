"""
10 minutos


def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
        

"""

def generate_hashtag(s):
    if s == "": return False
    res=""
    s = s.strip()
    s= s.split()

    for ele in s:
        res += ele[0].upper()+ele[1:].lower()

    if (len(res)+1) > 140:
        return False
    else:
        return "#"+res 



    

if __name__ == "__main__":
    print(generate_hashtag("Hello there thanks for trying my Kata"))
