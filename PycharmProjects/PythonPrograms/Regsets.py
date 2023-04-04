import re

txt = "The rain in spain"
# print(re.findall("[arm]", txt))
# print(re.findall("[a-zA-Z]", txt))

x = re.search("ai", txt)
print(x)

print(re.split("\s", txt,3))

print(re.sub("i", "9", txt, 2))

# search,find,split,sub


