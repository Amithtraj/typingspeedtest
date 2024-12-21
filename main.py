import time
import random
import os
import json
from datetime import datetime

class TypingTest:
    def __init__(self):
        self.difficulties = {
            'easy': self.get_easy_texts(),
            'medium': self.get_medium_texts(),
            'hard': self.get_hard_texts()
        }
        self.high_scores_file = 'typing_high_scores.json'
        self.load_high_scores()

    def get_easy_texts(self):
        return [
            "The sun sets in the west, painting the sky with brilliant hues of orange and pink.",
            "A gentle breeze rustles through the leaves, creating a peaceful melody in the garden.",
            "The old bookstore on the corner houses thousands of stories waiting to be discovered."
        ]

    def get_medium_texts(self):
        return [
            "The ancient civilization that once thrived in this valley left behind intricate artifacts and mysterious hieroglyphs that continue to puzzle archaeologists to this day.",
            "Scientists working at the cutting-edge research facility have made remarkable breakthroughs in quantum computing, potentially revolutionizing the way we process information.",
            "The experienced chef carefully selected fresh ingredients from the local market, combining traditional techniques with modern culinary innovations to create extraordinary dishes."
        ]

    def get_hard_texts(self):
        return [
            "The unprecedented technological advancement in artificial intelligence and machine learning has led to significant ethical considerations regarding privacy, autonomy, and the future of human-computer interaction in our increasingly interconnected society.",
            "Environmental scientists studying climate change patterns have observed accelerating glacial melting in polar regions, leading to rising sea levels and potential disruptions to global weather systems that could affect ecosystems worldwide.",
            "The renaissance period marked a transformative era in human history, characterized by groundbreaking achievements in art, literature, science, and philosophy, fundamentally changing how people perceived themselves and their relationship with the world around them."
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def calculate_wpm(self, time_elapsed, typed_chars):
        words = typed_chars / 5
        minutes = time_elapsed / 60
        return round(words / minutes)

    def calculate_accuracy(self, original_text, typed_text):
        if len(typed_text) == 0:
            return 0
        correct_chars = sum(1 for a, b in zip(original_text, typed_text) if a == b)
        max_length = max(len(original_text), len(typed_text))
        return round((correct_chars / max_length) * 100, 2)

    def calculate_score(self, wpm, accuracy, difficulty_multiplier):
        # Base score formula: (WPM * Accuracy%) * Difficulty Multiplier
        base_score = wpm * (accuracy / 100)
        final_score = round(base_score * difficulty_multiplier)
        return final_score

    def load_high_scores(self):
        try:
            with open(self.high_scores_file, 'r') as f:
                self.high_scores = json.load(f)
        except FileNotFoundError:
            self.high_scores = {'easy': [], 'medium': [], 'hard': []}

    def save_high_score(self, difficulty, score, wpm, accuracy):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_entry = {
            'score': score,
            'wpm': wpm,
            'accuracy': accuracy,
            'timestamp': timestamp
        }
        self.high_scores[difficulty].append(score_entry)
        self.high_scores[difficulty] = sorted(
            self.high_scores[difficulty],
            key=lambda x: x['score'],
            reverse=True
        )[:5]  # Keep only top 5 scores

        with open(self.high_scores_file, 'w') as f:
            json.dump(self.high_scores, f, indent=4)

    def display_high_scores(self, difficulty):
        print(f"\nHigh Scores for {difficulty.capitalize()} Level:")
        scores = self.high_scores[difficulty]
        if not scores:
            print("No high scores yet!")
            return
        
        print("\nRank  Score  WPM    Accuracy  Date")
        print("-" * 45)
        for i, score in enumerate(scores, 1):
            print(f"{i:2d}.   {score['score']:5d}  {score['wpm']:3d}    {score['accuracy']:5.1f}%   {score['timestamp']}")

    def get_detailed_stats(self, original_text, typed_text, time_elapsed):
        stats = {
            'total_characters': len(original_text),
            'characters_typed': len(typed_text),
            'correct_characters': sum(1 for a, b in zip(original_text, typed_text) if a == b),
            'errors': abs(len(original_text) - len(typed_text)) + sum(1 for a, b in zip(original_text, typed_text) if a != b),
            'time_elapsed': round(time_elapsed, 2)
        }
        return stats

    def run_test(self):
        self.clear_screen()
        print("Welcome to the Advanced Typing Speed Test!")
        print("\nSelect difficulty level:")
        print("1. Easy (1x score multiplier)")
        print("2. Medium (1.5x score multiplier)")
        print("3. Hard (2x score multiplier)")
        
        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice in ['1', '2', '3']:
                break
            print("Invalid choice. Please try again.")

        difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard'}
        multiplier_map = {'1': 1.0, '2': 1.5, '3': 2.0}
        
        difficulty = difficulty_map[choice]
        multiplier = multiplier_map[choice]
        
        text_to_type = random.choice(self.difficulties[difficulty])
        
        print("\nPrepare to type the following text:")
        print(f"\n{text_to_type}\n")
        input("Press Enter when you're ready to begin...")
        
        self.clear_screen()
        print("Type this text:\n")
        print(text_to_type + "\n")
        
        start_time = time.time()
        typed_text = input()
        end_time = time.time()
        
        time_elapsed = end_time - start_time
        wpm = self.calculate_wpm(time_elapsed, len(typed_text))
        accuracy = self.calculate_accuracy(text_to_type, typed_text)
        score = self.calculate_score(wpm, accuracy, multiplier)
        
        stats = self.get_detailed_stats(text_to_type, typed_text, time_elapsed)
        
        self.clear_screen()
        print("\n=== Test Results ===")
        print(f"\nDifficulty: {difficulty.capitalize()}")
        print(f"Time elapsed: {stats['time_elapsed']} seconds")
        print(f"Words per minute (WPM): {wpm}")
        print(f"Accuracy: {accuracy}%")
        print(f"Final Score: {score}")
        
        print("\n=== Detailed Statistics ===")
        print(f"Total characters: {stats['total_characters']}")
        print(f"Characters typed: {stats['characters_typed']}")
        print(f"Correct characters: {stats['correct_characters']}")
        print(f"Errors: {stats['errors']}")
        
        self.save_high_score(difficulty, score, wpm, accuracy)
        self.display_high_scores(difficulty)
        
        return score, difficulty

def main():
    typing_test = TypingTest()
    
    while True:
        score, difficulty = typing_test.run_test()
        
        print("\nWould you like to:")
        print("1. Try again")
        print("2. View high scores")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '2':
            typing_test.clear_screen()
            for diff in ['easy', 'medium', 'hard']:
                typing_test.display_high_scores(diff)
            input("\nPress Enter to continue...")
        elif choice != '1':
            print("\nThanks for practicing your typing speed!")
            break

if __name__ == "__main__":
    main()