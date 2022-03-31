
def calculate_number(first):
    total = 10
    if first % 2 == 0:
        # %2表示除以2取餘數; ==表示數值相等
        #if 是函數，所以後面假設完要加冒號告訴系統這是函數
        total += first
        # 表示total=total +first 
        print (total)
        
def app_log(name,func_id):
    print(f"{name} use the {func_id}")
    #函數裡的的參數，可以藉由執行自行做更換
    
def app_log(name,func_id,date="2022/03/29"):
    print(f"{name} use the {func_id} on {date}")
    #一開始參數設定時，我們可以先設一個數值。如果後面使用這個參數時，沒有特別指定，系統就會使用預設值