
# read the file and store all the lines in list
# reverse the list
# write the reversed list back to the file

with open('test.txt', 'r') as reader:
    
    input = reader.readlines() # get the file data here
    input = input[::-1]
    with open('test.txt', 'w') as file:
        
        for data in input:
            file.write(data)

