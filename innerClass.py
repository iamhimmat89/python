class Student:

    def __init__(self, m1, m2, m3, grp1, grp2):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.grpsub = self.groupSubject(grp1, grp2)

    def avg(self):
        print("Group Subject Avg: " + str(self.grpsub.avg()))
        return (self.m1 + self.m2 + self.m3) / 3

    class groupSubject:

        def __init__(self, grp1, grp2):
            self.grp1 = grp1
            self.grp2 = grp2

        def avg(self):
            return (self.grp1 + self.grp2) / 2


s1 = Student(34, 65, 23, 50, 40)
print("m1, m2, m3 Avg: " + str(s1.avg()))

print(s1.grpsub.grp1)
print(s1.grpsub.grp2)
