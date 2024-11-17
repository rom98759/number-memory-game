# Number Memory Game

The Number Memory Game is a Python-based memory training game built using the Tkinter library. The goal of the game is to test and improve your ability to remember and recall numbers displayed briefly on the screen.

## 🎮 How to Play

1. A random number will be displayed briefly on the screen (0.5 seconds).
2. After the number disappears, type the number into the input field.
3. Press Enter or click the Validate button to confirm your answer.
4. The game will respond:
   - **Correct Guess**: You earn a point.
   - **Incorrect Guess**: The game resets, and your score returns to 0.

---

## 🚀 Getting Started

To get started with the Number Memory Game, ensure you have Python 3.x or higher installed on your machine. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

---

To run the Number Memory Game on your local machine, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/rom98759/number-memory-game.git
```

2. Navigate to the project directory:

```bash
cd number-memory-game
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python memory_game.py
```

---

## 📋 Requirements

This project requires:

- **Python 3.x**
- The following dependencies (included in `requirements.txt`):
  - `tk` (Tkinter, included by default in most Python installations)

If `tkinter` is not installed on your system, follow the instructions below:

### Linux:
```bash
sudo apt-get install python3-tk
```

### macOS:
Tkinter is usually included with Python from the official installer.

### Windows:
Tkinter is included in the standard Python installation.

---

## 📈 Progressive Difficulty

The numbers become larger and more difficult to memorize after every 10 successful attempts. The font size increases to improve visibility.

| Successful Attempts | Number Range |
|---------------------|--------------|
| 1-10                | 0 to 99      |
| 11-20               | 100 to 999   |
| 21-30               | 1000 to 9999 |

---

## 📝 Feature

- **Exit the game**: Press the `q` key to exit the game at any time.
- **Escape full-screen mode**: Press the `Esc` key to exit full-screen mode.
- **Dynamic Interface**:
  - Labels and entry fields adjust for ease of use.
  - Immediate feedback on correct and incorrect guesses.
- **Score Tracking**: Your score is displayed and updated with each correct guess.

---

## 🌟 Future Improvements

- Add a leaderboard to track high scores.
- Introduce game levels with varying rules and challenges.
- Enhance the visual design with animations or themes.

---

## 🧑‍💻 Author

- **rom98759**

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
