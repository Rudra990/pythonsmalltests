class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f'Hello, {self.name}'
p = Person('Bob')
print(p.greet())