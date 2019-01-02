# coding:utf-8
from six import add_metaclass


class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)
        return super(MyMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)
        super(MyMeta, cls).__init__(name, bases, dct)


@add_metaclass(MyMeta)
class MyClass:
    __metaclass__ = MyMeta

    def foo(self, param):
        pass


instance1 = MyClass()
instance2 = MyClass()
print('-----------------------------------')
print(instance1)
print(instance2)