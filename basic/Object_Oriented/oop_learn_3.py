class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @ property
    def score(self):
        return self.__score

    @ score.setter
    def score(self, value):
        pass


