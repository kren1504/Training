def maximumToys(prices, k):

    budget = k
    prices.sort()
    contador = 0
    print(prices)

    for price in prices:
        if budget >= price:
            budget -= price
            contador +=1
            continue
        if price > budget:
            break

    return contador

        

        
def recursivo( pos,prices, budget):

    if budget <=0 or pos == 0:
        return 0

    if prices[pos-1] > budget:
        return recursivo(budget)

    




if __name__ == "__main__":
    print(maximumToys([1,12, 5, 111, 200, 1000, 10],50))