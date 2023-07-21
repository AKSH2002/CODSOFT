import tkinter as tk
from tkinter import messagebox
import random
import json

def load_questions_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data["questions"]

def show_question():
    global current_question, questions, score
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=f"Question {current_question+1}/4: {question_data['question']}")

        if "choices" in question_data:
            for i, choice in enumerate(question_data["choices"], start=97):
                choices[i].config(text=f"{chr(i)}. {choice}")
        else:
            for i in range(97, 101):
                choices[i].config(text="")

def check_answer(choice):
    global current_question, questions, score
    question_data = questions[current_question]
    user_answer = choice - 97

    if user_answer < 0 or user_answer >= len(question_data["choices"]):
        return

    if question_data["choices"][user_answer] == question_data["answer"]:
        score += 1

    current_question += 1

    if current_question >= 4:
        show_result()
    else:
        show_question()

def show_result():
    global score
    final_score = (score / 4) * 100
    result_message = f"Quiz Completed!\nNumber of Correct Answers: {score}/4"

    if final_score >= 70:
        result_message += "\nGreat job! You have a good knowledge of India."
    else:
        result_message += "\nYou can do better next time. Keep learning!"

    messagebox.showinfo("Quiz Result", result_message)
    restart_button.pack(pady=20)
    start_button.pack_forget()

def restart_quiz():
    global current_question, score
    current_question = 0
    score = 0
    random.shuffle(questions)
    show_question()
    start_button.pack(pady=20)
    restart_button.pack_forget()

# Load questions from JSON file
questions = load_questions_from_file("questions.json")

# Initialize global variables
current_question = 0
score = 0

# Create the main application window
app = tk.Tk()
app.title("India Quiz Game")
app.geometry("400x300")

# Create and place widgets
question_label = tk.Label(app, text="", wraplength=300)
question_label.pack(pady=20)

choices = {}
for i in range(97, 101):
    choices[i] = tk.Button(app, text="", width=30, command=lambda c=i: check_answer(c))
    choices[i].pack()

start_button = tk.Button(app, text="Start Quiz", command=show_question)
start_button.pack(pady=20)

restart_button = tk.Button(app, text="Restart Quiz", command=restart_quiz)

# Start the main event loop
app.mainloop()
