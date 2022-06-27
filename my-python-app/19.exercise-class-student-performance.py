class Student:
    def __init__(self, name, phy=0, chem=0, bio=0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return self.phy + self.chem + self.bio

    def percentage(self):
        return (self.totalObtained() / 300) * 100

student = Student("Mark", 80, 90, 40);
print(student.totalObtained())
print(student.percentage())
