
text = """name/subject, math, english, chinese, music
Peter,100,10,95,87
Mary,95,10,95,87
Lion,10,10,10,10
YunJu,100,95,95,87
Ian,100,100,100,100
Ken,100,80,95,45
"""

#import json
#json.dump()

#import json as j
#j.dump()


with open("data1.csv", "w") as f:
    f.write(text)



with open("data1.csv", "r") as f:
    content = f.read()
    print(content)
    
    content = content.split("\n")
    print(content)
    
    for line in content:
        if "name" in line or line == '':
            continue

        line = line.split(",")
        line_sum = 0
        line_average = 0
        for i in range(1, len(line)):
            line_sum += int(line[i]) 
            line_average = line_sum/(len(line)-1)
        
        print(line[0], line_sum, line_average)
print(content)
