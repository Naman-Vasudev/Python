# ============================================================================
# TKINTER MESSAGEBOX COMPLETE REFERENCE
from tkinter import *
from tkinter import messagebox

# ============================================================================
# 1. INFORMATION MESSAGES
# ============================================================================

# showinfo() - Shows an information dialog
# Returns: 'ok'
messagebox.showinfo("Title", "This is an information message")
messagebox.showinfo("Info", "Your file has been saved successfully!")

# ============================================================================
# 2. WARNING MESSAGES
# ============================================================================

# showwarning() - Shows a warning dialog
# Returns: 'ok'
messagebox.showwarning("Warning", "This action cannot be undone")
messagebox.showwarning("Warning", "Low disk space detected!")

# ============================================================================
# 3. ERROR MESSAGES
# ============================================================================

# showerror() - Shows an error dialog
# Returns: 'ok'
messagebox.showerror("Error", "File not found!")
messagebox.showerror("Error", "Connection failed. Please try again.")

# ============================================================================
# 4. QUESTION DIALOGS (YES/NO TYPE)
# ============================================================================

# askquestion() - Shows a question dialog with Yes/No buttons
# Returns: 'yes' or 'no'
result = messagebox.askquestion("Question", "Do you want to save changes?")
if result == 'yes':
    print("User clicked Yes")
else:
    print("User clicked No")

# askyesno() - Shows a question dialog with Yes/No buttons
# Returns: True or False (boolean)
result = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
if result:
    print("User clicked Yes - Delete confirmed")
else:
    print("User clicked No - Delete cancelled")

# ============================================================================
# 5. OK/CANCEL DIALOGS
# ============================================================================

# askokcancel() - Shows a dialog with OK/Cancel buttons
# Returns: True or False (boolean)
result = messagebox.askokcancel("Confirm", "Do you want to continue?")
if result:
    print("User clicked OK")
else:
    print("User clicked Cancel")

# ============================================================================
# 6. RETRY/CANCEL DIALOGS
# ============================================================================

# askretrycancel() - Shows a dialog with Retry/Cancel buttons
# Returns: True or False (boolean)
result = messagebox.askretrycancel("Connection Error", "Failed to connect. Retry?")
if result:
    print("User clicked Retry")
else:
    print("User clicked Cancel")

# ============================================================================
# 7. YES/NO/CANCEL DIALOGS
# ============================================================================

# askyesnocancel() - Shows a dialog with Yes/No/Cancel buttons
# Returns: True (Yes), False (No), or None (Cancel)
result = messagebox.askyesnocancel("Save Changes", "Do you want to save before closing?")
if result is True:
    print("User clicked Yes - Save and close")
elif result is False:
    print("User clicked No - Close without saving")
else:  # result is None
    print("User clicked Cancel - Don't close")

# ============================================================================
# 8. COMPLETE WORKING EXAMPLE
# ============================================================================

def complete_example():
    root = Tk()
    root.title("MessageBox Examples")
    root.geometry("400x500")
    
    # Function to demonstrate each messagebox
    def show_info():
        messagebox.showinfo("Information", "This is an info message!")
    
    def show_warning():
        messagebox.showwarning("Warning", "This is a warning message!")
    
    def show_error():
        messagebox.showerror("Error", "This is an error message!")
    
    def ask_question():
        result = messagebox.askquestion("Question", "Do you like Python?")
        messagebox.showinfo("Result", f"You answered: {result}")
    
    def ask_yesno():
        result = messagebox.askyesno("Yes/No", "Continue with the operation?")
        messagebox.showinfo("Result", f"You chose: {'Yes' if result else 'No'}")
    
    def ask_okcancel():
        result = messagebox.askokcancel("OK/Cancel", "Proceed with action?")
        messagebox.showinfo("Result", f"You chose: {'OK' if result else 'Cancel'}")
    
    def ask_retrycancel():
        result = messagebox.askretrycancel("Retry/Cancel", "Operation failed. Retry?")
        messagebox.showinfo("Result", f"You chose: {'Retry' if result else 'Cancel'}")
    
    def ask_yesnocancel():
        result = messagebox.askyesnocancel("Yes/No/Cancel", "Save changes before exit?")
        if result is True:
            msg = "Yes - Save and exit"
        elif result is False:
            msg = "No - Exit without saving"
        else:
            msg = "Cancel - Don't exit"
        messagebox.showinfo("Result", msg)
    
    # Create buttons for each messagebox type
    Button(root, text="Show Info", command=show_info, width=20).pack(pady=5)
    Button(root, text="Show Warning", command=show_warning, width=20).pack(pady=5)
    Button(root, text="Show Error", command=show_error, width=20).pack(pady=5)
    Button(root, text="Ask Question", command=ask_question, width=20).pack(pady=5)
    Button(root, text="Ask Yes/No", command=ask_yesno, width=20).pack(pady=5)
    Button(root, text="Ask OK/Cancel", command=ask_okcancel, width=20).pack(pady=5)
    Button(root, text="Ask Retry/Cancel", command=ask_retrycancel, width=20).pack(pady=5)
    Button(root, text="Ask Yes/No/Cancel", command=ask_yesnocancel, width=20).pack(pady=5)
    
    root.mainloop()



# ============================================================================
#  RETURN VALUES SUMMARY
# ============================================================================

# Function                  | Return Values
# --------------------------|----------------------------------
# showinfo()               | 'ok'
# showwarning()            | 'ok'  
# showerror()              | 'ok'
# askquestion()            | 'yes' or 'no'
# askyesno()               | True or False
# askokcancel()            | True or False
# askretrycancel()         | True or False
# askyesnocancel()         | True, False, or None

# ============================================================================
# 12. COMMON USE CASES
# ============================================================================

# Use showinfo() for: Success messages, general information
# Use showwarning() for: Warnings that don't stop execution
# Use showerror() for: Error messages, failed operations
# Use askquestion() for: Simple yes/no questions (returns string)
# Use askyesno() for: Yes/no questions (returns boolean - easier to work with)
# Use askokcancel() for: Confirmation dialogs, proceed/cancel choices
# Use askretrycancel() for: Error recovery, retry operations
# Use askyesnocancel() for: Save dialogs, three-way choices

# ============================================================================
# END OF MESSAGEBOX REFERENCE
# ============================================================================

# Run the complete example (uncomment the line below)
# complete_example()
