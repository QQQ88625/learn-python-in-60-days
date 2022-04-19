
c = int(input())
r = int(input())
    
  
N = int(input())
q = int(input())

list = []
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))
list.append(float(input()))

D = 0.0
profit = 0.0
exp = 0
# profit = sum( D*exp)

for i in range(0, q+1):
    exp = r * i - c * q
    if i != q:
        profit += list[i] * exp
        D += list[i]
    else:
        profit +=  (1-D)* exp

print(int(profit))
