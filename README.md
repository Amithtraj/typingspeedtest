Python Typing Speed Test
A feature-rich command-line typing speed test application that measures typing speed, accuracy, and maintains high scores across different difficulty levels.
Features

Multiple Difficulty Levels

Easy: Short sentences with basic vocabulary
Medium: Complex sentences with moderate difficulty
Hard: Long paragraphs with advanced vocabulary and punctuation


Comprehensive Scoring System

Words Per Minute (WPM) calculation
Accuracy percentage
Difficulty-based score multipliers
Persistent high scores storage


Detailed Statistics

Character count analysis
Error tracking
Time elapsed
Performance history



Installation

Clone the repository:

bashCopygit clone https://github.com/Amithtraj/typing-speed-test.git
cd typing-speed-test

No additional dependencies required - uses Python standard library only.

Usage
Run the program using Python 3:
bashCopypython typing_test.py
Follow the on-screen instructions to:

Select difficulty level
Read and prepare to type the displayed text
Press Enter to begin the test
Type the text as accurately and quickly as possible
View your results and statistics
Choose to retry or view high scores

Project Structure
Copytyping-speed-test/
│
├── typing_test.py          # Main application file
├── typing_high_scores.json # High scores storage (auto-generated)
├── README.md              # Project documentation
└── .gitignore            # Git ignore file
.gitignore Configuration
Create a .gitignore file with the following contents:
Copy# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# High Scores File (optional - remove if you want to track high scores)
typing_high_scores.json

# IDE specific files
.idea/
.vscode/
*.swp
*.swo
.DS_Store
Technical Details
Class Structure

TypingTest: Main class containing all functionality

Text management for different difficulty levels
Score calculation and storage
Statistics generation
High score tracking



Scoring Formula
pythonCopyfinal_score = (WPM * accuracy_percentage) * difficulty_multiplier

# Difficulty Multipliers
Easy:   1.0x
Medium: 1.5x
Hard:   2.0x
Performance Metrics

WPM Calculation: (characters_typed / 5) / minutes_elapsed
Accuracy: (correct_characters / total_characters) * 100
Final Score: (WPM * accuracy_percentage) * difficulty_multiplier

Contributing

Fork the repository
Create a feature branch: git checkout -b feature-name
Commit changes: git commit -am 'Add feature'
Push to branch: git push origin feature-name
Submit a Pull Request

Future Enhancements

Real-time error highlighting
Custom text input support
Typing practice mode
Progress tracking over time
Online leaderboard integration
Different languages support
Custom themes

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Inspired by various typing test applications
Thanks to the Python community for standard library tools

Version History

v1.0.0 (Initial Release)

Basic typing test functionality
Three difficulty levels
High score system
Detailed statistics