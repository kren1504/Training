"""
The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your function although you will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling period).

Examples:

3 needs to become $3.00

3.1 needs to become $3.10


"""

def format_money(num):
    num = str(num)
    division = num.split(".")
    if len(division) == 1:
        return "$"+num+".00"
    elif len(division[1]) == 1:
        return "$"+num+"0"
    else:
        return "$"+division[0]+"."+division[1][:2]
    

if __name__ == "__main__":
    print(format_money(44444444443.44))