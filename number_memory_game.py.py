import tkinter as tk
import random

class NumberMemoryGame:
	def __init__(self, root):
		self.root = root
		self.root.title("Number Memory Game")

		# Enable full screen
		self.root.attributes('-fullscreen', True)

		# Exit full screen by pressing the Escape key
		self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

		# Exit the game by pressing the 'q' key
		self.root.bind("q", lambda e: self.root.quit())

		self.score = 0
		self.attempts = 0
		self.min_value = 0
		self.max_value = 99
		self.font_size = 50  # Initial number size
		self.create_widgets()

	def create_widgets(self):
		# Create the label to display the score
		self.label_score = tk.Label(self.root, text="Score: 0", font=("Helvetica", 20))
		self.label_score.pack(pady=10)

		# Create the label that will display the number
		self.label_number = tk.Label(self.root, text="", font=("Helvetica", self.font_size))
		self.label_number.pack(pady=20, expand=True, side='top')  # Center vertically and horizontally

		# Create the entry field to enter the number
		self.entry_number = tk.Entry(self.root, font=("Helvetica", 20))
		self.entry_number.pack(pady=10, expand=True, side='top')  # Center vertically

		# Bind the Enter key to the number verification
		self.entry_number.bind("<Return>", self.verify_number)  # Press Enter to validate

		# Create the validation button
		self.button_validate = tk.Button(self.root, text="Validate", font=("Helvetica", 20), command=self.verify_number)
		self.button_validate.pack(pady=10, expand=True, side='top')  # Center vertically

		# Start the game by displaying a number
		self.display_number()

	def display_number(self):
		self.number_to_guess = random.randint(self.min_value, self.max_value)
		self.label_number.config(text=str(self.number_to_guess), fg="black")
		self.root.update()  # Refresh the interface to display the number
		self.root.after(500, self.clear_number)  # Clear after 0.5 seconds

	def clear_number(self):
		self.label_number.config(text="")  # Clear the text
		self.entry_number.focus()  # Refocus on the entry field

	def verify_number(self, event=None):  # Take into account the event for Enter
		try:
			# Get the user input
			entered_number = int(self.entry_number.get())
		except ValueError:
			self.label_number.config(text="Invalid input")
			self.root.after(1000, self.display_number)
			return

		# Compare with the displayed number
		if entered_number == self.number_to_guess:
			self.score += 1
			self.label_number.config(text="Well done!")
		else:
			self.label_number.config(text="Lost!")
			self.label_number.after(1000, lambda: self.label_number.config(text=f'Score: {self.score}'))
			self.root.after(1000, self.reset_game)  # Delay before resetting the game
			return

		self.attempts += 1
		self.entry_number.delete(0, tk.END)  # Clear the entry field
		self.label_score.config(text=f"Score: {self.score}")  # Update the score

		# Increase the size of the numbers every 10 attempts
		if self.attempts % 10 == 0:
			self.font_size += 10
			self.min_value = self.max_value + 1
			self.max_value = self.min_value * 10 - 1
			self.label_number.config(font=("Helvetica", self.font_size))

		# Display a new number after a delay
		self.root.after(1000, self.display_number)

	def reset_game(self):
		self.label_number.config(text=f"New game! Number: {self.number_to_guess}", font=("Helvetica", self.font_size), fg="red")
		self.attempts = 0
		self.score = 0
		self.font_size = 50
		self.min_value = 0
		self.max_value = 99
		self.label_score.config(text="Score: 0")  # Reset the displayed score
		self.label_number.after(2000, lambda: self.label_number.config(text="", font=("Helvetica", self.font_size)))
		self.entry_number.delete(0, tk.END)
		self.root.after(1000, self.display_number)  # Delay before displaying a new number


# Create the main window
root = tk.Tk()
app = NumberMemoryGame(root)

# Start the main tkinter loop
root.mainloop()
