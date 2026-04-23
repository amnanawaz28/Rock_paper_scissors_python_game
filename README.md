# Rock_paper_scissors_python_game
This is my first ever coded game It is a simple command line interface implementation of the classic "Rock, Paper, Scissors" game built using Python.The game allows a user to play against the computer by selecting a number representing their move. The program handles user input, validates it to prevent crashes, and determines the winner.
Key Features:
Input Validation: The code checks if the user entered a valid number (0, 1, or 2) before processing.

Data Mapping: Uses Python dictionaries to translate computer numbers into human-readable strings (e.g., 0 becomes "rock").

Win/Loss Logic: A complete set of conditional statements to decide the outcome.

How to Play
Run the script using Python: python main.py

Enter a number when prompted:

0 for Rock

1 for Paper

2 for Scissors

The computer will randomly choose its move.

The result will be displayed on the screen!

Logic & Learning Journey
While building this game, I encountered and solved several logical challenges:

1. Data Type Consistency
I learned that comparing a String (like "rock") to an Integer (like 0) always results in False. I fixed this by keeping the game logic focused on integers and only using strings for display purposes.

2. Dictionary Lookups
I practiced using Python dictionaries to map keys to values. I learned the difference between using [] for lookups and why () is only for functions.

3. The "Safety Check" Pattern
I discovered that the order of code matters. I implemented a "Guardrail" if statement to check user input before the dictionary lookup to prevent KeyErrors.
