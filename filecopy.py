file = open('test.txt')
s = file.read()
file.close()
file = open('test2.txt', 'w')
file.write(s)
file.close()