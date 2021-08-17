from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


def MagicList():
    lst = [0]
    return lst


def MagicList(cls_type=Person):
    lst1 = [Person, Person]
    return lst1


a = MagicList()
a[0] = 5
print(a)

a = MagicList(cls_type=Person)
a[0].age = 5
print(a)
print(str(a[0].age))

a[1].age = 7
print(a)
print(str(a[1].age))
