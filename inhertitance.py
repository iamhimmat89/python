print("Example 1:: ")


class Parent1:
    def __init__(self):
        print("Parent1: init")

    def feature1(self):
        print("Parent1: feature 1")

    def feature2(self):
        print("Parent1: feature 2")


class Child1(Parent1):
    def __init__(self):
        super().__init__()  # Call Parent1 __init__
        print("Child1: init")

    def feature1(self):
        print("Child1: feature 1")

    def feature4(self):
        print("Child1: feature 4")


p1 = Parent1()  # Call Parent1 __init__
c1 = Child1()  # Call Child1 __init__

p1.feature1()  # Call Parent1 feature1
p1.feature2()  # Call Parent1 feature2

c1.feature1()  # Call Child1 feature1
c1.feature2()  # Call Parent1 feature2
c1.feature4()  # Call Child1 feature4


print()
print("Example 2:: ")


class Parent2:
    def __init__(self):
        print("Parent2: init")

    def feature1(self):
        print("Parent2: feature 1")

    def feature2(self):
        print("Parent2: feature 2")


class Parent3:
    def __init__(self):
        print("Parent3: init")

    def feature1(self):
        print("Parent3: feature 1")

    def feature4(self):
        print("Parent3: feature 4")


class Child2(Parent2, Parent3):
    def __init__(self):
        super().__init__()  # method resolution order. first added class
        print("Child2: init")

    def feature3(self):
        print("Child2: feature 3")


c2 = Child2()
c2.feature1()  # method resolution order. first added class
c2.feature3()

