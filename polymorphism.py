class type1:

    def execute(self):
        print("type1")


class type2:

    def execute(self):
        print("type2")


class duckTyping:

    def code(self, ide):
        ide.execute()


ide = type1()
dtype = duckTyping()
dtype.code(ide)


class A:

    def show(self):
        print("in A show")


class B:

    def show(self):
        print("in B show")

a1 = B()
a1.show()

