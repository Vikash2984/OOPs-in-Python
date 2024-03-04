## Abstract class
# from abc import ABC,abstractmethod   # here ABC means Abstract Base Class
# class AbsBaseClass(ABC):
#     def __init__(self):
#         print ("Abstract class constructor...")
#     @abstractmethod
#     def abstractMethod1(self):
#         pass
#     @abstractmethod
#     def abstractMethod2(self):
#         pass
#     def concreteMethod(self):
#         print ("concreteMethod() is executing...")
# class Derived(AbsBaseClass):
#     def abstractMethod1(self):
#         print ("abstractMethod1() body is redefined...")
#     def abstractMethod2(self):
#         print ("abstractMethod2() body is redefined...")
# ob1 = Derived()
# ob1.abstractMethod1()
# ob1.abstractMethod2()
# ob1.concreteMethod()

# from abc import ABC, abstractmethod
# class AbsBaseClass(ABC):
#     def __init__(self):
#         print ("Abstract class constructor...")
#     @abstractmethod
#     def my_abstract_method(self):
#         print ("Initial content of the my_abstract_method() method...")
#     def my_concrete_method(self):
#         print ("my_concrete_method() is executing...")
# class Derived(AbsBaseClass):
#     def my_abstract_method(self):
#         print ("my_abstract_method() body is overwritten...")
#         super().my_abstract_method()
# ob1 = Derived()
# ob1.my_abstract_method()
# ob1.my_concrete_method()
# from abc import ABC, abstractmethod
# class AbsBaseClass(ABC):
#     def __init__(self):
#         print ("Abstract class constructor...")
#     @abstractmethod
#     def my_abstract_method(self):
#         print ("Initial content of the my_abstract_method() method...")
#     def my_concrete_method(self):
#         print ("my_concrete_method() is executing...")
# class Derived(AbsBaseClass):
#     def my_abstract_method(self):
#         print ("my_abstract_method() body is overwritten...")
#         super().my_abstract_method()
# ob1 = Derived()
# ob1.my_abstract_method()
# ob1.my_concrete_method()
