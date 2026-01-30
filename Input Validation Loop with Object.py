class exam:
    def __init__(self, subject_name, total_marks):
        self.subject_name = subject_name  # string name
        self.total_marks = total_marks  # integer variable
        self.obtained_marks = 0  # integer variable

    @property
    def GerSubjectName(self):
        return self.subject_name

    @property
    def GetTotalMarks(self):
        return self.total_marks

    def GetObtainedMarks(self, marks):
        if marks >= 0 and marks <= self.total_marks:
            self.obtained_marks = marks
            return True
        return False

    def CalculatePercentage(self):
        percentage = (self.obtained_marks / self.total_marks) * 100
        return percentage

    def GetGrade(self, percentage):
        if percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"


MyExam = exam("Computer Science", 100)
while True:
    marks = int(input("Enter obtained marks: "))
    if MyExam.GetObtainedMarks(marks):
        break
    else:
        print(f"invalid, try again! ")
        continue
percentage = MyExam.CalculatePercentage()
print(f"Percentage:{percentage}")
print(f"Grade:{MyExam.GetGrade(percentage)}")
