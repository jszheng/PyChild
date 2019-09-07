'''class number:
    def __init__(self, second, third):
        self.r = second
        self.i = third + second


s = number(3, 5)
print(s.r, s.i)'''



'''class test:
    def prt(self):
        print(self)
        print(self.__class__)

T = test()
print(T.prt)'''


class people:
    name = ''
    age = 0
    _weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self._weight = w

    def speak(self):
        print('%s says: I am %s years old' % (self.name, self.age))


i = people('Mike', 15, 127)
i.speak()


class Student:
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print('%s says: I am %s years old and I am in grade %s' % (self.name, self.age, self.grade))


s = Student('Ken', 14, 121, 9)
s.speak()


class Speaker:
    name = ''
    topic = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speech(self):
        print('My name is %s, my topic today is %s' % (self.name, self.topic))


t = Speaker('Sam', 'Environment')
t.speech()


class sample:
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = sample('Tim', 20, 150, 4, 'python')
test.speak()
