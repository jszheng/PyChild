class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def student_print(self):
        print(self.name, self.score)

    def grade(self):
        if self.score >= 90:
            print('Great!')
        elif self.score >= 60:
            print('Not bad.')
        else:
            print('Fail!')


bart = Student('Bart Simpson', 100)
bart.grade()

print('====================================================')
print('                     Pirate                         ')


class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_name_score(self):
        print(self.get_name(), self.get_score())

    def set_grade(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score!')

    def get_grade(self):
        if self.get_score() >= 90:
            print('Great!')
        elif self.get_score() >= 60:
            print('Not bad.')
        else:
            print('Fail!')


bart = Student2('Bart Simpson', 100)
bart.print_name_score()

bart.set_grade(99)
bart.print_name_score()
bart.get_grade()







