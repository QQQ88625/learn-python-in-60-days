#單格式format用法: {} .format(value)
print("{} , A computer science portal for geeks".format("GeeksforGeeks"))

str = "this article is written in {}"
print(str.format("python"))


#多格式format用法: {} {} .format(value1,value2)
x = str()
x = str(input(x))
print("x is {}, type is {} ".format(x,type(x)))


#format(value)，括弧內的value也要加上"",讓系統知道value值也是字串
my_string = "{},is a {}  science portal for {} "
print(my_string.format(GeeksforGeeks,computer,geek))

my_string = "{},is a {}  science portal for {} "
print(my_string.format("GeeksforGeeks","computer","geek"))

my_string = "{},is a {} {} science portal for {} "
print(my_string.format("GeeksforGeeks","computer","geek"))


#format括弧內也可以使數值
print("Hi My name is {} and I am {} year old".format("Ian",28))


#我們也可以指定{}排序，在PY是由0為索引的開始數值
my_string = "{1} love {0} "
print(my_string.format("GeeksforGeeks","geek"))

my_string = "{0} love {1} "
print(my_string.format("GeeksforGeeks","geek"))