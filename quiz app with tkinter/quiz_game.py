from tkinter import *

# open file
file_location = "questions.txt"
file = open(file_location)

lines = [line.strip() for line in file]
questions = []
options = []
a_temp = []
answers = []

for i in range(len(lines)):

    if i in range(0, len(lines), 6):
        questions.append(lines[i])
    if i in range(1, len(lines), 6):
        opt = []
        for j in range(i, i+4):
            opt.append(lines[j])
        options.append(opt)
    if i in range(5, len(lines), 6):
        a_temp.append(lines[i])
for i in a_temp:
    answers.append(int(i))


class Quiz:
    def __init__(self, root):
        self.option = IntVar()
        self.q_no = 0
        self.correct = 0
        self.ques, self.opts = self.create_question(root, self.q_no, 4)
        self.display_question(self.q_no)
        self.button = Button(root, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_question(self, root, qn, n):
        question_label = Label(root, text=questions[qn])
        question_label.pack(side=TOP)
        opt_val = 0
        option_list = []
        while opt_val < n:
            btn = Radiobutton(root, variable=self.option, value=opt_val + 1)
            option_list.append(btn)
            btn.pack(side=TOP, anchor="w")
            opt_val = opt_val + 1
        return question_label, option_list

    def display_question(self, qn):
        opt_val = 0
        self.option.set(0)
        self.ques['text'] = questions[qn]
        for op in options[qn]:
            self.opts[opt_val]['text'] = op
            opt_val = opt_val + 1

    def next_btn(self):
        if self.option.get() == answers[self.q_no]:
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.q_no = self.q_no + 1
        if self.q_no >= len(questions):
            self.print_score()
        else:
            self.display_question(self.q_no)

    def print_score(self):
        score = "Your total score is: " + str(self.correct) + " out of " + str(len(questions))
        score_label = Label(root, text=str(score))
        score_label.pack(side=TOP)


root = Tk()
root.geometry("500x300")
app = Quiz(root)
root.mainloop()
