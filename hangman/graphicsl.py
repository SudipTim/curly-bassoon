import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

def word_selection():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        word = random.choice(lines).strip()
        return word

class WordGuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.attempts = 7
        self.word = word_selection()
        self.letters = list(self.word)
        self.hidden_word = ["_" for _ in self.word]
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Word Guessing Game")
        self.setFixedSize(400, 300)

        # Apply CSS styles to the window
        self.setStyleSheet("""
            QWidget {
                background-color: #2e3b4e;
                color: #ffffff;
                font-family: Arial;
            }
            QLabel {
                font-size: 18px;
                margin: 10px 0;
            }
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                border: 2px solid #ffffff;
                font-size: 18px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
                margin: 10px 0;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #a5a5a5;
            }
        """)

        # Create layout and widgets
        self.layout = QVBoxLayout()

        self.word_label = QLabel(" ".join(self.hidden_word))
        self.word_label.setStyleSheet("font-weight: bold; font-size: 22px; letter-spacing: 2px;")
        self.layout.addWidget(self.word_label)

        self.status_label = QLabel(f"Attempts Left: {self.attempts}")
        self.status_label.setStyleSheet("font-size: 16px; color: #ffcc00;")
        self.layout.addWidget(self.status_label)

        self.guess_input = QLineEdit()
        self.guess_input.setMaxLength(1)  # One character guess
        self.layout.addWidget(self.guess_input)

        self.submit_button = QPushButton("Submit Guess")
        self.submit_button.clicked.connect(self.submit_guess)
        self.layout.addWidget(self.submit_button)

        self.new_game_button = QPushButton("New Game")
        self.new_game_button.clicked.connect(self.new_game)
        self.layout.addWidget(self.new_game_button)

        # Set layout
        self.setLayout(self.layout)

    def submit_guess(self):
        guess = self.guess_input.text().lower().strip()
        if len(guess) != 1:
            QMessageBox.warning(self, "Invalid Input", "Please enter a single letter.")
            return

        if guess in self.letters:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.hidden_word[index] = letter
            self.word_label.setText(" ".join(self.hidden_word))
        else:
            self.attempts -= 1
            self.status_label.setText(f"Attempts Left: {self.attempts}")

        # Check for game over conditions
        if "_" not in self.hidden_word:
            QMessageBox.information(self, "You Win!", f"Congratulations! You guessed the word: {self.word}")
            self.disable_game()

        elif self.attempts <= 0:
            QMessageBox.information(self, "Game Over", f"Out of attempts! The word was: {self.word}")
            self.disable_game()

        self.guess_input.clear()

    def new_game(self):
        self.word = word_selection()
        self.letters = list(self.word)
        self.hidden_word = ["_" for _ in self.word]
        self.attempts = 7

        # Reset UI
        self.word_label.setText(" ".join(self.hidden_word))
        self.status_label.setText(f"Attempts Left: {self.attempts}")
        self.guess_input.clear()
        self.submit_button.setEnabled(True)

    def disable_game(self):
        self.submit_button.setEnabled(False)

# Main part of the code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = WordGuessingGame()
    window.show()

    sys.exit(app.exec_())
