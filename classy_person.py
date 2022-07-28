'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    age = 0
    name = ''

    def __init__(self,nam, ag):
        self.name = nam
        self.age = ag
        #print(f"{self.name}, age {self.age}: Constructed!")

    def increase_age(self):
        self.age += 1

    def say_greeting(self):
        print(f"Hello world! My name is {self.name}!")

    def count_to_age(self):
        n = 0
        while n < self.age:
            n += 1
            print(n)

'''
nathan = Person('Nathan',32)
print(nathan.age)
nathan.say_greeting()
nathan.increase_age()
print(nathan.age)
nathan.count_to_age()
'''

# You won't need to call anything here.