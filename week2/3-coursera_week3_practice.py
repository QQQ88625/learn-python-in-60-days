#int跟float可以互相轉換
x = 52.7
y = int(x)
print(x)
print(y)
print(type(x))
print(type(y))


#我們可以將float轉換成str，並用len計算出字串的長度
i = 52.0
s = str(i)
print(i)
print(s)
print(type(i))
print(type(s))
print(len(s))

#我們也可以用len計算list裡的字元
z = [52, 56.0 , 6.6]
w = int(z[2])
print(w)
print(len(z))

#len裡面放int，系統就不知道要怎麼處理
i = 52
a = int(i)
print(a)
print(len(a))
