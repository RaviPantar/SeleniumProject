file = open('text.txt')

# with open('text.txt') as file: # alternate to file.close

with open('text.txt', 'r') as reader:
    content = reader.readlines()  # ['Ravi,'Maruti','Pantar']
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write()

