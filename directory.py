import os

# List of project names
projects = [
    "Simple Calculator", "Tic-Tac-Toe Game", "Weather App using OpenWeather API", "Quiz Application",
    "Rock, Paper, Scissors Game", "Number Guessing Game", "Hangman Game",
    "Flashcards App", "Pomodoro Timer", "To-Do List App", "BMI Calculator",
    "Unit Converter", "Simple Alarm Clock", "Student Grade Calculator",
    "Currency Converter using API", "Age Calculator", "Basic Web Scraper", 
    "Random Joke Generator", "Countdown Timer", "Simple Stopwatch", 
    "Random Password Generator", "Daily Quote Generator using API", "Basic Expense Tracker",
    "Prime Number Checker", "Palindrome Checker", "Simple Digital Clock",
    "Multiplication Table Generator", "Binary to Decimal Converter", 
    "Roman Numeral Converter", "Temperature Converter", "Python Notepad", 
    "Text-Based Adventure Game", "Simple Voting System", "Word Counter Tool", 
    "Simple ATM Interface", "Periodic Table Lookup", "Basic E-commerce System", 
    "Mad Libs Generator", "Sudoku Solver", "Maze Game", "Recipe Manager", 
    "Simple File Encryption/Decryption", "Binary Search Algorithm Simulation", 
    "Movie Recommendation System", "Password Strength Checker", "Calendar App", 
    "Simple Chatbot", "Spelling Checker", "Binary Image Creator", "Stopwatch with Laps", 
    "Music Player", "Simple Drawing App using Turtle", "Pong Game", "Basic Chess Game", 
    "Simple Blog System", "Task Manager App", "Weather Notifier", 
    "Random Compliment Generator", "Simple Calculator with GUI", "Periodic Table Quiz Game", 
    "Sudoku Generator", "Snake Game", "Password Manager", 
    "Cryptocurrency Price Tracker", "Unit Test Practice", "Budget Calculator", 
    "Personal Journal with Search Function", "Language Translator using API", 
    "Quiz Grader", "Drawing App with Pygame", "Online Study Flashcards", 
    "Dice Rolling Simulator", "Random Quote Machine", "Inventory Management System", 
    "Login and Registration System", "Task Automation Tool", "Python Portfolio Website", 
    "Word Scrambler Game", "HTML Page Generator", "Event Countdown Timer", 
    "File Backup Tool", "Quiz Game with Categories", "Sorting Algorithm Visualizer", 
    "Morse Code Converter", "Personal Finance Tracker", "HTML-to-PDF Converter", 
    "Expense Splitter", "ASCII Art Generator", "Contact Book", "GUI Stopwatch", 
    "Video Game Store System", "Typing Speed Test", "Data Visualization", 
    "Python Game with Pygame", "Event Countdown App", "Email Slicer", 
    "Python Space Invaders Game", "Text-Based RPG Game", "Quiz with Timer", "Voting App"
]

# Folder creation function with README file
def create_project_folders_with_readme():
    for i, project in enumerate(projects, start=1):
        folder_name = f"{i}. {project}"
        try:
            # Create the folder
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
            
            # Create README.md file
            readme_content = f"# {project}\n\nThis is the README file for the {project} project.\n\n## Description\n\nBrief description of the project.\n\n## Getting Started\n\nInstructions to get the project running.\n\n## Usage\n\nHow to use the project.\n\n## License\n\nThis project is licensed under the MIT License."
            readme_path = os.path.join(folder_name, 'README.md')
            
            with open(readme_path, 'w') as readme_file:
                readme_file.write(readme_content)
            
            print(f"README.md file created in '{folder_name}'.")
            
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")
        except Exception as e:
            print(f"Error creating folder or README.md in '{folder_name}': {e}")

# Run the function to create folders and README files
create_project_folders_with_readme()
