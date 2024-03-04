# class Base:
#     def __init__(self):
#         print ("Base: Constructor method is executing...")
#     def displayB(self):
#         print ("Base: Display method is executing...")

# class Mid1(Base):
#     def __init__(self):
#         print ("Mid1: Constructor method is executing...")
#     def displayB(self):
#         print ("Mid1: Display method is executing...")

# class Mid2(Base):
#     # def __init__(self):
#     #     print ("Mid2: Constructor method is executing...")
#     def displayB(self):
#         print ("Mid2: Display method is executing...")


# class Derived(Mid1,Mid2):
#     def displayD1(self):
#         print ("Derived: Display method is executing...")
        


# ob1 = Derived()
# print()
# ob2 = Mid2()
# super(Derived,ob1).__init__() 


# class MyClass:
#     def __init__(self, xx, yy):
#         self.x = xx
#         self.y = yy
#     def __floordiv__(self, ob):
#         temp = MyClass(0, 0)
#         temp.x = self.x // ob.x
#         temp.y = self.y // ob.y
#         return temp
    
# ob1 = MyClass(12, 4)
# ob2 = MyClass(4, 2)
# print (ob1.x, ob1.y)
# print (ob2.x, ob2.y)
# print ("After performing the division operation...")
# result1 = ob1 // ob2
# print (result1.x, result1.y)
# result2 = ob1.__floordiv__(ob2)
# print (result2.x, result2.y)


# abstract class
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