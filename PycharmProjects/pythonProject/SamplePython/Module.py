import re

s = "I am verY BAD 12356"
new = re.sub('[^0-9]', ' ', s)
print(new)
