# Base class
class BaseClass:
    def markzuckerberg(self):
        print("he is facebook developer")

    def elonmusk(self):
        print("openai developer")

# Child class 1 (inherits from BaseClass)
class ChildClass1(BaseClass):
    def billgates(self):
        print("microsoft developer")

    def supercell(self):
        print("clash of clans developer")

# Child class 2 (inherits from BaseClass)
class ChildClass2(BaseClass):
    def brunomars(self):
        print("singer")

    def avamax(self):
        print("singergirl")

# Creating objects of ChildClass1 and ChildClass2 and calling methods
child1_obj = ChildClass1()
child1_obj.markzuckerberg()  # From BaseClass
child1_obj.billgates()  # From ChildClass1

child2_obj = ChildClass2()
child2_obj.brunomars()  # From BaseClass
child2_obj.avamax()  # From ChildClass2
