text = '100%'

try :
    number = int(text) # 에러가 발생할 가능성이 있는 코드
# except ValueError :  # 에러 종류
except Exception as e:
    print('예외발생', e)

# https://www.daleseo.com/python-property/

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age

# person = Person("John", "Doe", 20)
# person.get_age()
# person.set_age(-1)
# person.age = person.age + 1
# person.age



class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # @property
    def full_name(self):
        return self.first_name + " " + self.last_name

person = Person("John", "Doe", 20)
print(person.full_name())