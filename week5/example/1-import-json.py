# json is library
# for example print is function name, do not change the name
#
# import ison is nothing
# but you can give it a nickname
#
# import json as ison
# import json as ian
#
# Normally, we would "import json as j", because it is very short
#
# test.json is a filename
# you can store json format into a txt file, file extension is nothing, the content is "real"
# so you can name the file as "test.json", "test.jsonnn", "test.txt"
import json

# # create json
# content = ['1', '2', '5']
# print(content)

# with open('test1.json', 'w') as f:
#     f.write(json.dumps(content))

with open('test.jsonnn', 'r') as f:
    content = f.read()

print(content, type(content))

# # it is not available to call content[0], content[1] to get the list value
# # because it is string
# print(content[0], content[1], content[2])

# # more example
# # try to enter "['hello']"
# x = input()
# print(x[0], x[1])

# you would get the same output like the above
# [ '

# so ... how to parse the content as list? as dictionary?
# you can store data as json format

content = json.loads(content)
print(content[0], content[1])


other_str = "[10, 100, 1000]"
content = json.loads(other_str)
print(content[0], content[1])


