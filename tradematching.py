
# create lists for buy and sell side of trading book
buyBook = []
sellBook = []


# function to add an order to a trading book, either on the buy side or the sell side
#automatically keeps the lsit sorted.

def addOrder(type, amount, price):
    item = [amount,price]
    if type == "B":
        buyBook.append(item)
        buyBook.sort(key=lambda x: x[1], reverse=True)
    elif type == "S":
        sellBook.append(item)
        sellBook.sort(key=lambda x: x[1])
    else:
        print("Invalid order type, use B for buy orders, and S for sell orders.")

addOrder("S",8880,1205)
addOrder("S",2000,1205)
addOrder("S",4300,1205)
addOrder("S",5400,1206)
addOrder("S",1700,1208)
addOrder("B",4200,1204)
addOrder("B",5000,1203)
addOrder("B",8000,1202)
addOrder("B",1200,1202)
addOrder("B",1700,1199)
        



#buy order: at market best.
def buy_atMarket (buy_amount):
    while buy_amount!= 0:
        if buy_amount >= sellBook[0][0]: # amount to buy is greater than/equal to whats in the first order, so buy all of it remove it from the book and continue.
            print(f"{sellBook[0][0]} bought at {sellBook[0][1]}")
            buy_amount -= sellBook[0][0]
            del sellBook[0]
        if buy_amount != 0 and buy_amount < sellBook[0][0]:
            print(f"{buy_amount} bought at {sellBook[0][1]}")
            sellBook[0][0] -= buy_amount
            buy_amount -= buy_amount
    print ("Order executed")


#buy order: at market best.
def sell_atMarket (sell_amount):
    while sell_amount!= 0:
        if sell_amount >= buyBook[0][0]: # amount to sell is greater than/equal to whats in the first order, so sell all of it remove it from the book and continue.
            print(f"{buyBook[0][0]} sold at {buyBook[0][1]}")
            sell_amount -= buyBook[0][0]
            del buyBook[0]
        if sell_amount != 0 and sell_amount < buyBook[0][0]:
            print(f"{sell_amount} sold at {buyBook[0][1]}")
            buyBook[0][0] -= sell_amount
            sell_amount -= sell_amount
    print ("Order executed")
            

            
        


'''
#buy order: at market bests.
def sell_atMarket (sell_amount):
    amount_sold = 0
    starting_amount = sell_amount
    while sell_amount != 0 : # while there is still stuff left to buy]
        while sell_amount > buyBook[0][0]:
         if sell_price <= buyBook[0][1]: # if the most desperate buyers are willing ot pay equal or more than my limit, and i have to buy more than whats being sold, buy all of it
            delta = buyBook[0][0]
            sell_amount-= delta# increase you bought everything that was bought and you still need more
            amount_sold +=delta
            buyBook.remove(buyBook[0])# we've fulfilled this whole buy order, so remove it form the top of the boosk
         elif sell_price<= buyBook[0][1] and sell_amount <= buyBook[0][0] :
             delta = sell_amount
             buyBook[0][0] -= delta
             print("most desperate buyer is offering too little money, order executed")
             print (f"{amount_sold} sold at {sell_price} and {starting_amount-amount_sold} was unfilled.")

             break
             
          
'''



sell_atMarket(11000)
print(buyBook)



    







   

