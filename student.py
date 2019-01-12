class Student:
    school = "Shivaji University"

    def __init__(self, m1, m2, m3):  # initialize variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # Accessor: only fetching the values
        return self.m1

    def set_m1(self, value):  # Mutator: modify the values
        self.m1 = value

    @classmethod
    def getschool(cls):  # class method
        return cls.school

    @staticmethod
    def info():  # static method
        print("This is Student class")

    def compare(self, s2):
        if self.m1 == s2.m1 and self.m2 == s2.m2 and self.m3 == s2.m3:
            return True
        else:
            return False


s1 = Student(34, 65, 23)  # Constructor
s2 = Student(45, 46, 87)
s3 = Student(45, 46, 87)


if s2.compare(s3):
    print("Both s2 and s3 are same")
else:
    print("Both s2 and s3 are different")

print(s1.avg())
print(s2.avg())

print(Student.getschool())
Student.info()
