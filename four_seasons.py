"""
I highly recommend listening Vivaldi's Four Seasons as an inspiration to solve this Kata :)

In the UK,
winter begins on 21 December and ends on 20 March. 
Spring begins on 21 March and ends on 20 June.
Summer begins on 21 June and ends on 20 September.
Autumn begins on 21 September and ends on 20 December.

Given a date day from 1 (January 1st) to 365 (December 31th) your task is to return the season of the year that corresponds to that day.
If the number given is greater than 365, return "The year flew by!".

Note: We are not considering leap years.

"""

def four_seasons(d):
    if d > 365:
        return "The year flew by!"
    if d > 79 and d < 172:
        return "Spring Season"
    if d >171 and d< 264:
        return "Summer Season"
    if d>263 and d< 355:
        return "Autumn Season"
    else:
        return "Winter Season"
    

if __name__ =="__main__":
    print(four_seasons(171))