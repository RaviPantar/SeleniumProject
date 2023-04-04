import re

s = re.findall(r"[-+]?(?:\d*\.*\d+)", "Current Level: -13.222db or 14.2 or 3")
print(s)

s1 = re.findall("\d+\.\d+", "Current Level: -13.22db or 14.2 or 3")
print(s1)

found = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,4}", "test is 127.0.0.1")
print(found)