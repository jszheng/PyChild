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

# import os
# filesize = 0
# for file in os.listdir('D:\\Python\\PyChild'):
#     filesize = filesize + os.path.getsize(os.path.join('D:\\Python\\PyChild', file))
# print(filesize)


#


# readfile = open('D:\\Python\\PyChild\\regex.py')
# print(readfile)
#
# # regexcontent = readfile.readlines()
# # print(regexcontent)
#
# regexcontent = readregex.read()


# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))
# fileobj = open('mycats.py', 'w')
# fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileobj.close()
# readobj = open('mycats.py')
# content = readobj.read()
# print(content)


import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoneix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indianapolis': 'Iowa', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
                'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dekota': 'Bismarck', 'Ohio': 'Colunbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhose Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
                'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(4):
    quizfile = open('testfile%s.txt' % (quiznum + 1), 'w')
    answerfile = open('quiz_answer%s.txt' % (quiznum + 1), 'w')

    # step 1: title
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz(form%s)' % (quiznum + 1))
    quizfile.write('\n\n')

    # setp 2: random choose states
    State = list(capitals.keys())
    random.shuffle(State)

    for questionnum in range(50):
        correctanswer = capitals[State[questionnum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroption = wronganswer + [correctanswer]
        random.shuffle(answeroption)

        quizfile.write('%s. What is the capital of %s?\n' % (questionnum + 1, State[questionnum]))
        for i in range(4):
            quizfile.write(' %s. %s\n' % ('ABCD'[i], answeroption[i]))
        quizfile.write('\n')

        answerfile.write(' %s. %s\n' % (questionnum + 1, 'ABCD'[answeroption.index(correctanswer)]))

    quizfile.close()
    answerfile.close()
