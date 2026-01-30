class ClickButton:
    def __init__(self, button_name):
        self.button_name = button_name  # string variable
        self.click_count = 0  # integer variable

    @property
    def GetButtonName(self):
        return self.button_name

    @property
    def GetClickCount(self):
        return self.click_count

    def ClickCount(self):
        self.click_count += 1

    def reset(self):
        self.click_count = 0


Btn_1 = ClickButton("Submit Button")
for count in range(5):
    Btn_1.ClickCount()
print(f"Click Count: {Btn_1.GetClickCount}")
Btn_1.reset()
print(f"Click Count After Reset: {Btn_1.GetClickCount}")
