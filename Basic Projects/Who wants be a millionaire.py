# import tkinter as tk
# from tkinter import ttk, messagebox
# import time

# class MillionaireGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Who Wants to Be a Millionaire")
#         self.root.geometry("900x700")
#         self.root.configure(bg='#000033')
#         self.root.resizable(False, False)
        
#         # Game data
#         self.questions = [
#             ['How many sides does a triangle have?', ['2', '3', '4', '5', [2]]],
#             ['Which ocean is the largest?', ['Atlantic', 'Pacific', 'Indian', 'Arctic', [2]]],
#             ['What is the capital of Australia?', ['Sydney', 'Melbourne', 'Canberra', 'Perth', [3]]],
#             ['Who painted the Mona Lisa?', ['Van Gogh', 'Picasso', 'Da Vinci', 'Monet', [3]]],
#             ['What is the smallest country in the world?', ['Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', [2]]],
#             ['Which element has the atomic number 1?', ['Helium', 'Hydrogen', 'Oxygen', 'Carbon', [2]]],
#             ['In which year did the Berlin Wall fall?', ['1987', '1989', '1991', '1993', [2]]],
#             ['What is the longest river in the world?', ['Amazon', 'Nile', 'Yangtze', 'Mississippi', [2]]],
#             ['Which composer wrote "The Four Seasons"?', ['Bach', 'Mozart', 'Beethoven', 'Vivaldi', [4]]],
#             ['What is the rarest naturally occurring element on Earth?', ['Francium', 'Astatine', 'Technetium', 'Promethium', [2]]]
#         ]
        
#         self.money_levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
#         self.safe_levels = {2: 2000, 4: 10000, 7: 80000}
        
#         # Game state
#         self.current_question = 0
#         self.winning_amount = 0
#         self.selected_option = tk.IntVar()
        
#         self.setup_ui()
#         self.show_welcome()
    
#     def setup_ui(self):
#         # Main frame
#         self.main_frame = tk.Frame(self.root, bg='#000033')
#         self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
#         # Title
#         self.title_label = tk.Label(
#             self.main_frame, 
#             text="WHO WANTS TO BE A MILLIONAIRE?", 
#             font=('Arial', 24, 'bold'),
#             fg='#FFD700', 
#             bg='#000033'
#         )
#         self.title_label.pack(pady=20)
        
#         # Money ladder frame
#         self.money_frame = tk.Frame(self.main_frame, bg='#000033')
#         self.money_frame.pack(side='right', fill='y', padx=(20, 0))
        
#         self.money_label = tk.Label(
#             self.money_frame,
#             text="MONEY LADDER",
#             font=('Arial', 14, 'bold'),
#             fg='#FFD700',
#             bg='#000033'
#         )
#         self.money_label.pack(pady=(0, 10))
        
#         # Money ladder
#         self.money_labels = []
#         for i in range(9, -1, -1):  # Display from highest to lowest
#             color = '#00FF00' if i == self.current_question else '#FFFFFF'
#             if i + 1 in [3, 5, 8]:  # Safe levels
#                 bg_color = '#FFD700'
#                 text_color = '#000033'
#             else:
#                 bg_color = '#000033'
#                 text_color = color
                
#             label = tk.Label(
#                 self.money_frame,
#                 text=f"{i+1:2d}  ${self.money_levels[i]:,}",
#                 font=('Arial', 12, 'bold'),
#                 fg=text_color,
#                 bg=bg_color,
#                 width=15
#             )
#             label.pack(pady=1)
#             self.money_labels.append(label)
        
#         # Game content frame
#         self.game_frame = tk.Frame(self.main_frame, bg='#000033')
#         self.game_frame.pack(side='left', fill='both', expand=True)
        
#         # Current winnings
#         self.winnings_label = tk.Label(
#             self.game_frame,
#             text="Current Winnings: $0",
#             font=('Arial', 16, 'bold'),
#             fg='#00FF00',
#             bg='#000033'
#         )
#         self.winnings_label.pack(pady=10)
        
#         # Question frame
#         self.question_frame = tk.Frame(self.game_frame, bg='#000066', relief='raised', bd=3)
#         self.question_frame.pack(fill='x', pady=20)
        
#         self.question_label = tk.Label(
#             self.question_frame,
#             text="",
#             font=('Arial', 14, 'bold'),
#             fg='#FFFFFF',
#             bg='#000066',
#             wraplength=500,
#             justify='center'
#         )
#         self.question_label.pack(pady=20)
        
#         # Options frame
#         self.options_frame = tk.Frame(self.game_frame, bg='#000033')
#         self.options_frame.pack(fill='x', pady=20)
        
#         # Option buttons
#         self.option_buttons = []
#         for i in range(4):
#             btn = tk.Radiobutton(
#                 self.options_frame,
#                 text="",
#                 variable=self.selected_option,
#                 value=i+1,
#                 font=('Arial', 12),
#                 fg='#FFFFFF',
#                 bg='#000066',
#                 selectcolor='#FFD700',
#                 activebackground='#000099',
#                 activeforeground='#FFFFFF',
#                 indicatoron=False,
#                 width=50,
#                 height=2
#             )
#             btn.pack(pady=5, fill='x')
#             self.option_buttons.append(btn)
        
#         # Control buttons frame
#         self.control_frame = tk.Frame(self.game_frame, bg='#000033')
#         self.control_frame.pack(pady=20)
        
#         self.submit_btn = tk.Button(
#             self.control_frame,
#             text="Final Answer",
#             command=self.submit_answer,
#             font=('Arial', 14, 'bold'),
#             bg='#FFD700',
#             fg='#000033',
#             width=15,
#             height=2
#         )
#         self.submit_btn.pack(side='left', padx=10)
        
#         self.quit_btn = tk.Button(
#             self.control_frame,
#             text="Take Money & Quit",
#             command=self.quit_game,
#             font=('Arial', 14, 'bold'),
#             bg='#FF6600',
#             fg='#FFFFFF',
#             width=18,
#             height=2
#         )
#         self.quit_btn.pack(side='left', padx=10)
        
#         # Welcome/Result frame
#         self.welcome_frame = tk.Frame(self.game_frame, bg='#000033')
        
#     def show_welcome(self):
#         self.hide_game_elements()
        
#         self.welcome_frame.pack(fill='both', expand=True)
        
#         welcome_text = """
# Welcome to 'Who Wants to Be a Millionaire'!

# 🎯 Answer 10 questions correctly to win $3,20,000!

# 💰 Safe levels at questions 3, 5, and 8
#    (You won't lose money below these levels)

# 📝 Rules:
#    • Select your answer and click 'Final Answer'
#    • You can quit anytime and keep your winnings
#    • Wrong answer drops you to last safe level

# Good Luck! 🍀
#         """
        
#         welcome_label = tk.Label(
#             self.welcome_frame,
#             text=welcome_text,
#             font=('Arial', 14),
#             fg='#FFFFFF',
#             bg='#000033',
#             justify='center'
#         )
#         welcome_label.pack(expand=True)
        
#         start_btn = tk.Button(
#             self.welcome_frame,
#             text="START GAME",
#             command=self.start_game,
#             font=('Arial', 18, 'bold'),
#             bg='#00FF00',
#             fg='#000033',
#             width=20,
#             height=3
#         )
#         start_btn.pack(pady=20)
    
#     def start_game(self):
#         self.welcome_frame.pack_forget()
#         self.show_game_elements()
#         self.display_question()
    
#     def hide_game_elements(self):
#         self.winnings_label.pack_forget()
#         self.question_frame.pack_forget()
#         self.options_frame.pack_forget()
#         self.control_frame.pack_forget()
    
#     def show_game_elements(self):
#         self.winnings_label.pack(pady=10)
#         self.question_frame.pack(fill='x', pady=20)
#         self.options_frame.pack(fill='x', pady=20)
#         self.control_frame.pack(pady=20)
    
#     def update_money_ladder(self):
#         for i, label in enumerate(self.money_labels):
#             question_num = 9 - i  # Reverse index
#             if question_num == self.current_question:
#                 label.configure(fg='#00FF00', bg='#FFD700')
#             elif question_num < self.current_question:
#                 label.configure(fg='#CCCCCC', bg='#000033')
#             else:
#                 if question_num + 1 in [3, 5, 8]:  # Safe levels
#                     label.configure(fg='#000033', bg='#FFD700')
#                 else:
#                     label.configure(fg='#FFFFFF', bg='#000033')
    
#     def display_question(self):
#         if self.current_question >= 10:
#             self.show_final_result(True)
#             return
        
#         self.update_money_ladder()
#         self.winnings_label.configure(text=f"Current Winnings: ${self.winning_amount:,}")
        
#         question_data = self.questions[self.current_question]
#         question_text = f"Question {self.current_question + 1}: {question_data[0]}"
#         self.question_label.configure(text=question_text)
        
#         # Set options
#         for i, btn in enumerate(self.option_buttons):
#             btn.configure(text=f"{chr(65+i)}. {question_data[1][i]}")
        
#         # Reset selection
#         self.selected_option.set(0)
        
#         # Enable buttons
#         self.submit_btn.configure(state='normal')
#         if self.current_question > 0:
#             self.quit_btn.configure(state='normal')
#         else:
#             self.quit_btn.configure(state='disabled')
    
#     def submit_answer(self):
#         if self.selected_option.get() == 0:
#             messagebox.showwarning("No Selection", "Please select an answer!")
#             return
        
#         self.submit_btn.configure(state='disabled')
#         self.quit_btn.configure(state='disabled')
        
#         # Check answer
#         correct_option = self.questions[self.current_question][1][4][0]
#         selected = self.selected_option.get()
        
#         if selected == correct_option:
#             self.winning_amount = self.money_levels[self.current_question]
#             messagebox.showinfo("Correct!", f"That's correct! You've won ${self.winning_amount:,}!")
#             self.current_question += 1
            
#             if self.current_question < 10:
#                 # Ask if they want to continue
#                 if self.current_question > 0:
#                     result = messagebox.askyesno(
#                         "Continue?", 
#                         f"You have ${self.winning_amount:,}. Do you want to continue to the next question?"
#                     )
#                     if not result:
#                         self.show_final_result(False)
#                         return
                
#                 self.display_question()
#             else:
#                 self.show_final_result(True)
#         else:
#             correct_answer = self.questions[self.current_question][1][correct_option-1]
#             messagebox.showerror(
#                 "Wrong Answer!", 
#                 f"Sorry, that's incorrect!\nThe correct answer was: {chr(64+correct_option)}. {correct_answer}"
#             )
            
#             # Calculate safe level amount
#             last_safe = 0
#             for question_num, amount in self.safe_levels.items():
#                 if self.current_question >= question_num:
#                     last_safe = amount
            
#             self.winning_amount = last_safe
#             self.show_final_result(False)
    
#     def quit_game(self):
#         result = messagebox.askyesno(
#             "Quit Game", 
#             f"Are you sure you want to quit and take ${self.winning_amount:,}?"
#         )
#         if result:
#             self.show_final_result(False)
    
#     def show_final_result(self, won_all):
#         self.hide_game_elements()
        
#         result_frame = tk.Frame(self.game_frame, bg='#000033')
#         result_frame.pack(fill='both', expand=True)
        
#         if won_all:
#             title_text = "🎉 CONGRATULATIONS! 🎉"
#             message_text = f"You've answered all 10 questions correctly!\nYou've won the maximum prize of ${self.winning_amount:,}!"
#             title_color = '#FFD700'
#         else:
#             title_text = "🎮 GAME OVER 🎮"
#             message_text = f"Thank you for playing!\nYou've answered {self.current_question} questions correctly.\nYou're taking home ${self.winning_amount:,}!"
#             title_color = '#FF6600'
        
#         result_title = tk.Label(
#             result_frame,
#             text=title_text,
#             font=('Arial', 20, 'bold'),
#             fg=title_color,
#             bg='#000033'
#         )
#         result_title.pack(pady=30)
        
#         result_message = tk.Label(
#             result_frame,
#             text=message_text,
#             font=('Arial', 16),
#             fg='#FFFFFF',
#             bg='#000033',
#             justify='center'
#         )
#         result_message.pack(pady=20)
        
#         # Buttons
#         button_frame = tk.Frame(result_frame, bg='#000033')
#         button_frame.pack(pady=30)
        
#         play_again_btn = tk.Button(
#             button_frame,
#             text="PLAY AGAIN",
#             command=self.restart_game,
#             font=('Arial', 14, 'bold'),
#             bg='#00FF00',
#             fg='#000033',
#             width=15,
#             height=2
#         )
#         play_again_btn.pack(side='left', padx=10)
        
#         exit_btn = tk.Button(
#             button_frame,
#             text="EXIT",
#             command=self.root.quit,
#             font=('Arial', 14, 'bold'),
#             bg='#FF0000',
#             fg='#FFFFFF',
#             width=15,
#             height=2
#         )
#         exit_btn.pack(side='left', padx=10)
    
#     def restart_game(self):
#         # Reset game state
#         self.current_question = 0
#         self.winning_amount = 0
#         self.selected_option.set(0)
        
#         # Clear the game frame
#         for widget in self.game_frame.winfo_children():
#             widget.destroy()
        
#         # Recreate the game elements
#         self.setup_game_frame()
#         self.show_welcome()
    
#     def setup_game_frame(self):
#         # Recreate game frame elements
#         self.winnings_label = tk.Label(
#             self.game_frame,
#             text="Current Winnings: $0",
#             font=('Arial', 16, 'bold'),
#             fg='#00FF00',
#             bg='#000033'
#         )
        
#         self.question_frame = tk.Frame(self.game_frame, bg='#000066', relief='raised', bd=3)
        
#         self.question_label = tk.Label(
#             self.question_frame,
#             text="",
#             font=('Arial', 14, 'bold'),
#             fg='#FFFFFF',
#             bg='#000066',
#             wraplength=500,
#             justify='center'
#         )
#         self.question_label.pack(pady=20)
        
#         self.options_frame = tk.Frame(self.game_frame, bg='#000033')
        
#         self.option_buttons = []
#         for i in range(4):
#             btn = tk.Radiobutton(
#                 self.options_frame,
#                 text="",
#                 variable=self.selected_option,
#                 value=i+1,
#                 font=('Arial', 12),
#                 fg='#FFFFFF',
#                 bg='#000066',
#                 selectcolor='#FFD700',
#                 activebackground='#000099',
#                 activeforeground='#FFFFFF',
#                 indicatoron=False,
#                 width=50,
#                 height=2
#             )
#             btn.pack(pady=5, fill='x')
#             self.option_buttons.append(btn)
        
#         self.control_frame = tk.Frame(self.game_frame, bg='#000033')
        
#         self.submit_btn = tk.Button(
#             self.control_frame,
#             text="Final Answer",
#             command=self.submit_answer,
#             font=('Arial', 14, 'bold'),
#             bg='#FFD700',
#             fg='#000033',
#             width=15,
#             height=2
#         )
#         self.submit_btn.pack(side='left', padx=10)
        
#         self.quit_btn = tk.Button(
#             self.control_frame,
#             text="Take Money & Quit",
#             command=self.quit_game,
#             font=('Arial', 14, 'bold'),
#             bg='#FF6600',
#             fg='#FFFFFF',
#             width=18,
#             height=2
#         )
#         self.quit_btn.pack(side='left', padx=10)
        
#         self.welcome_frame = tk.Frame(self.game_frame, bg='#000033')

# def main():
#     root = tk.Tk()
#     game = MillionaireGame(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
import tkinter as tk
from tkinter import ttk, messagebox
import time

class MillionaireGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Who Wants to Be a Millionaire")
        self.root.geometry("900x700")
        self.root.configure(bg='#000033')
        self.root.resizable(False, False)
        
        # Game data
        self.questions = [
            ['How many sides does a triangle have?', ['2', '3', '4', '5', [2]]],
            ['Which ocean is the largest?', ['Atlantic', 'Pacific', 'Indian', 'Arctic', [2]]],
            ['What is the capital of Australia?', ['Sydney', 'Melbourne', 'Canberra', 'Perth', [3]]],
            ['Who painted the Mona Lisa?', ['Van Gogh', 'Picasso', 'Da Vinci', 'Monet', [3]]],
            ['What is the smallest country in the world?', ['Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', [2]]],
            ['Which element has the atomic number 1?', ['Helium', 'Hydrogen', 'Oxygen', 'Carbon', [2]]],
            ['In which year did the Berlin Wall fall?', ['1987', '1989', '1991', '1993', [2]]],
            ['What is the longest river in the world?', ['Amazon', 'Nile', 'Yangtze', 'Mississippi', [2]]],
            ['Which composer wrote "The Four Seasons"?', ['Bach', 'Mozart', 'Beethoven', 'Vivaldi', [4]]],
            ['What is the rarest naturally occurring element on Earth?', ['Francium', 'Astatine', 'Technetium', 'Promethium', [2]]]
        ]
        
        self.money_levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
        self.safe_levels = {2: 2000, 4: 10000, 7: 80000}
        
        # Game state
        self.current_question = 0
        self.winning_amount = 0
        self.selected_option = tk.IntVar()
        
        self.setup_ui()
        self.show_welcome()
    
    def setup_ui(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg='#000033')
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame, 
            text="WHO WANTS TO BE A MILLIONAIRE?", 
            font=('Arial', 24, 'bold'),
            fg='#FFD700', 
            bg='#000033'
        )
        self.title_label.pack(pady=20)
        

        
        # Game content frame
        self.game_frame = tk.Frame(self.main_frame, bg='#000033')
        self.game_frame.pack(fill='both', expand=True)
        
        # Current winnings
        self.winnings_label = tk.Label(
            self.game_frame,
            text="Current Winnings: $0",
            font=('Arial', 16, 'bold'),
            fg='#00FF00',
            bg='#000033'
        )
        self.winnings_label.pack(pady=10)
        
        # Question frame
        self.question_frame = tk.Frame(self.game_frame, bg='#000066', relief='raised', bd=3)
        self.question_frame.pack(fill='x', pady=20)
        
        self.question_label = tk.Label(
            self.question_frame,
            text="",
            font=('Arial', 14, 'bold'),
            fg='#FFFFFF',
            bg='#000066',
            wraplength=500,
            justify='center'
        )
        self.question_label.pack(pady=20)
        
        # Options frame
        self.options_frame = tk.Frame(self.game_frame, bg='#000033')
        self.options_frame.pack(fill='x', pady=20)
        
        # Option buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=i+1,
                font=('Arial', 12),
                fg='#FFFFFF',
                bg='#000066',
                selectcolor='#FFD700',
                activebackground='#000099',
                activeforeground='#FFFFFF',
                indicatoron=False,
                width=50,
                height=2
            )
            btn.pack(pady=5, fill='x')
            self.option_buttons.append(btn)
        
        # Control buttons frame
        self.control_frame = tk.Frame(self.game_frame, bg='#000033')
        self.control_frame.pack(pady=20)
        
        self.submit_btn = tk.Button(
            self.control_frame,
            text="Final Answer",
            command=self.submit_answer,
            font=('Arial', 14, 'bold'),
            bg='#FFD700',
            fg='#000033',
            width=15,
            height=2
        )
        self.submit_btn.pack(side='left', padx=10)
        
        self.quit_btn = tk.Button(
            self.control_frame,
            text="Take Money & Quit",
            command=self.quit_game,
            font=('Arial', 14, 'bold'),
            bg='#FF6600',
            fg='#FFFFFF',
            width=18,
            height=2
        )
        self.quit_btn.pack(side='left', padx=10)
        
        # Welcome/Result frame
        self.welcome_frame = tk.Frame(self.game_frame, bg='#000033')
        
    def show_welcome(self):
        self.hide_game_elements()
        
        self.welcome_frame.pack(fill='both', expand=True)
        
        welcome_text = """
Welcome to 'Who Wants to Be a Millionaire'!

🎯 Answer 10 questions correctly to win $3,20,000!

💰 Safe levels at questions 3, 5, and 8
   (You won't lose money below these levels)

📝 Rules:
   • Select your answer and click 'Final Answer'
   • You can quit anytime and keep your winnings
   • Wrong answer drops you to last safe level

Good Luck! 🍀
        """
        
        welcome_label = tk.Label(
            self.welcome_frame,
            text=welcome_text,
            font=('Arial', 14),
            fg='#FFFFFF',
            bg='#000033',
            justify='center'
        )
        welcome_label.pack(expand=True)
        
        start_btn = tk.Button(
            self.welcome_frame,
            text="START GAME",
            command=self.start_game,
            font=('Arial', 18, 'bold'),
            bg='#00FF00',
            fg='#000033',
            width=20,
            height=3
        )
        start_btn.pack(pady=20)
    
    def start_game(self):
        self.welcome_frame.pack_forget()
        self.show_game_elements()
        self.display_question()
    
    def hide_game_elements(self):
        self.winnings_label.pack_forget()
        self.question_frame.pack_forget()
        self.options_frame.pack_forget()
        self.control_frame.pack_forget()
    
    def show_game_elements(self):
        self.winnings_label.pack(pady=10)
        self.question_frame.pack(fill='x', pady=20)
        self.options_frame.pack(fill='x', pady=20)
        self.control_frame.pack(pady=20)
    
    def update_winnings_display(self):
        self.winnings_label.configure(text=f"Current Winnings: ${self.winning_amount:,}")
    
    def display_question(self):
        if self.current_question >= 10:
            self.show_final_result(True)
            return
        
        self.update_winnings_display()
        
        question_data = self.questions[self.current_question]
        question_text = f"Question {self.current_question + 1}: {question_data[0]}"
        self.question_label.configure(text=question_text)
        
        # Set options
        for i, btn in enumerate(self.option_buttons):
            btn.configure(text=f"{chr(65+i)}. {question_data[1][i]}")
        
        # Reset selection
        self.selected_option.set(0)
        
        # Enable buttons
        self.submit_btn.configure(state='normal')
        if self.current_question > 0:
            self.quit_btn.configure(state='normal')
        else:
            self.quit_btn.configure(state='disabled')
    
    def submit_answer(self):
        if self.selected_option.get() == 0:
            self.question_label.configure(text="Please select an answer!", fg='#FF0000')
            return
        
        self.submit_btn.configure(state='disabled')
        self.quit_btn.configure(state='disabled')
        
        # Check answer
        correct_option = self.questions[self.current_question][1][4][0]
        selected = self.selected_option.get()
        
        if selected == correct_option:
            self.winning_amount = self.money_levels[self.current_question]
            self.question_label.configure(
                text=f"Correct! You've won ${self.winning_amount:,}!", 
                fg='#00FF00'
            )
            self.current_question += 1
            
            if self.current_question < 10:
                # Auto-continue after 2 seconds
                self.root.after(2000, self.ask_continue)
            else:
                self.root.after(2000, lambda: self.show_final_result(True))
        else:
            correct_answer = self.questions[self.current_question][1][correct_option-1]
            self.question_label.configure(
                text=f"Wrong! Correct answer: {chr(64+correct_option)}. {correct_answer}", 
                fg='#FF0000'
            )
            
            # Calculate safe level amount
            last_safe = 0
            for question_num, amount in self.safe_levels.items():
                if self.current_question >= question_num:
                    last_safe = amount
            
            self.winning_amount = last_safe
            self.root.after(3000, lambda: self.show_final_result(False))
    
    def ask_continue(self):
        if self.current_question > 1:  # After question 2 onwards, ask if they want to continue
            self.question_label.configure(
                text=f"You have ${self.winning_amount:,}. Continue to next question?", 
                fg='#FFD700'
            )
            
            # Show continue/quit buttons
            continue_btn = tk.Button(
                self.control_frame,
                text="Continue",
                command=self.continue_game,
                font=('Arial', 14, 'bold'),
                bg='#00FF00',
                fg='#000033',
                width=12,
                height=2
            )
            continue_btn.pack(side='left', padx=5)
            
            quit_now_btn = tk.Button(
                self.control_frame,
                text="Take Money",
                command=lambda: self.show_final_result(False),
                font=('Arial', 14, 'bold'),
                bg='#FF6600',
                fg='#FFFFFF',
                width=12,
                height=2
            )
            quit_now_btn.pack(side='left', padx=5)
            
            # Hide original buttons
            self.submit_btn.pack_forget()
            self.quit_btn.pack_forget()
        else:
            self.continue_game()
    
    def continue_game(self):
        # Remove continue/quit buttons if they exist
        for widget in self.control_frame.winfo_children():
            if widget not in [self.submit_btn, self.quit_btn]:
                widget.destroy()
        
        # Show original buttons
        self.submit_btn.pack(side='left', padx=10)
        self.quit_btn.pack(side='left', padx=10)
        
        self.display_question()
    
    def quit_game(self):
        self.question_label.configure(
            text=f"Are you sure you want to quit with ${self.winning_amount:,}?", 
            fg='#FFD700'
        )
        
        # Show confirm buttons
        yes_btn = tk.Button(
            self.control_frame,
            text="Yes, Quit",
            command=lambda: self.show_final_result(False),
            font=('Arial', 12, 'bold'),
            bg='#FF0000',
            fg='#FFFFFF',
            width=10
        )
        yes_btn.pack(side='left', padx=5)
        
        no_btn = tk.Button(
            self.control_frame,
            text="No, Continue",
            command=self.cancel_quit,
            font=('Arial', 12, 'bold'),
            bg='#00FF00',
            fg='#000033',
            width=12
        )
        no_btn.pack(side='left', padx=5)
        
        # Hide original buttons
        self.submit_btn.pack_forget()
        self.quit_btn.pack_forget()
    
    def cancel_quit(self):
        # Remove confirm buttons
        for widget in self.control_frame.winfo_children():
            if widget not in [self.submit_btn, self.quit_btn]:
                widget.destroy()
        
        # Show original buttons
        self.submit_btn.pack(side='left', padx=10)
        self.quit_btn.pack(side='left', padx=10)
        
        # Restore question
        self.display_question()
    
    def show_final_result(self, won_all):
        self.hide_game_elements()
        
        result_frame = tk.Frame(self.game_frame, bg='#000033')
        result_frame.pack(fill='both', expand=True)
        
        if won_all:
            title_text = "🎉 CONGRATULATIONS! 🎉"
            message_text = f"You've answered all 10 questions correctly!\nYou've won the maximum prize of ${self.winning_amount:,}!"
            title_color = '#FFD700'
        else:
            title_text = "🎮 GAME OVER 🎮"
            message_text = f"Thank you for playing!\nYou've answered {self.current_question} questions correctly.\nYou're taking home ${self.winning_amount:,}!"
            title_color = '#FF6600'
        
        result_title = tk.Label(
            result_frame,
            text=title_text,
            font=('Arial', 20, 'bold'),
            fg=title_color,
            bg='#000033'
        )
        result_title.pack(pady=30)
        
        result_message = tk.Label(
            result_frame,
            text=message_text,
            font=('Arial', 16),
            fg='#FFFFFF',
            bg='#000033',
            justify='center'
        )
        result_message.pack(pady=20)
        
        # Buttons
        button_frame = tk.Frame(result_frame, bg='#000033')
        button_frame.pack(pady=30)
        
        exit_btn = tk.Button(
            button_frame,
            text="EXIT",
            command=self.root.quit,
            font=('Arial', 14, 'bold'),
            bg='#FF0000',
            fg='#FFFFFF',
            width=15,
            height=2
        )
        exit_btn.pack(padx=10)
    


def main():
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()