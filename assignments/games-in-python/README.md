# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python that teaches string manipulation, control flow, and simple game state management.

## 📝 Tasks

### 🛠️ Game Core

#### Description
Implement the core Hangman gameplay: choose a secret word, accept letter guesses, reveal correct letters, and track remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list or from the provided `data.csv` word list.
- Accept single-letter guesses and display the current word progress (e.g. `_ a _ _ m _ n`).
- Track and display the number of incorrect guesses remaining.
- End the game when the player guesses the word or runs out of attempts.
- Display clear win or lose messages and reveal the secret word on loss.

### 🛠️ Extra Credit (optional)

#### Description
Add helpful features that improve user experience and demonstrate additional skills.

#### Requirements (choose any)

- Support difficulty levels that adjust number of allowed mistakes.
- Load word list from a CSV or text file in the assignment folder.
- Prevent repeated guesses from counting against the player and show letters already guessed.
- Add ASCII-art or a simple hangman drawing that updates with each wrong guess.

## 🧰 Starter Code

A starter file `starter-code.py` is provided to help you get started. Use it as the foundation or write your own implementation from scratch.

## ▶️ How to run

Run the game from the assignment folder with Python 3:

```bash
python3 starter-code.py
```

## 📚 Skills Practiced

- String manipulation
- Loops and conditionals
- Random selection and file I/O (optional)
- Basic program structure and user interaction

Good luck — have fun building the game!
