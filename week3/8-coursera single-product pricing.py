# we want to find the price p*
# max(a - b*p)(p - c)

a = int(input("base demand = "))
b = int(input("price sensitivity = "))
c = int(input("unit cost = "))

maxprofit = 0
optimalprice = 0
for p in range(c+1, a//b):
    profit = (a - b * p)* (p - c)
    
    if profit > maxprofit:
       maxprofit = profit
       optimalprice = p
       
# Using "else: break" can stop caalculating when you find the maxprofit
       
print("optimalprice price =" + str(optimalprice))
print("maximized profit =" + str(maxprofit))