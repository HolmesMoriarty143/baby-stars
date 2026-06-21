#Student Report Card
class Student():
    def __init__(self):
        self.name = input("Enter Your Name               : ")
        self.age = int(input("Enter Your Age                : "))
        self.reg_no = input("Enter Your Register number    : ")
        self.gender = input("Enter Your Gender (M/F/T)     : ")
        self.is_hosteller = input("Hosteller? (Y/N)              : ")
student=Student()

def get_mark(subject):
    mark = float(input(f"Enter your marks in {subject}: "))
    while mark < 0 or mark > 100:
        print("Invalid marks. Try again.")
        mark = float(input(f"Enter your marks in {subject}: "))
    return mark


class Subjects():
    def __init__(self):
        self.course = input("Enter Your Course (CSE/IT/ME/CE/EEE/ECE): ")

        while self.course not in ["CSE","IT","ME","CE","EEE","ECE"]:
            print("Invalid Choice")
            self.course = input("Enter Your Course (CSE/IT/ME/CE/EEE/ECE): ")

        if self.course == "CSE":
            self.s1 = "Data Structures & Algorithms"
            self.s2 = "Database Management Systems"
            self.s3 = "Operating Systems"

        elif self.course == "IT":
            self.s1 = "Database Management Systems"
            self.s2 = "Computer Networks"
            self.s3 = "Web Technologies"

        elif self.course == "ME":
            self.s1 = "Thermodynamics"
            self.s2 = "Strength of Materials"
            self.s3 = "Theory of Machines"

        elif self.course == "CE":
            self.s1 = "Structural Analysis"
            self.s2 = "RCC Design"
            self.s3 = "Geotechnical Engineering"

        elif self.course == "EEE":
            self.s1 = "Electrical Machines"
            self.s2 = "Power Systems"
            self.s3 = "Control Systems"

        elif self.course == "ECE":
            self.s1 = "Digital Electronics"
            self.s2 = "Analog Electronics"
            self.s3 = "Communication Systems"

        self.m1 = get_mark(self.s1)
        self.m2 = get_mark(self.s2)
        self.m3 = get_mark(self.s3)
sub=Subjects()

class Marks():
    def __init__(self):
        self.total=round(sub.m1+sub.m2+sub.m3,2)
        self.avg=round(self.total/3,2)
        if self.avg>=90:
            self.grade = "A"
        elif 70<=self.avg<90:
            self.grade = "B"
        elif 50<=self.avg<70:
            self.grade = "C"
        elif 30<=self.avg<50:
            self.grade = "D"
        else:
            self.grade = "F"
mark=Marks()

print("\t--------------REPORT CARD----------------")
print("Name               : ",student.name)
print("Age                : ",student.age)
print("Register number    : ",student.reg_no)
print("Gender             : ",student.gender)
print("Hosteller          : ",student.is_hosteller)
print(f"{sub.s1:<35}: {sub.m1}")
print(f"{sub.s2:<35}: {sub.m2}")
print(f"{sub.s3:<35}: {sub.m3}")
print("Total: ",mark.total)
print("Average: ",mark.avg)
print("Grade: ",mark.grade)
print("\t-------------------------------------------")

#End of Program
