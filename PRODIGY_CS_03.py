import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(not char.isalnum() for char in password)

    score = 0
    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digit:
        score += 1
    if special_char:
        score += 1

    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score == 2:
        return "Moderate"
    else:
        return "Weak"

def check_password_strength():
    password = password_entry.get()
    strength = assess_password_strength(password)
    messagebox.showinfo("Password Strength", f"Strength: {strength}")


root = tk.Tk()
root.title("Password Strength Checker")


password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)


check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

root.mainloop()
