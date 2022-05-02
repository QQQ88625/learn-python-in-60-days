x = "hello"
result = x.split("e")

print(result)


print("e".join(result))


y = """Mary,10,100,1000
Eric,1000,100,10"""
result = y.split("\n")
print(result)

for line in result:
    line = line. (",")
    print(line)
    line = ",".join(line)
    print(line, type(line))