

with open('pi_digits.txt', 'w+') as file_object:
    file_object.write('test content') #write content
    file_object.seek(0)
    #reset line index to the beginning for reading
    contents = file_object.read()  #read the content
    file_object.close()
print(contents)


