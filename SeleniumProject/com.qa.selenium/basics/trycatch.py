try:
    with open('files.txt', 'r') as reader:
        reader.read()
except:
    print("some how i reached this block there is failure in try block")

finally:
    print("cleaning in progress")
