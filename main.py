import json
import random 
import tkinter as tk
from tkinter import messagebox

# Add the explore thing
# Fix the colours
# Add a dropdown 

# Defining the window and home screen
window = tk.Tk()
window.title("Vocabulary App")
window.geometry("700x600")
window.configure(bg='#f6f2ec')

Title_Label = tk.Label(window, text="Cowboy Dictionary", bg='#f6f2ec', fg="#f12c0a", font=("BOOKmanOpti", 30)).pack()


# Load the dictionary
def load_dictionary(filename="dictionary.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def explore():
    explore = tk.Toplevel(window)
    explore.title("Dictionary")
    explore.geometry("700x600")

    pairs = list(dictionary.items())

    for i, (word,meaning) in enumerate(pairs):
        word_label = tk.Label(explore, text=word, width=20, font=("BOOKmanOpti", 16), relief="ridge")
        word_label.grid(row=i, column=0, padx=5, pady=2)

        meaning_label = tk.Label(explore, text=meaning, width=20, font=("BOOKmanOpti", 16), relief="ridge")
        meaning_label.grid(row=i, column=1, padx=5, pady=2)

        remove_button = tk.Button(explore, text="Remove",width=10, font=("BOOKmanOpti", 16), relief="ridge")
        remove_button.grid(row=i, column=2, padx=5, pady=2)


# Clear the dictionary
def clear_dictionary():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all words?")
    if confirm:
        dictionary.clear()
        save_dictionary(dictionary)
        messagebox.showinfo("Cleared", "Dictionary has been cleared.")

# Save the dictionary
def save_dictionary(dictionary, filename="dictionary.json"):
    with open(filename, "w") as file:
        json.dump(dictionary, file, indent=4)

def add_word():
    word = word_entry.get().strip()
    meaning = meaning_entry.get().strip()
    if word and meaning:
        dictionary[word] = meaning
        save_dictionary(dictionary)
        word_entry.delete(0, tk.END)
        meaning_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Word added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter both a word and its meaning.")

def search_word():
    word = search_entry.get().strip()
    meaning = dictionary.get(word, "Word not found in dictionary.")
    result_label.config(text=f"Meaning: {meaning}")

def vocab_test():
    if len(dictionary) < 5:
        messagebox.showwarning("Not enough words", "Add at least 5 words.")
        return

    test_window = tk.Toplevel(window)
    test_window.title("Vocab Test")
    test_window.geometry("510x400")

    selected_pairs = random.sample(list(dictionary.items()), 5)
    meaning_labels = []

    for i, (word, meaning) in enumerate(selected_pairs):
        word_label = tk.Label(test_window, text=word, width=20, font=("BOOKmanOpti", 16), relief="ridge")
        word_label.grid(row=i, column=0, padx=5, pady=2)

        meaning_label = tk.Label(test_window, text="???", width=40, font=("BOOKmanOpti", 16), relief="ridge")
        meaning_label.grid(row=i, column=1, padx=5, pady=2)

        meaning_labels.append((meaning_label, meaning))

    def show_meanings():
        for lbl, meaning in meaning_labels:
            lbl.config(text=meaning)

    show_btn = tk.Button(test_window, text="Show Meanings", command=show_meanings)
    show_btn.grid(row=6, column=0, columnspan=2, pady=10)



dictionary = load_dictionary()

tk.Label(window ,text="Word:" ,font=("BOOKmanOpti", 14)).pack()
word_entry = tk.Entry(window, width=50)
word_entry.pack()

tk.Label(window, text="Meaning:" ,font=("BOOKmanOpti", 14)).pack()
meaning_entry = tk.Entry(window, width=50)
meaning_entry.pack()

tk.Button(window, text="Add Word" ,font=("BOOKmanOpti", 14), command=add_word).pack()

tk.Label(window, text="Search Word:",font=("BOOKmanOpti", 14)).pack()
search_entry = tk.Entry(window, width=50)
search_entry.pack()

tk.Button(window, text="Search",font=("BOOKmanOpti", 14) ,command=search_word).pack()

tk.Button(window, text="Vocab Test",font=("BOOKmanOpti", 14), command=vocab_test).pack()

tk.Button(window, text="Explore",font=("BOOKmanOpti", 14), command=explore).pack()

tk.Button(window, text="Clear Dictionary",font=("BOOKmanOpti", 14), command=clear_dictionary).pack(pady=5)


result_label = tk.Label(window, text="", font=("BOOKmanOpti", 14))
result_label.pack()

window.mainloop()
