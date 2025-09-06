"""
Programmer: Sidd Hamsanipally
Project: Superhero quiz
Date 11/16/2023
"""

import tkinter as tk
from tkinter import messagebox

class SuperheroQuiz:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Superhero Quiz")

        # Questions for the quiz
        self.questions = ["Favorite color? \na) blue, b) red, c) Green, d) black",
                          "\nPreferred transportation? \na) flight, b) running c) teleportation d) vehicle",
                          "\nGreatest strength? \na) strength, b) fast reflexes, c) flexibility, d) intelligence"]
        # Superheroes corresponding to answer choices
        self.superheroes = {"a": "Superman", "b": "The Flash", "c": "Green Lantern", "d": "Professor X"}

        # Store user's answers
        self.user_answers = []

        # Track the current question
        self.current_question = 0

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Display the current question
        tk.Label(self.master, text=self.questions[self.current_question]).pack()

        # Create buttons for answer choices (a, b, c, d)
        for choice in ["a", "b", "c", "d"]:
            tk.Button(self.master, text=choice, command=lambda c=choice: self.record_answer(c)).pack(side=tk.LEFT)

    def record_answer(self, answer):
        # Record the user's answer and proceed to the next question
        self.user_answers.append(answer)
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def update_question(self):
        # Update the displayed question
        tk.Label(self.master, text=self.questions[self.current_question]).pack_forget()
        self.create_widgets()

    def show_result(self):
        # Display the result in a message box
        result = "".join([self.superheroes[answer] for answer in self.user_answers])
        messagebox.showinfo("Result", f"You are... {result}!")

if __name__ == "__main__":
    # Create the main window and run the application
    root = tk.Tk()
    app = SuperheroQuiz(root)
    root.mainloop()
