# import os
# path = os.path.join('user','bin','spam')
# print(path)
#
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\User\\asweighgard', filename))




# hellofile = open('/home/zyz/python/PyChild/regex.py')
# helloreadfile = hellofile.read()
# print(helloreadfile)

# ?
# testfile = open('write_add_test.txt', 'w')
# testfile.write('hello_world')
# testfile.close
# content = testfile.read()
# testfile.close
# testfile.open('write_add_test.txt', 'a')
# testfile.write('Bacon is not a vegetable')
# testfile.close
# testfile = open('write_add_test.txt')
# content = testfile.read()
# print(content)


import shelve
shelffile = shelve.open('shelftest')

