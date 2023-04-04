str = "This is Python Program Python"

sub_str = "Python"
count = 0
if (str.find(sub_str) == -1):
    print("Not Found")
else:
    print("Found")
    count += 1

print("substring {} found {} times".format(sub_str, count))
