import tkinter as tk
from tkinter import messagebox
from tkinter import font

root = tk.Tk()
root.title("MCQ Quiz Game")
root['bg']="dark cyan"
root.geometry("1400x1000")

score = 0
current_question = 0
replay_button = None

questions = [
    {
        "question": "QUES1 Which of the following is not a keyword?",
        "options": ["pass", "nonlocal", "assert", "eval"],
        "answer": 0
    },
    {
        "question": "QUES2 Which of the following is not a core data type?",
        "options": ["Class", "Tuples", "Dictionary", "Lists"],
        "answer": 0
    },
    {
        "question": "QUES3 Who invented Python?",
        "options": ["Dennis Ritchie","Guido van Rossum","Charles Babbage","James Gosling"],
        "answer":1
    },
    {
        "question": "QUES4 Python programs are typed in which mode?",
        "options":["Interactive mode","Script mode","Interactive+Script mode","None of these"],
        "answer":1
    },
    {
        "question":"QUES5 Which of the following is not a python IDE?",
        "options":["IDLE","Spyder","Oracle","Sublime Text"],
        "answer":3
    },
    {
        "question":"QUES6 Data items having fixed value are called?",
        "options":["Identifiers","fuctions","Keywords","literals"],
        "answer":3
    },
    {
        "question":"QUES7 Escape sequences are treated as....",
        "options":["strings","characters","integers","none of these"],
        "answer":1
    },
    {
        "question":"QUES8 Which of the following are keywords?",
        "options":["name","Print","print","Input"],
        "answer":2
    },
    {
        "question":"QUES9 The default separator of character of print() is......",
        "options":["tab","space","newline","dot"],
        "answer":1
    },
    {
        "question":"QUES10 Negative index -1 belongs to ..... of string",
        "options":["first character","last character","second last character","second character"],
        "answer":1
    }
]

question_label = tk.Label(root, text="",font=("Algerian",28,"bold"))
option_buttons = []
next_button = None
submit_button = None
start_button = None

def start_quiz():
    global replay_button
    if replay_button is not None:
        replay_button.destroy()
    opening_frame.destroy()
    start_button.destroy()
    display_question()
    create_next_button()  # Create the "Next" button

def next_question():
    global current_question
    current_question += 1

    if current_question <len(questions):
        display_question()
        create_next_button()  # Create the "Next" button
    else:
        clear_screen()
        next_button.destroy()
        submit_button.pack(pady=300)

def check_answer(answer):
    global score
    if answer == questions[current_question]["answer"]:
        score += 1

def display_question():
    question_label.config(text=questions[current_question]["question"])
    question_label.pack(pady=80)

    # Clear previous buttons
    clear_buttons()

    # Create new buttons for options
    options = questions[current_question]["options"]

    for i ,option in enumerate(options):
       button=tk.Button(root,text=option,command=lambda ans =i:check_answer(ans),bg="gray92",font=("Times",16,"bold italic"))
       button.pack(pady=10)
       option_buttons.append(button)

def create_next_button():
    global next_button
    if next_button is not None:
        next_button.destroy()
    next_button = tk.Button(root, text="Next", command=next_question,font=("Times",28,"bold"),bg="yellow")
    next_button.pack(pady=60)

def clear_buttons():
    for button in option_buttons:
        button.destroy()
    
    option_buttons.clear()

def clear_screen():
    
    question_label.pack_forget()
    next_button.pack_forget()
    
    submit_button.pack_forget()
    clear_buttons()

def submit_quiz():
    clear_screen()
    global replay_button
    if replay_button is None:
        replay_button = tk.Button(root, text="Replay", command=start_quiz, font=("Times", 28, "bold"), bg="blue", width=10)
        replay_button.pack(pady=300)

    global score, current_question
    messagebox.showinfo("Quiz Completed", f"Your score is: {score}")
    score = 0
    current_question = 0


opening_frame = tk.Frame(root)
opening_frame.pack(pady=20)

opening_label = tk.Label(opening_frame, text="Welcome To MCQ Quiz Game!", font=("Algerian", 56, "bold"))
custom_font = font.Font(opening_label, opening_label.cget("font"))
custom_font.configure(underline=True)
opening_label.configure(font=custom_font)
opening_label.pack()

opening_inst = tk.Label(opening_frame, text="Rules & Instructions:", font=("Helvetica", 20, "bold"), fg="red")
c_font=font.Font(opening_inst,opening_inst.cget("font"))
c_font.configure(underline=True)
opening_inst.configure(font=c_font)
opening_inst.pack(pady=30)
opening_s = tk.Label(opening_frame, text=" 1. Questions will be asked on the topic-Python Language.",
                     font=("Times", 12, "bold italic"), fg="green")
opening_s.pack()
t = tk.Label(opening_frame, text="2. This game offers multiple choice questions which will have several options.",
              font=("Times", 12, "bold italic"), fg="green")
t.pack()
u = tk.Label(opening_frame, text="3. It will keep track of scores based on correct answers. 1 mark will be awarded for "
                                 "correct answers and 0 marks for wrong answers.",
              font=("Times", 12, "bold italic"), fg="green")
u.pack()
v = tk.Label(opening_frame, text="4. Finally, the overall score of the user will be displayed.",
              font=("Times", 12, "bold italic"), fg="green")
v.pack()

start_button = tk.Button(opening_frame, text="Start", command=start_quiz, font=("Times", 18,"bold"), bg="blue", width=10)
start_button.pack(pady=120)

submit_button = tk.Button(root, text="Submit", command=submit_quiz,font=("Times",28,"bold"),bg="red")

root.mainloop()