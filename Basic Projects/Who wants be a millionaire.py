questions = [
    ['Who is the PM of India: ', ['MODI', 'RAHUL', 'Kejrival', 'NONE', [1]]],
    ['Which planet is known as the Red Planet?', ['Earth', 'Mars', 'Venus', 'Jupiter', [2]]],
    ['What is the capital of France?', ['Madrid', 'Berlin', 'Paris', 'Rome', [3]]],
    ['Which element has the chemical symbol O?', ['Oxygen', 'Gold', 'Silver', 'Iron', [1]]],
    ['What year did World War II end?', ['1945', '1939', '1918', '1955', [1]]],
    ['Who wrote "Hamlet"?', ['Shakespeare', 'Dickens', 'Hemingway', 'Austen', [1]]],
    ['What is the largest mammal?', ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus', [2]]],
    ['How many continents are there?', ['5', '6', '7', '8', [3]]],
    ['Which country hosted the 2020 Summer Olympics?', ['Japan', 'Brazil', 'China', 'UK', [1]]],
    ['Which gas do plants absorb from the atmosphere?', ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen', [2]]]
]


money_levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
safe_levels = {2: 2000, 4: 10000, 7: 80000}  # Questions 3, 5, and 8 are safe levels

def display_welcome():
    print("Welcome to 'Who Wants to Be a Millionaire'!")
    print("Answer 10 questions correctly to win the grand prize of ₹320,000!")
    print("There are safe levels at questions 3, 5, and 8.")
    print("Let's begin!\n")

def main():
    display_welcome()
    correct_answers = 0
    winning_amount = 0
    
    for i in range(10):

        if i > 0:
            print(f"\nYou currently have ₹{winning_amount}")
            playing_status = input("Do you want to continue? (yes/no): ")
            if playing_status.lower() != "yes":
                print("\nThank You for playing! 😊😊")
                print(f"You walk away with ₹{winning_amount}!")
                break
        

        print(f"\nQuestion {i+1}: {questions[i][0]}")
        for j in range(4):
            print(f"{j+1}. {questions[i][1][j]}")
        

        while True:
            try:
                entered_option = int(input("Enter an option (1/2/3/4): "))
                if 1 <= entered_option <= 4:
                    break
                else:
                    print("Invalid option. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check if the answer is correct
        correct_option = questions[i][1][4][0]
        if entered_option == correct_option:
            correct_answers += 1
            winning_amount = money_levels[i]
            print(f"Correct! You've won ₹{winning_amount}!")
        else:
            print(f"Oops!!! That's incorrect. The correct answer was option {correct_option}: {questions[i][1][correct_option-1]}")
            
            # Find the last safe level the player reached
            last_safe = 0
            for question_num, amount in safe_levels.items():
                if i > question_num:
                    last_safe = amount
            
            winning_amount = last_safe
            print(f"You drop back to ₹{winning_amount}")
            break
    
    # If all questions were answered correctly
    if correct_answers == 10:
        print("\nCONGRATULATIONS! You've answered all questions correctly!")
        print(f"You've won the maximum prize of ₹{winning_amount}!")
    else:
        print(f"\nGame over! You've answered {correct_answers} questions correctly.")
        print(f"You've won ₹{winning_amount}!")

if __name__ == "__main__":
    main()