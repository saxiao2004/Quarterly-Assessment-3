# Susana Xiao
# Quarterly Assessment 3
# DS 3850 Section 001
# The first window interface will allow the user to select a category with quiz questions and then they would press a button to start the quiz.

# Import necessary libraries.
import tkinter as tk
from tkinter import ttk
import sqlite3

# Define the main Quiz application class
class QuizApp:
    def __init__(self, root, categories, db):
        # Initialize the main application window, categories, and database.
        self.root = root
        self.categories = categories
        self.db = db
        # Vairable to hold the selected category.
        self.selected_category = tk.StringVar()
        # List to store questions feteched from the database.
        self.questions = [] 
        # Index to track the current question.
        self.current_question_index = 0  
        # Setup the main window layout
        self.setup_window()

    # Fetch questions from the database based on the selected category.
    def fetch_questions(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        cursor.execute("SELECT question, choice_a, choice_b, choice_c, choice_d, correct_answer FROM QuizBowl_Questions WHERE category = ?", (self.selected_category.get(),))
        self.questions = cursor.fetchall()
        connection.close()

    # Start the quiz by fetching questions and showing the first question.
    def start_quiz(self):
        self.fetch_questions()
        self.current_question_index = 0
        # Hide the main window while displaying questions.
        self.root.withdraw()
        self.show_question()

    # Show the current question in a new window.
    def show_question(self):
        if self.current_question_index < len(self.questions):
            # Close the current question window if it exists
            if hasattr(self, 'question_window') and self.question_window:
                self.question_window.destroy()
            self.question_window = tk.Toplevel(self.root)
            question = self.questions[self.current_question_index]
            # Pass the question data to the QuestionApp for display.
            QuestionApp(self.question_window, question, self)
        else:
            # End the quiz if there are no more questions.
            self.end_quiz()

    # Move to the next question.
    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    # End the quiz and close the applications
    def end_quiz(self):
        if hasattr(self, 'question_window') and self.question_window:
            self.question_window.destroy()
        self.root.destroy()

    # Setup the main application windiw layout.
    def setup_window(self):
        self.root.title("Quiz Categories")
        dropdown_frame = tk.Frame(self.root)
        dropdown_frame.pack()
        ttk.Label(dropdown_frame, text="Select a Category:").pack(side='left')
        dropdown = ttk.Combobox(dropdown_frame, width=38, textvariable=self.selected_category, state='readonly')
        dropdown['values'] = self.categories
        dropdown.pack(side='left', padx=(10, 0))
        dropdown.current(0)

        start_button = ttk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        start_button.pack(pady=20)

# Define the Question application class to display individual questions.
class QuestionApp:
    def __init__(self, root, question, quiz_app):
        self.root = root
        self.question = question
        self.quiz_app = quiz_app 
        self.setup_ui()

    # Setup the question window UI
    def setup_ui(self):
        self.root.title("Quiz Application")
        question_label = tk.Label(self.root, text=self.question[0], wraplength=400)
        question_label.pack()
        self.options = [self.question[1], self.question[2], self.question[3], self.question[4]]
        self.correct_answer = self.question[5]
        for option in self.options:
            option_label = tk.Label(self.root, text=option, wraplength=400)
            option_label.pack()
        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack()
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    # Handle the submit section
    def submit(self):
        user_answer = "CORRECT ANSWER: " + self.answer_entry.get().strip().upper()
        correct_answer = self.correct_answer.strip().upper()
        if user_answer == correct_answer:
            self.result_label.config(text="Correct! You've selected the right answer.", fg="green")
        else:
            self.result_label.config(text="Incorrect. " + correct_answer, fg="red")
        next_question = tk.Button(self.root, text="Next question", command=self.next_question)
        next_question.pack()

    # Button to move to the next questions
    def next_question(self):
        self.quiz_app.next_question()

# Trigger the next question display.
if __name__ == "__main__":
    categories = ['Accounting', 'Money and Banking', 'Business Management', 'Operation Supply Chain Management', 'Data Driven Analytics', 'Business App Develop']
    db= 'Quiz_Questions.db' 
    root = tk.Tk()
    app = QuizApp(root, categories, db)
    root.mainloop()