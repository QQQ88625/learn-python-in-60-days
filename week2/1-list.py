#可以藉由x[]來呼叫list相對應的字元
x = [10,100,1000]
print(x[0])
print(x[1])
print(x[2])

#list[]可以是int，string，flaot
#索引數值為正數，通常是由左到右去找。索引值為負值，就是從右到左呼叫，
x = ["紀", 1.5 , 1122,-1]
print(x[0])
print(x[1])
print(x[2])
print(x[-1])

# .append為list底下function。可以透過此來增加list裡字元
# len為計算長度函數
x = [10,100,1000]
x.append((1))
print(x,x[3],len(x))

#del則是可以刪除指定字元的元素
del x[2]
print(x,x[2],len(x))


x = ["紀", 1.5 , 1122]
del(x[2])
print(x,x[1],len(x))