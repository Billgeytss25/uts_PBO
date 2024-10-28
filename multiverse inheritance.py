# Base class
class BaseClass:
    def method1(self):
        print("Method 1 from BaseClass")

    def method2(self):
        print("Method 2 from BaseClass")

# Intermediate class (inherits from BaseClass)
class IntermediateClass(BaseClass):
    def method3(self):
        print("Method 3 from IntermediateClass")

    def method4(self):
        print("Method 4 from IntermediateClass")

# Derived class (inherits from IntermediateClass)
class DerivedClass(IntermediateClass):
    def method5(self):
        print("Method 5 from DerivedClass")

    def method6(self):
        print("Method 6 from DerivedClass")

# Creating an object of DerivedClass and calling methods
derived_obj = DerivedClass()
derived_obj.method1()  # From BaseClass
derived_obj.method3()  # From IntermediateClass
derived_obj.method5()  # From DerivedClass
derived_obj.method6()  # From DerivedClass
