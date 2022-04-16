def cal_money(x=50):
    out_money = 1000 - x
    # [0] * 6 is a syntax sugar
    # [0] * 6 would convert to [0, 0, 0, 0, 0, 0]
    answer = [0] * 6
    order  = [500, 100, 50, 10, 5, 1]

    answerStr = ""
    for index in range(len(order)):
        # // means divide without remainder
        answer[index] = out_money // order[index]
        out_money = out_money % order[index]
        if index != 5 and answer[index] != 0:
            answerStr += "{}, {}; ".format(order[index], answer[index])
        elif answer[index] != 0:  
            answerStr += "{}, {}".format(order[index], answer[index])
    print(answerStr)
cal_money(286)
cal_money(100)
cal_money(1)
cal_money(841)
cal_money(999)
cal_money(413)



