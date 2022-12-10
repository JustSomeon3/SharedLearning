[comment]: <Reference> (https://realpython.com/python3-object-oriented-programming/)
[comment]: <Reference> (https://www.tutorialsteacher.com/python/magic-methods-in-python)
[comment]: <Reference> (https://www.youtube.com/watch?v=rq8cL2XMM5M)

<h1 style = "text-align : center;"><b> OOP PYTHON</b></h1>

## Define Class

``` python
class Student:
    pass
```
- In line [1] Classes first letter must be in Uppercase
- In line [2] pass is used for empty functions or classes

## Function \_\_init__(self)

Once an instance of a class has been created, the function init sets the initial state of the object.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Class Attribute
A variable defined outside the init function, usually used for counters or a value that won't change its value on different instances.

```python
class Student:
    course = "mathematics"
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Instantiate
```python
class Student:
    course = "mathematics"
    def __init__(self, name, age):
        self.name = name
        self.age = age

studentOne = Student("jhon",21)
print(studentOne.name)
print(studentOne.age)
print(studentOne.course)

 Results
>> jhon
>> 21
>> mathematics
```

## Instance Methods
```python
class Student:
    course = "mathematics"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance Method
    def __str__(self):
        return f"{self.name} and his/her age is {self.age}"

studentOne = Student("jhon",21)
print(studentOne)

 Results
>> jhon and his/her age is 21
```

We can use a method 'getStudent' or ```__str__``` &larr; a **Dunder method**, this method allows us to get the same string by calling the instance of the object, so instead of ```print(student.getStudent()) we can &rarr; print(student)```

## Inheritance
```python
class Student:
    course = "mathematics"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def __str__(self):
        return f"{self.name} and his/her age is {self.age}"


class UnderGrad(Student):
    def __init__(self, name, age):
        super().__init__(name, age)

    def getInfo(self):
        return "The name of this underGraduate is: " + super().__str__()


joseph = UnderGrad('joseph', 21)
print(joseph.getInfo())

```

To access a variable from the father use ```super().variable```

## Class Method

```python
class Student:
    course = "mathematics"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_course(cls, course):
        cls.course = course

    # Instance Method
    def __str__(self):
        return f"{self.name} and his/her age is {self.age}"

print(Student.course)
Student.set_course("English")
print(Student.course)

 Results
>> mathematics
>> English
```

This Decorator allows us to work with the class. A great use is &rarr;

```python
class Employee():
    def __init__(first, last):
        ...

    @classmethod
    def from_string(cls, str):
        first, last = str.split('-')
        return cls(first, last)

text = 'jhon-doe'
new_usr = Employee.from_string(text)
```

## Static Method

```python
class Student:
    course = "mathematics"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def sum(x, y):
        return x+y
    
    # Instance Method
    def __str__(self):
        return f"{self.name} and his/her age is {self.age}"

print(Student.sum(5,2))

 Results
>> 7
```

This function can be called without the necessity of an object, so we can call it like this &rarr; ```Student.sum(var,var)```
This method does not access the instance or the class.

## Encapsulation
- **Public**: Accessible for everyone
- **Private(_)**: Only accessible from its own class
- **Protected (__)**: Only accessible from the same class and its subclasses

```python
class Student:
    course = "mathematics"
    def __init__(self, name, age, gender):
        self.name = name # public
        self._age = age # protected
        self.__gender = gender #Private
```