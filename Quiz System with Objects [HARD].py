class Question:
    def __init__(self, question_text, correct_answer, points):
        self.__question_text = question_text  # Private string variable
        self.__correct_answer = correct_answer  # Private string variable
        self.__points = points  # Private integer variable
        self.__attempts_used = 0  # Private integer variable

    @property
    def GetQuestionText(self):
        return self.__question_text

    @property
    def GetAttemptsUsed(self):
        return self.__attempts_used

    def CheckAnswer(self, user_answer):
        self.__attempts_used += 1
        if user_answer.lower() == self.__correct_answer.lower():
            return True
        return False

    def CalculateScore(self):
        if self.__attempts_used == 1:
            return self.__points
        elif self.__attempts_used == 2:
            return self.__points // 2
        else:
            return self.__points // 4


Question_1 = Question(
    input("Enter the question: "),
    input("Enter the correct answer: "),
    int(input("Enter points for this question: ")),
)
print(f"\n")
while True:
    print(f"{Question_1.GetQuestionText}")
    user_answer = input(f"Enter your answer: ")
    if Question_1.CheckAnswer(user_answer):
        break
    print(f"Wrong! Try again ")

print(
    f"You scored {Question_1.CalculateScore()} points in {Question_1.GetAttemptsUsed} attempts"
)
