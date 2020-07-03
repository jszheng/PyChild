class Animal(object):
    def run(self):
        print('Animal is running!')


class Dogs(Animal):
    def run(self):
        print('Dogs are running!')


class Husky(Dogs):
    pass


class Cats(Animal):
    def run(self):
        print('Cats are running!')


print('====================Test====================')

dog = Dogs()
dog.run()

cat = Cats()
cat.run()

print(isinstance(dog, Animal))
print(isinstance(dog, Dogs))

print('====================continue====================')


def run_twice(animal):
    animal.run()
    animal.run()


print('====================Test====================')

d = Dogs()
c = Cats()
h = Husky()

print(isinstance(h, Dogs))
# print(dir(h))

print('====================continue====================')

