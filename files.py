test_file = open("test.txt" , 'a')

test_file.write("\n")
test_file.write('Wlasnie dodajesz jeszcze druga linijke')

test_file.close()


test_file = open("test.txt" , 'r')
print(test_file.read())

