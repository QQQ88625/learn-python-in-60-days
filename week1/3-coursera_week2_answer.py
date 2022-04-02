#該怎麼找錢

#如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。假設客人的消費金額 aa 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這些面額的鈔票和零錢，我們希望你能依照下面的規則找錢：
#你找的錢的總額要是 1000 - a1000−a。

#與其給客人五張 100 元，不如給他一張 500 元；與其給客人兩個 50 元，不如給他一張 100 元……依此類推。

#法一
def cal_money(x=50):
    out_money = 1000 - x
    answer = [0]*6
    order = [500,100,50,10,5,1]

    for index in range(len(order)):
        answer[index] = out_money //order[index]
        out_money = out_money % order[index]
    print(answer)
  
#法二
a = 1000
b = int ()
b = int (input("請輸入金額"))
x=a-b
print(x//500,(x%500)//100,(x%100)//50,(x%50)//10,(x%10)//5,(x%5)//1)